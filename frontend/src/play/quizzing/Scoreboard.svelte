<script>
	import Score from './Score.svelte';
	import {apiUrl} from '../../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';

	/**
	 * File description:
	 * Provides a component that displays a scoreboard.
	 */

	export let gameId;
	export let players;
	export let finalScoreboard = false;

	const dispatch = createEventDispatcher();

	let apiUrlStore;
	let scores;
	let fullPlayers;
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
	 * Initiates every needed resource for proper functioning of the page.
	 *
	 * - Subscribes to stores
	 * - Gets the game scores
	 */
	function init() {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

		onDestroy(() => {
			unsubscribeApiUrl();
		});

		fetch(`${apiUrlStore}game/${gameId}/score`, {
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

	/**
	 * Passes on a returnHome event to its parent component.
	 *
	 * @fires returnHome
	 */
	function returnHome() {
		dispatch('returnHome');
	}

	/**
	 * Passes on a nextQuestion event to its parent component.
	 *
	 * @fires nextQuestion
	 */
	function nextQuestion() {
		dispatch('nextQuestion');
	}
</script>

<div class="uk-grid uk-margin" uk-grid="">
	<div class="uk-width-expand">
		<h1>
            {#if finalScoreboard}
				Leaderboard
            {:else}
				Scoreboard
            {/if}
		</h1>
	</div>
	<div class="uk-width-auto">
		<button class="uk-button uk-button-{finalScoreboard ? 'primary' : 'default'} uk-border-rounded" on:click={returnHome}>
            {#if finalScoreboard}
				Return home
            {:else}
				Cancel and return home
            {/if}
		</button>
        {#if !finalScoreboard}
			<button class="uk-button uk-button-primary uk-border-rounded" on:click={nextQuestion}>Next question</button>
        {/if}
	</div>
</div>

{#each fullPlayers as player, i}
    {#if finalScoreboard}
		<Score color={i === 0 ? 'GOLD' : i === 1 ? 'SILVER' : i === 2 ? 'BRONZE' : player.color} colorName={player.color} score={player.score} position={i+1}/>
    {:else}
		<Score color={player.color} colorName={player.color} score={player.score} position={i+1}/>
    {/if}
    {#if fullPlayers.length > i+1 && i+1 > 2}
		<hr class="uk-margin-small">
    {/if}
{:else}
	<div class="uk-card uk-card-default uk-card-small uk-border-rounded">
		<div uk-spinner="ratio: 3"></div>
		Fetching scores
	</div>
{/each}