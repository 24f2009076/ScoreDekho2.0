<template>
    <div class="dashboard">
        <div class="sidebar-container">
            <SideBar class="sidebar"/>
        </div>
        <div class="content">
            <div class="head">Hi! {{ full_name }}</div>
            <div class="cards">

                <div class="small-card">
                    <div class="big"> {{ active_torunament_count }} </div>
                    <div class="small"> ACTIVE TOURNAMENTS </div>
                </div>

                <div class="small-card">
                    <div class="big"> {{ players_count }} </div>
                    <div class="small"> PLAYERS </div>
                </div>

                <div class="small-card">
                    <div class="big"> {{ live_matches_count }} </div>
                    <div class="small"> LIVE MATCHES </div>
                </div>

                <div class="small-card">
                    <div class="big"> {{ upcoming_tournament_count }} </div>
                    <div class="small"> UPCOMING TOURNAMENTS </div>
                </div>

            </div>

            <div class="active-tournament-section">
                <div class="section-head"> ACTIVE TOURNAMENTS </div>

                <RouterLink to="/" class="tournament-list">

                    <div class="tournament-item">
                        
                        <div class="item-head"> KMDA Premier League </div>

                        <table class="item-teams">
                            <tr class="item-teams-head-row">
                                <td class="head-cell"> Srl No. </td>
                                <td class="head-cell"> Team </td>
                                <td class="head-cell"> P </td>
                                <td class="head-cell"> W </td>
                                <td class="head-cell"> L </td>
                                <td class="head-cell"> PTS </td>
                                <td class="head-cell"> NRR </td>
                            </tr>
                            <tr class="teams-item">
                                <td class="item-cell"> 1 </td>
                                <td class="item-cell"> KMDA Blasters </td>
                                <td class="item-cell"> 5 </td>
                                <td class="item-cell"> 4 </td>
                                <td class="item-cell"> 1 </td>
                                <td class="item-cell"> 8 </td>
                                <td class="item-cell"> +2.5 </td>
                            </tr>
                            <tr class="teams-item">
                                <td class="item-cell"> 2 </td>
                                <td class="item-cell"> KMDA Mavericks </td>
                                <td class="item-cell"> 5 </td>
                                <td class="item-cell"> 3 </td>
                                <td class="item-cell"> 2 </td>
                                <td class="item-cell"> 6 </td>
                                <td class="item-cell"> +0.14 </td>
                            </tr>
                            <tr class="teams-item">
                                <td class="item-cell"> 3 </td>
                                <td class="item-cell"> KMDA Warriors </td>
                                <td class="item-cell"> 4 </td>
                                <td class="item-cell"> 2 </td>
                                <td class="item-cell"> 2 </td>
                                <td class="item-cell"> 4 </td>
                                <td class="item-cell"> -0.15 </td>
                            </tr>
                            <tr class="teams-item">
                                <td class="item-cell"> 4 </td>
                                <td class="item-cell"> KMDA Strickers </td>
                                <td class="item-cell"> 4 </td>
                                <td class="item-cell"> 1 </td>
                                <td class="item-cell"> 3 </td>
                                <td class="item-cell"> 2 </td>
                                <td class="item-cell"> -1.30 </td>
                            </tr>

                        </table>
                    </div>
                </RouterLink>
            </div>
            
        </div>
    </div>
</template>

<script setup>
import SideBar from '@/components/SideBar.vue'
import { useAuthStore } from '@/stores/auth'
import { onMounted, ref } from 'vue'

const authStore = useAuthStore()
const full_name = authStore.full_name.split(' ')[0] || 'User'

const active_torunament_count = ref(-1);
const upcoming_tournament_count = ref(-1);
const live_matches_count = ref(-1);
const players_count = ref(-1);

async function fetchTournamentData() {
    try {
        const response = await fetch('http://localhost:8000/api/tournaments/', 
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authStore.token}`
                }
            }
        );
        const data = await response.json();
        // console.log(data);
        active_torunament_count.value = data.active_count;
        upcoming_tournament_count.value = data.upcoming_count;
    } catch (error) {
        console.error('Error fetching tournament data:', error);
    }
}

async function fetchMatchdata() {
    try {
        const response = await fetch('http://localhost:8000/api/matches/live',
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'applications/json',
                    'Authorization': `Bearer ${authStore.token}`
                }
            }
        )

        const data = await response.json();
        live_matches_count.value = data.count;

    } catch (error) {
        console.error('Error fetching match data:', error);
    }
}

async function fetchPlayerData() {
    try {
        const response = await fetch('http://localhost:8000/api/players/',
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'applications/json',
                    'Authorization': `Bearer ${authStore.token}`
                }
            }
        )

        const data = await response.json();
        players_count.value = data.count;

    } catch (error) {
        console.error('Error fetching player data:', error);
    }
}



async function refresh() {
    await fetchTournamentData();
    await fetchPlayerData();
    await fetchMatchdata();
}

onMounted(() => {
    refresh();
})


</script>

<style scoped>

    .dashboard {
        display: flex;
        width: 100%;
        max-height: 100%;
        gap: 0;
        /* overflow-y: hidden; */
        /* border: 2px solid red; */
    }

    .sidebar-container {
        width: 5rem;
        position: sticky;
        left: 0;
        top: 0;
        background-color: black;
        z-index: 10;
        /* height: 100vh; */
        /* border: 2px solid blue; */
    }

    .sidebar {
        height: 100%;
        position: sticky;
        left: 0;
        top: 0;
        z-index: 999;
        background-color: black;
        /* border: 2px solid red; */
    }

    .content {
        flex: 1;
        padding: 2rem;
        display: flex;
        flex-direction: column;
        border-radius: 14px;
        height: 100%;
        /* background: linear-gradient(180deg, rgba(8, 98, 9, 0.12), rgba(8, 98, 9, 0.04)); */
        /* border: 1px solid rgba(8, 98, 9, 0.25); */
        /* box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); */
        /* border: 2px solid lime; */
        gap: 2rem;
        /* account for the fixed sidebar so content doesn't sit under it */
        /* margin-left: rem; */
    }

    .head {
        font-size: clamp(1.2rem, 2.5vw, 1.8rem);
        font-weight: 600;
        color: #b9e2a7;
    }

    /* ----------- CARDS ----------- */
    .cards {
        width: 100%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 1rem;
    }
    
    .small-card {
        /* background-color: #086209; */
        border-radius: 8px;
        padding-left: 3.5rem;
        color: #b9e2a7;
        background: linear-gradient(180deg, rgba(8, 98, 9, 0.12), rgba(8, 98, 9, 0.04));
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        border: 2.5px solid rgba(8, 98, 9, 0.25);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        aspect-ratio: 3/2;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }

    .small-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.16);
        border-color: rgba(8, 98, 9, 0.4);
    }

    .big {
        font-size: clamp(2rem, 6vw, 5rem);
        font-weight: 700;
        line-height: 1;
        color: #ffffff;
        width: 100%;
    }

    .small {
        margin-top: 0.75rem;
        font-size: 0.98rem;
        font-weight: 500;
        letter-spacing: 0.02em;
        color: rgba(232, 245, 233, 0.82);
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        /* border: 1px dashed lime; */
    }
    /* ----------- ACTIVE TOURNAMENTS ----------- */

    .active-tournament-section {
        padding: 1rem;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: start;
        /* border: 2px solid red; */
    }

    .section-head {
        font-size: 1rem;
        font-weight: 600;
        color: #b9e2a7;
        /* margin-bottom: 1rem; */
        position: relative;
        /* background-color: black; */
        /* z-index: 3; */
        /* border: 2px solid blue; */
    }

    .section-head::before {
        background-color: #40e436;
        content: '';
        position: absolute;
        bottom: 50%;
        left: 108%;
        width: 60vw;
        height: 1px;
    }

    .tournament-list {
        margin-top: 1rem;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        background: linear-gradient(180deg, rgba(8, 98, 9, 0.12), rgba(8, 98, 9, 0.04));
        border: 2.5px solid rgba(8, 98, 9, 0.25);
        border-radius: 8px;
        padding: 1rem 2rem;

        /* border: 2px solid red; */
        color: white;
        transition: transform 0.2s ease, border-color 0.2s ease;
        cursor: pointer;
        text-decoration: none;
        /* allow horizontal scrolling for wide tables on small screens */
        overflow-x: auto;
    }

    .tournament-list:hover {
        /* scale: 1.01; */
        transform: translateY(-2px);
        border-color: rgba(8, 98, 9, 0.4);
    }

    .item-head {
        font-size: 1.25rem;
        font-weight: 600;
        color: #b9e2a7;
        /* border: 2px solid red; */
    }

    .item-teams {
        width: 100%;
        border-collapse: collapse;
        margin-top: 0.75rem;
        padding: 0.5rem;
        /* border: 2px dashed lime; */
    }

    /* ensure table content can scroll on narrow viewports */
    @media (max-width: 900px) {
        .content { margin-left: 3.5rem; }
        .sidebar-container { width: 3.5rem; }
        .sidebar { left: 0; }
    }

    @media (max-width: 650px) {
        .content { margin-left: 0; padding: 16px; }
        .sidebar { position: relative; width: 100%; height: auto; z-index: 2; }
        /* .sidebar-container { display: none; } */
        .tournament-list { padding: 0.75rem; }
        .item-teams { display: block; overflow-x: auto; }
    }
    
    .item-teams-head-row {
        /* background-color: rgba(8, 98, 9, 0.25); */
        color: #b9e2a7;
        border-bottom: 2px solid rgba(8, 98, 9, 0.5);
        /* border: 2px solid red; */
    }

    .head-cell {
        padding: 0.5rem;
        font-size: 1rem;
        font-weight: 500;
        text-align: left;
    }

    .teams-item:nth-child(even) {
        background-color: rgba(8, 98, 9, 0.12);
    }

    .item-cell {
        padding: 0.5rem;
        font-size: 0.95rem;
        font-weight: 400;
        text-align: left;
    }

    @media (max-width: 1000px) {
        .content {
            padding: 0;
        }

        .section-head::before {
            display: none;
        }

        .small-card {
            aspect-ratio: 1/1;
            justify-content: center;
            padding: 1rem;

        }

        .big {
            font-size: 2.5rem;
            justify-content: center;
        }

        .small {
            font-size: 0.5rem;
            text-align: center;
            /* border: 1px dashed lime; */
        }

    }

    @media (max-width: 700px) {
        .cards {
            display: none;
        }
        .dashboard {
            overflow: scroll;
        }
    }



</style>