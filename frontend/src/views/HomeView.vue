<template>
    <div class="body">
        <div class="hero-section reveal">
            <div class="hero-glow"></div>
            <div class="hero-text">
                Proffesionalize Your <span class="lime">Local Tournament</span>
            </div>
            <div class="sub-hero-text">
                Elevate your league with professional-grade scoring, real-time analytics, and seamless management tools designed for the modern game.
            </div>
            <div class="btn-panel">
                <RouterLink to="/" class="btn get-started">Get Started</RouterLink>
                <RouterLink to="/" class="btn live-tournaments">Live Tournaments</RouterLink>
            </div>
        </div>

        <div class="features">
            <div class="features__header">
                <h2 class="features__title">Unmatched Feature Set</h2>
                <p class="features__subtitle">
                    Precision tools for every phase of your tournament lifecycle, from the first auction to the final ball.
                </p>
            </div>

            <div class="feature-grid reveal">
                <article class="feature-card feature-card--large">
                    <div class="feature-card__body">
                        <div class="feature-card__icon">
                             <img src="/icons/cricket.png" alt="Live scoring icon" class="cricket-icon"/>
                        </div>
                        <h3 class="feature-card__title">Live Ball-by-Ball Scoring</h3>
                        <p class="feature-card__text">
                            Real-time updates that keep fans engaged. Our interface is optimized for speed and accuracy,
                            ensuring every run and wicket is recorded instantly.
                        </p>
                    </div>

                    <div class="feature-card__media feature-card__media--score"></div>
                </article>

                <article class="feature-card feature-card--small">
                    <div class="feature-card__body">
                        <div class="feature-card__icon">
                            <img src="/icons/action.png" alt="Player auctions icon" class="action-icon"/>
                        </div>
                        <h3 class="feature-card__title">Pro-Style Player Auctions</h3>
                        <p class="feature-card__text">
                            Transform team selection into a high-stakes event with real-time bidding, wallet tracking,
                            and player scouting reports.
                        </p>
                    </div>
                </article>

                <article class="feature-card feature-card--wide">
                    <div class="feature-card__body feature-card__body--wide">
                        <div>
                            <div class="feature-card__icon">
                                <img src="/icons/stats.png" alt="Player stats icon" class="stats-icon"/>
                            </div>
                            <h3 class="feature-card__title">Comprehensive Stats</h3>
                            <p class="feature-card__text">
                                Deep-dive into player performance. From wagon wheels to strike rate trends, get the
                                professional analytics your players deserve.
                            </p>

                            <div class="feature-stats">
                                <div class="feature-stat">
                                    <span class="feature-stat__value">50+</span>
                                    <span class="feature-stat__label">Metrics</span>
                                </div>
                                <div class="feature-stat">
                                    <span class="feature-stat__value">Real-time</span>
                                    <span class="feature-stat__label">Analytics</span>
                                </div>
                            </div>
                        </div>

                        <div class="feature-card__media feature-card__media--stats"></div>
                    </div>
                </article>
            </div>
        </div>

        <div class="contact-section reveal">

            <div class="card">
                <div class="card-heading">Build for <span class="lime">Boundary Line</span></div>
                <div class="card-text">
                    Join over 5+ tournament organizers who have scaled their events with ScoreDekho's technical precision. 
                </div>
                <div class="btn-panel">
                    <RouterLink to="/" class="btn get-started">Get Started</RouterLink>
                    <RouterLink to="/" class="btn live-tournaments">Live Tournaments</RouterLink>
                </div>
            </div>

        </div>

    </div>


</template>

<script setup>

import { onMounted, onBeforeUnmount } from 'vue'

onMounted(() => {
  const sections = document.querySelectorAll('.reveal')

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.15 }
  )

  sections.forEach(section => observer.observe(section))
})



</script>

<style scoped>

    .body {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: start;
        width: 100%;
        background: black;
        /* border: 2px solid blue; */
    }
     
    /* -------------------------------------- Hero Section Styles -------------------------------------- */
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1rem;

        min-height: 80vh;
        width: 100%;
        padding: 3rem 1rem;

        background: radial-gradient(circle at top, rgba(30, 30, 30, 0.4) 0%, rgba(10, 13, 18, 1) 100%);
        /* border: 2px solid red; */
    }

    .hero-glow {
        position: absolute;

        top: -20%;
        left: 50%;
        transform: translateX(-50%);

        width: 900px;
        height: 900px;

        border-radius: 50%;

        background: radial-gradient(
            circle,
            rgba(64, 228, 54, 0.35) 0%,
            rgba(64, 228, 54, 0.12) 30%,
            rgba(64, 228, 54, 0.03) 55%,
            transparent 75%
        );

        filter: blur(120px);

        pointer-events: none;
    }

    .hero-text {
        font-size: clamp(1.75rem, 5vw, 5rem);
        color: #dae2ff;
        text-align: center;
        font-family: 'Plus Jakarta Sans';
        width: min(90%, 60rem);

        /* border: 2px solid lime; */
    }

    .lime {
        color: #40e436;
    }

    .sub-hero-text {
        font-size: clamp(1rem, 2.2vw, 1.25rem);
        color: #7c808e;
        text-align: center;
        font-family: 'Plus Jakarta Sans';
        width: min(90%, 50rem);
    }

    .btn-panel {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
        justify-content: center;
    }

    .btn {
        padding: 0.65rem 1.25rem;
        font-size: clamp(1rem, 2.5vw, 1.25rem);
        font-weight: 500;
        border-radius: 4px;
        text-decoration: none;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .btn.live-tournaments {
        background-color: transparent;
        color: #40e436;
        border: 2px solid #40e436;
        position: relative;
        overflow: hidden;
        z-index: 0;
        transition: width 0.3s ease, color 0.3s ease;
    }

    .btn.live-tournaments::after {
        content: '';
        position: absolute;
        top: 100%;
        left: -10%;
        width: 0%;
        aspect-ratio: 0.5;
        background: #40e436;
        transform: translate(0%, -50%);
        border-radius: 50%;
        transition: width 0.7s ease, color 0.2s ease;
        z-index: -1;
    }

    .btn.live-tournaments:hover::after {
        width: 220%;
    }

    .btn.live-tournaments:hover {
        color: #0a0d12;
    }

    .btn.get-started {
        background-color: #40e436;
        color: #0a0d12;
    }

    .btn.get-started:hover {
        background-color: #32c92e;
    }

    /* -------------------------------------- Features Section Styles -------------------------------------- */
    .features {
        width: min(100%, 80rem);
        padding: 6rem 1.5rem 7rem;
    }

    .features__header {
        margin-bottom: 1.5rem;
    }

    .features__title {
        margin: 0 0 0.5rem;
        color: #f5f5f5;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: clamp(2rem, 4vw, 3.25rem);
        line-height: 1.1;
        letter-spacing: -0.04em;
    }

    .features__subtitle {
        max-width: 42rem;
        margin: 0;
        color: #a0a0a0;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1rem;
        line-height: 1.6;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(12, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }

    .feature-card {
        display: flex;
        flex-direction: column;
        gap: 1.25rem;
        padding: 1.5rem;
        border-radius: 0.75rem;
        background: rgba(34, 34, 34, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        transition: border-color 0.2s ease, transform 0.2s ease, background-color 0.2s ease;
    }

    .feature-card:hover {
        border-color: rgba(64, 228, 54, 0.3);
        transform: translateY(-2px);
    }

    .feature-card--large {
        grid-column: span 8;
    }

    .feature-card--small {
        grid-column: span 4;
        justify-content: space-between;
        min-height: 100%;
    }

    .feature-card--wide {
        grid-column: span 12;
    }

    .feature-card__body {
        max-width: 30rem;
    }

    .feature-card__body--wide {
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(18rem, 34rem);
        gap: 1.5rem;
        align-items: center;
        max-width: none;
    }

    .feature-card__icon {
        width: 3rem;
        height: 3rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        border-radius: 0.75rem;
        background: rgba(64, 228, 54, 0.1);
        color: #40e436;
        font-family: 'Material Symbols Outlined', sans-serif;
        font-size: 1.4rem;
        line-height: 1;
    }

    .feature-card__title {
        margin: 0 0 0.85rem;
        color: #f5f5f5;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: clamp(1.4rem, 2vw, 2rem);
        line-height: 1.2;
        letter-spacing: -0.03em;
    }

    .feature-card__text {
        margin: 0;
        color: #a0a0a0;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1rem;
        line-height: 1.7;
    }

    .feature-card__media {
        border-radius: 0.75rem;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
        background: #0f1012;
        min-height: 16rem;
    }

    .feature-card__media--score {
        background:
            radial-gradient(circle at 30% 30%, rgba(64, 228, 54, 0.22), transparent 35%),
            linear-gradient(135deg, rgba(18, 18, 18, 0.95), rgba(9, 12, 17, 0.95)),
            linear-gradient(120deg, rgba(64, 228, 54, 0.08), transparent 45%);
    }

    .feature-card__media--stats {
        min-height: 18rem;
        background:
            radial-gradient(circle at 25% 25%, rgba(64, 228, 54, 0.24), transparent 28%),
            radial-gradient(circle at 65% 35%, rgba(64, 228, 54, 0.12), transparent 22%),
            linear-gradient(135deg, rgba(12, 13, 16, 0.98), rgba(24, 24, 24, 0.95));
    }

    .feature-stats {
        display: flex;
        gap: 2rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
    }

    .feature-stat {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }

    .feature-stat__value {
        color: #40e436;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 2rem;
        font-weight: 700;
    }

    .feature-stat__label {
        color: #8b919f;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .cricket-icon {
        width: 100%;
        height: 100%;
        object-fit: contain;
        padding: 0.35rem;
    }

    .action-icon {
        width: 100%;
        height: 100%;
        padding: 0.15rem;
        object-fit: contain;
    }

    .stats-icon {
        width: 100%;
        height: 100%;
        padding: 0.25rem;
        object-fit: contain;
    }

    .contact-section {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4rem 1.5rem;
         /* border: 2px solid red; */
        position: relative;
        width: 100%;
        padding: 3rem 9rem;
    }

    .card {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
        padding: 5rem;
        border-radius: 0.75rem;
        background: rgba(34, 34, 34, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        width: 100%;
         /* border: 2px solid red; */
    }

    .card-heading {
        margin: 0;
        color: #f5f5f5;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: clamp(1.75rem, 3vw, 2.5rem);
        line-height: 1.1;
        letter-spacing: -0.04em;
    }

    .card-text {
        max-width: 32rem;
        margin: 0;
        color: #a0a0a0;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.125rem;
        line-height: 1.6;
        text-align: center;
    }

    .reveal {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .reveal.is-visible {
        opacity: 1;
        transform: translateY(0);
    }

    @media (max-width: 900px) {
        .feature-card--large,
        .feature-card--small,
        .feature-card--wide {
            grid-column: span 12;
        }

        .feature-card__body--wide {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 640px) {
        .features {
            padding-inline: 1rem;
        }

        .feature-card {
            padding: 1.25rem;
        }

        .feature-stats {
            gap: 1rem;
        }

        
        .hero-section { padding-top: 2.25rem; padding-bottom: 2.25rem; }
        .hero-text { font-size: 2rem; }
        .sub-hero-text { font-size: 0.95rem; }
        .btn { padding: 0.6rem 1rem; }
        .feature-card__media { min-height: 10rem; }
        .contact-section { padding: 3rem 1rem; margin-top: -5rem; }
        .card { padding: 2rem; }
    }
</style>