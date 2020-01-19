<script>
	import Score from './Score.svelte';
	import {apiUrl} from '../../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';

	export let game;
	export let players;

	const dispatch = createEventDispatcher();

	let apiUrlStore;
	let scores;
	let fullPlayers;
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

	function init() {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

		onDestroy(() => {
			unsubscribeApiUrl();
		});

		fetch(`${apiUrlStore}game/${game.id}/score`, {
			method: 'POST',
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

	function returnHome() {
		dispatch('returnHome');
	}

	function nextQuestion() {
		dispatch('nextQuestion');
	}
</script>

<div class="uk-grid uk-margin" uk-grid="">
	<div class="uk-width-expand">
		<h1>
			Scoreboard
		</h1>
	</div>
	<div class="uk-width-auto">
		<button class="uk-button uk-button-default uk-border-rounded" on:click={returnHome}>Cancel and return home
		</button>
		<button class="uk-button uk-button-primary uk-border-rounded" on:click={nextQuestion}>Next question</button>
	</div>
</div>

{#each fullPlayers as player, i}
	<Score color={player.color} score={player.score} position={i+1}/>
    {#if fullPlayers.length > i+1 && i+1 > 2}
		<hr class="uk-margin-small">
    {/if}
{:else}
	<div class="uk-card uk-card-default uk-card-small uk-border-rounded">
		<div uk-spinner="ratio: 3"></div>
		Fetching quizzes
	</div>
{/each}