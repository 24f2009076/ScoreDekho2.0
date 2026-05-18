<template>
    <div class="body">
        <RouterLink class="tab">
            <img src="/icons/home.png" alt="" class="tab-icon">
            <div class="tab-label">Dashboard</div>
        </RouterLink>
        <RouterLink class="tab">
            <img src="/icons/dashboard_sidebar_match.png" alt="" class="tab-icon">
            <div class="tab-label">Match</div>
        </RouterLink>
        <RouterLink class="tab">
            <img src="/icons/dashboard_sidebar_tournament.png" alt="" class="tab-icon">
            <div class="tab-label">Tournaments</div>
        </RouterLink>
        <RouterLink class="tab">
            <img src="/icons/team.png" alt="" class="tab-icon">
            <div class="tab-label">Players</div>
        </RouterLink>
        <RouterLink class="tab">
            <img src="/icons/user.png" alt="" class="tab-icon">
            <div class="tab-label">Profile</div>
        </RouterLink>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
    const body = document.querySelector('.body');
    const labels = document.querySelectorAll('.tab-label');
    const tabs = document.querySelectorAll('.tab');
    body.addEventListener('mouseover', () => {
        labels.forEach(label => label.style.display = 'block');
        labels.forEach(label => label.style.opacity = '1');
        // tabs.forEach(tab => tab.style.justifyContent = 'flex-start');
    });
    body.addEventListener('mouseout', () => {
        labels.forEach(label => label.style.display = 'none');
        labels.forEach(label => label.style.opacity = '0.5');
        // tabs.forEach(tab => tab.style.justifyContent = 'center');
    });
});


</script>

<style scoped>

.body {
    min-height: 100%;
    width: 4.5rem;

    display: flex;
    flex-direction: column;
    padding: 1.5rem 0;

    border-right: 1px solid #40E436;
    transition: width 0.3s ease;
}

.body:hover {
    width: 15rem;
}

.body .tab{
    height: 3rem;
    width: 100%;
    margin-bottom: 1rem;

    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 1.3rem 1rem;
    transition: all 0.3s ease-in-out;
    border-radius: 0.5rem;
    text-decoration: none;

    /* border: 2px solid blue; */
}

.body .tab:hover {
    background-color: #1e3b1d;
    cursor: pointer;
}

.body .tab .tab-icon {
    height: 2rem;
    aspect-ratio: 1;
    /* transition: all 0.5s ease-in-out; */
}

.tab-label {
    margin-left: 1rem;
    font-size: 1.2rem;
    font-weight: 500;
    color: #dae2ff;
    transition: opacity 0.7s ease-in-out;
    display: none;
    opacity: 0.5;
}



</style>