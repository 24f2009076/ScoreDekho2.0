from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from controllers.database import Base

"""
ScoreDekho — models.py
SQLAlchemy ORM models for Supabase (PostgreSQL)

Tables:
  Auth layer        : users
  Player registry   : players
  Tournament layer  : tournaments, teams, auction_group_config, tournament_players
  Auction log       : auction_bids
  Match layer       : matches, innings, deliveries, match_state
"""

import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class UserRole(str, enum.Enum):
    # Kept minimal — credential control is the access control.
    # All authenticated users have full write access.
    authenticated = "authenticated"


class SkillType(str, enum.Enum):
    batsman        = "batsman"
    bowler         = "bowler"
    all_rounder    = "all_rounder"
    wicket_keeper  = "wicket_keeper"


class BattingStyle(str, enum.Enum):
    right_hand = "right_hand"
    left_hand  = "left_hand"


class BowlingStyle(str, enum.Enum):
    right_arm_fast         = "right_arm_fast"
    right_arm_medium       = "right_arm_medium"
    right_arm_off_spin     = "right_arm_off_spin"
    right_arm_leg_spin     = "right_arm_leg_spin"
    left_arm_fast          = "left_arm_fast"
    left_arm_medium        = "left_arm_medium"
    left_arm_orthodox_spin = "left_arm_orthodox_spin"
    left_arm_chinaman      = "left_arm_chinaman"
    none                   = "none"


class TournamentStatus(str, enum.Enum):
    draft     = "draft"      # Being set up
    auction   = "auction"    # Auction in progress
    ongoing   = "ongoing"    # Matches being played
    completed = "completed"  # Tournament over


class AuctionGroup(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"


class AuctionStatus(str, enum.Enum):
    pending = "pending"   # Not yet come up for bidding
    live    = "live"      # Currently on the podium
    sold    = "sold"      # Successfully sold to a team
    unsold  = "unsold"    # Went through auction, no bids met base price


class TossDecision(str, enum.Enum):
    bat  = "bat"
    bowl = "bowl"


class MatchStatus(str, enum.Enum):
    scheduled  = "scheduled"
    live       = "live"
    completed  = "completed"
    abandoned  = "abandoned"


class InningsStatus(str, enum.Enum):
    pending   = "pending"
    live      = "live"
    completed = "completed"


class ExtraType(str, enum.Enum):
    wide    = "wide"
    no_ball = "no_ball"
    bye     = "bye"
    leg_bye = "leg_bye"
    none    = "none"


class WicketType(str, enum.Enum):
    bowled            = "bowled"
    caught            = "caught"
    lbw               = "lbw"
    run_out           = "run_out"
    stumped           = "stumped"
    hit_wicket        = "hit_wicket"
    caught_and_bowled = "caught_and_bowled"
    retired_hurt      = "retired_hurt"


# ---------------------------------------------------------------------------
# Auth layer
# ---------------------------------------------------------------------------

class User(Base):
    """
    Authenticated users — admins and scorers trusted with login credentials.
    Unauthenticated visitors are spectators and have no row here.
    """
    __tablename__ = "users"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name     = Column(String(120), nullable=False)
    email         = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at    = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Audit trail — players this user added
    players_added = relationship("Player", back_populates="created_by_user")
    tournaments_created = relationship("Tournament", back_populates="created_by_user")


# ---------------------------------------------------------------------------
# Player registry
# ---------------------------------------------------------------------------

class Player(Base):
    """
    Not a system user — no login credentials.
    Added manually or via CSV import by an authenticated user.
    """
    __tablename__ = "players"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name     = Column(String(120), nullable=False)
    # housing_unit  = Column(String(60), nullable=True)
    phone         = Column(String(20), nullable=True)
    skill_type    = Column(Enum(SkillType), nullable=False)
    # batting_style = Column(Enum(BattingStyle), nullable=True)
    # bowling_style = Column(Enum(BowlingStyle), nullable=True, default=BowlingStyle.none)

    # Audit — who added this player
    created_by    = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at    = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    created_by_user      = relationship("User", back_populates="players_added")
    tournament_entries   = relationship("TournamentPlayer", back_populates="player")
    deliveries_as_batter = relationship("Delivery", foreign_keys="Delivery.batter_id", back_populates="batter")
    deliveries_as_bowler = relationship("Delivery", foreign_keys="Delivery.bowler_id", back_populates="bowler")
    dismissals           = relationship("Delivery", foreign_keys="Delivery.dismissed_player_id", back_populates="dismissed_player")


# ---------------------------------------------------------------------------
# Tournament layer
# ---------------------------------------------------------------------------

class Tournament(Base):
    """
    A season edition of the housing complex cricket tournament.
    Holds global config: overs, purse, and points system.
    """
    __tablename__ = "tournaments"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name           = Column(String(120), nullable=False)
    created_by     = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    season_year    = Column(String(9), nullable=False)   # e.g. "2025" or "2024-25"
    status         = Column(Enum(TournamentStatus), nullable=False, default=TournamentStatus.draft)
    # overs_per_side = Column(Integer, nullable=False, default=20)

    # Auction config — same purse for every team in this tournament
    team_purse     = Column(Integer, nullable=False, default=100000)

    # Points system — configurable per tournament
    points_per_win = Column(Integer, nullable=False, default=2)
    points_per_tie = Column(Integer, nullable=False, default=1)

    starts_at      = Column(DateTime, nullable=True)
    ends_at        = Column(DateTime, nullable=True)

    # Relationships
    teams              = relationship("Team", back_populates="tournament")
    auction_group_configs = relationship("AuctionGroupConfig", back_populates="tournament")
    tournament_players = relationship("TournamentPlayer", back_populates="tournament")
    matches            = relationship("Match", back_populates="tournament")
    created_by_user = relationship("User", back_populates="tournaments_created")


class Team(Base):
    """
    A team competing within a specific tournament.
    Budget is computed: tournament.team_purse - SUM(sold_price) for this team.
    """
    __tablename__ = "teams"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    name          = Column(String(80), nullable=False)
    # home_color    = Column(String(7), nullable=True)   # Hex color e.g. "#FF6D00"

    # Relationships
    tournament         = relationship("Tournament", back_populates="teams")
    tournament_players = relationship("TournamentPlayer", back_populates="team")
    auction_bids       = relationship("AuctionBid", back_populates="team")


class AuctionGroupConfig(Base):
    """
    Per-tournament configuration for each player group (A, B, C).
    Defines the base price and bid increment for that group.
    Exactly 3 rows per tournament — one per group.
    """
    __tablename__ = "auction_group_config"
    __table_args__ = (
        UniqueConstraint("tournament_id", "group", name="uq_auction_group_per_tournament"),
    )

    id               = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id    = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    group            = Column(Enum(AuctionGroup), nullable=False)
    base_price       = Column(Integer, nullable=False)
    increment_amount = Column(Integer, nullable=False)

    # Relationships
    tournament = relationship("Tournament", back_populates="auction_group_configs")


class TournamentPlayer(Base):
    """
    Junction table linking a player to a tournament.
    Carries auction outcome (group, sold_price, team) for that season.
    Stats (runs, wickets etc.) are NOT stored here —
    they are always computed live from the deliveries table.
    """
    __tablename__ = "tournament_players"
    __table_args__ = (
        UniqueConstraint("tournament_id", "player_id", name="uq_player_per_tournament"),
    )

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    player_id     = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=False)

    # Nullable until the player is sold at auction
    team_id       = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)

    # Auction fields
    group          = Column(Enum(AuctionGroup), nullable=False)
    sold_price     = Column(Integer, nullable=True)   # Null if unsold
    auction_status = Column(Enum(AuctionStatus), nullable=False, default=AuctionStatus.pending)

    # Relationships
    tournament   = relationship("Tournament", back_populates="tournament_players")
    player       = relationship("Player", back_populates="tournament_entries")
    team         = relationship("Team", back_populates="tournament_players")
    auction_bids = relationship("AuctionBid", back_populates="tournament_player")


# ---------------------------------------------------------------------------
# Auction event log
# ---------------------------------------------------------------------------

class AuctionBid(Base):
    """
    Every individual bid increment placed during the auction.
    Linked to tournament_player (not player directly) — a bid only
    makes sense in the context of a specific tournament slot.
    Full history is preserved for audit and replay.
    """
    __tablename__ = "auction_bids"

    id                   = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_player_id = Column(UUID(as_uuid=True), ForeignKey("tournament_players.id"), nullable=False)
    team_id              = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    amount               = Column(Integer, nullable=False)
    bid_at               = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    tournament_player = relationship("TournamentPlayer", back_populates="auction_bids")
    team              = relationship("Team", back_populates="auction_bids")


# ---------------------------------------------------------------------------
# Match layer
# ---------------------------------------------------------------------------

class Match(Base):
    """
    A fixture between two teams within a tournament.
    Stores the result summary written once when the match completes.
    overs_faced columns are needed for NRR computation in standings.
    Live state (who is batting/bowling) lives in MatchState.
    """
    __tablename__ = "matches"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tournament_id = Column(UUID(as_uuid=True), ForeignKey("tournaments.id"), nullable=False)
    team_a_id     = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    team_b_id     = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)

    # Toss — nullable until toss is done
    toss_winner_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)
    toss_decision  = Column(Enum(TossDecision), nullable=True)

    status         = Column(Enum(MatchStatus), nullable=False, default=MatchStatus.scheduled)

    # Result — nullable until match completes
    winning_team_id  = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=True)
    team_a_score     = Column(Integer, nullable=True)
    team_a_wickets   = Column(Integer, nullable=True)
    team_a_overs_faced = Column(Numeric(4, 1), nullable=True)  # e.g. 18.4
    team_b_score     = Column(Integer, nullable=True)
    team_b_wickets   = Column(Integer, nullable=True)
    team_b_overs_faced = Column(Numeric(4, 1), nullable=True)
    result_summary   = Column(String(200), nullable=True)  # e.g. "Team A won by 24 runs"

    scheduled_at  = Column(DateTime, nullable=True)
    completed_at  = Column(DateTime, nullable=True)

    # Relationships
    tournament   = relationship("Tournament", back_populates="matches")
    team_a       = relationship("Team", foreign_keys=[team_a_id])
    team_b       = relationship("Team", foreign_keys=[team_b_id])
    toss_winner  = relationship("Team", foreign_keys=[toss_winner_id])
    winning_team = relationship("Team", foreign_keys=[winning_team_id])
    innings      = relationship("Innings", back_populates="match", order_by="Innings.innings_number")
    match_state  = relationship("MatchState", back_populates="match", uselist=False)


class Innings(Base):
    """
    One half of a match — either team's batting turn.
    Bridges Match and Deliveries. Two rows per match (innings 1 and 2).
    """
    __tablename__ = "innings"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    match_id       = Column(UUID(as_uuid=True), ForeignKey("matches.id"), nullable=False)
    batting_team_id  = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    bowling_team_id  = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    innings_number = Column(Integer, nullable=False)   # 1 or 2
    status         = Column(Enum(InningsStatus), nullable=False, default=InningsStatus.pending)

    # Relationships
    match        = relationship("Match", back_populates="innings")
    batting_team = relationship("Team", foreign_keys=[batting_team_id])
    bowling_team = relationship("Team", foreign_keys=[bowling_team_id])
    deliveries   = relationship("Delivery", back_populates="innings",
                                order_by="[Delivery.over_number, Delivery.ball_number]")
    match_state  = relationship("MatchState", back_populates="innings")


class Delivery(Base):
    """
    A single ball bowled. The source of truth for all stats.

    over_number and ball_number are stored as separate integers —
    no string encoding like "14.2". This makes undo trivial:
      DELETE ... ORDER BY over_number DESC, ball_number DESC LIMIT 1

    Wides and no-balls do NOT increment ball_number (they are re-bowled),
    so ball_number reflects legal deliveries only within an over.

    All player stats (runs, wickets, economy, strike rate, Orange Cap,
    Purple Cap, career figures) are computed by aggregating this table.
    Nothing is cached elsewhere.
    """
    __tablename__ = "deliveries"

    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    innings_id  = Column(UUID(as_uuid=True), ForeignKey("innings.id"), nullable=False)
    bowler_id   = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=False)
    batter_id   = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=False)

    over_number  = Column(Integer, nullable=False)   # 0-indexed: over 1 = 0, over 2 = 1 ...
    ball_number  = Column(Integer, nullable=False)   # 1–6 for legal deliveries

    runs_off_bat = Column(Integer, nullable=False, default=0)
    extras       = Column(Integer, nullable=False, default=0)
    extra_type   = Column(Enum(ExtraType), nullable=False, default=ExtraType.none)

    is_wicket          = Column(Boolean, nullable=False, default=False)
    wicket_type        = Column(Enum(WicketType), nullable=True)
    dismissed_player_id = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=True)

    created_at   = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationships
    innings          = relationship("Innings", back_populates="deliveries")
    bowler           = relationship("Player", foreign_keys=[bowler_id], back_populates="deliveries_as_bowler")
    batter           = relationship("Player", foreign_keys=[batter_id], back_populates="deliveries_as_batter")
    dismissed_player = relationship("Player", foreign_keys=[dismissed_player_id], back_populates="dismissals")


class MatchState(Base):
    """
    Volatile live state for an active match.
    One row per match — overwritten on every ball by the scorer.
    Drives the live scoreboard: who is batting, who is bowling.
    Can be deleted when the match completes (or left as a snapshot).

    This is NOT a permanent record — all historical truth lives in Delivery.
    """
    __tablename__ = "match_state"

    id                = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    match_id          = Column(UUID(as_uuid=True), ForeignKey("matches.id"), nullable=False, unique=True)
    innings_id        = Column(UUID(as_uuid=True), ForeignKey("innings.id"), nullable=False)

    striker_id        = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=True)
    non_striker_id    = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=True)
    current_bowler_id = Column(UUID(as_uuid=True), ForeignKey("players.id"), nullable=True)

    updated_at        = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    match       = relationship("Match", back_populates="match_state")
    innings     = relationship("Innings", back_populates="match_state")
    striker     = relationship("Player", foreign_keys=[striker_id])
    non_striker = relationship("Player", foreign_keys=[non_striker_id])
    bowler      = relationship("Player", foreign_keys=[current_bowler_id])