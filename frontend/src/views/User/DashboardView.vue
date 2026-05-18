<template>
    <div class="dashboard">
        <div class="sidebar-container">
            <SideBar class="sidebar"/>
        </div>
        <div class="content">
            <div class="head">Hi! {{ full_name }}</div>
            <div class="cards">

                <div class="small-card">
                    <div class="big"> 10 </div>
                    <div class="small"> ACTIVE TOURNAMENTS </div>
                </div>

                <div class="small-card">
                    <div class="big"> 5 </div>
                    <div class="small"> PLAYERS </div>
                </div>

                <div class="small-card">
                    <div class="big"> 5 </div>
                    <div class="small"> LIVE MATCHES </div>
                </div>

                <div class="small-card">
                    <div class="big"> 5 </div>
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

const authStore = useAuthStore()
const full_name = authStore.full_name.split(' ')[0] || 'User'



</script>

<style scoped>

    .dashboard {
        display: flex;
        width: 100%;
        height: 100%;
        gap: 0;
        /* border: 2px solid red; */
    }

    .sidebar-container {
        width: 5rem;
        height: 100%;
        /* border: 2px solid blue; */
    }

    .sidebar {
        position: fixed;
        z-index: 999;
        background-color: black;
        /* border: 2px solid red; */
    }

    .content {
        flex: 1;
        padding: 20px;
        display: flex;
        flex-direction: column;
        border-radius: 14px;
        padding: 24px;
        height: 100%;
        /* background: linear-gradient(180deg, rgba(8, 98, 9, 0.12), rgba(8, 98, 9, 0.04)); */
        /* border: 1px solid rgba(8, 98, 9, 0.25); */
        /* box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); */
        /* border: 2px solid lime; */
        gap: 2rem;
    }

    .head {
        font-size: 1.8rem;
        font-weight: 600;
        color: #b9e2a7;
        /* border: 1px dashed lime; */
    }

    /* ----------- CARDS ----------- */
    .cards {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
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
        font-size: 5rem;
        font-weight: 700;
        line-height: 1;
        color: #ffffff;
        width: 100%;
        /* text-align: center; */
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

    @media (max-width: 650px) {
        .cards {
            display: none;
        }
    }



</style>