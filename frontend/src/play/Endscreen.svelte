<script>
    import Score from "./quizzing/Score.svelte";
    import {apiUrl} from '../stores.js';
    import {onDestroy, createEventDispatcher} from 'svelte';

    export let game;
    export let players;


    let apiUrlStore;
    let scores;
    let fullPlayers;

    const dispatch = createEventDispatcher();

    // Creates a new players array that includes their id, color, and score.
    $: {
        fullPlayers = players.map(player => {
            if (scores !== undefined) {
                player.score = scores[player.id];
            }
            return player;
        });
        fullPlayers.sort((a, b) => {
            if (a.score > b.score) {
                return -1;
            } else if (a.score < b.score) {
                return 1;
            } else {
                return 0;
            }
        });
    }
    let state = {
        scores: {
            attempted: false,
            successful: false
        }
    };

    init();

    /**
     * Gathers the score Data needed.
     *
     * - Subscribes to stores
     * - Gets the game scores
     */
    function init() {
        const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

        onDestroy(() => {
            unsubscribeApiUrl();
        });

        fetch(`${apiUrlStore}game/${game.id}/score`, {
            method: 'GET',
            mode: 'cors'
        }).then(res => {
            state.scores.attempted = true;
            state.scores.successful = true;
            return res.json();
        }).then(data => {
            return scores = data;
        }).catch(_ => {
            state.scores.attempted = true;
        });
    }

    function handleReturnHome() {
        dispatch('returnHome', {
            target: 'home',
            navbar: true,
            container: true,
            title: true,
            subtitle: true,
            divider: true,
            text: true
        });
    }
</script>



<div class="uk-position-top-center uk-margin-large-top" style="width: 30%">
    <h1>Final Score</h1>
    <h2>Top 3 Pihooters</h2>
        {#each fullPlayers as player, i}
            {#if i <= 2}
                <Score color={player.color} score={player.score} position={i+1}/>
            {/if}
        {/each}
    <br>
        {#if fullPlayers.length > 3}
            <h3>The others</h3>
            {#each fullPlayers as player, i}
                {#if i >= 3}
                    <Score color={player.color} score={player.score} position={i+1}/>
                {/if}
            {/each}
        {/if}
</div>

<div class="uk-position-bottom-right uk-margin-large-bottom uk-margin-large-right">
    <button class="uk-button uk-button-default" on:click={handleReturnHome}>Home</button>
</div>