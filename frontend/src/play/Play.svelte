<script>
	import {apiUrl, animationConfig} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';
	import {passByVal} from '../util.js'
	import LoadingGame from './PreGame.svelte';
	import PlayersJoin from './PlayersJoin.svelte';

	export let data;
	const dispatch = createEventDispatcher();

	let quiz = data.quiz;
	let game;
	let players = [];
	let apiUrlStore;
	let animationConf;
	let connectionStatus = {
		createGame: {
			attempted: false,
			successful: false
		},
		ws: {
			attempted: false,
			successful: false,
			subscriptionOpen: false
		}
	};

	init();

	function handlePageUpdate(e) {
		dispatch('pageUpdate', e.detail);
	}

	function handleVisibilityUpdate(e) {
		dispatch('visibilityChange', e.detail);
	}

	function handleRetryGameStart(_) {
		connectionStatus = {
			createGame: {
				attempted: false,
				successful: false
			},
			ws: {
				attempted: false,
				successful: false,
				subscriptionOpen: false
			}
		};
		init();
	}

	function handleStartPlaying(_) {
		// Start Playing
	}

	function init() {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);
		const unsubscribeAnimationConf = animationConfig.subscribe(value => animationConf = value);

		onDestroy(() => {
			unsubscribeApiUrl();
			unsubscribeAnimationConf();
		});

		fetch(`${apiUrlStore}quiz/${quiz.id}/play`, {
			method: 'POST',
			mode: 'cors'
		}).then(res => res.json()).then(data => {
			game = data;
			connectionStatus.createGame.attempted = true;
			connectionStatus.createGame.successful = true;
		}).catch(res => {
			connectionStatus.createGame.attempted = false;
		});

		for (let i = 1000; i <= 10000; i += 1000) {
			setTimeout(() => openWebsocketSubscription(), i);
		}
	}

	async function openWebsocketSubscription() {
		const client = Stomp.client('ws://localhost:8080/ws/connect');
		if (game !== undefined && !connectionStatus.ws.subscriptionOpen) {
			client.connect({}, _ => {
				connectionStatus.ws.subscriptionOpen = true;
				client.subscribe(`/ws/game/${game.id}/players`, rawData => {
					players = JSON.parse(rawData.body);
				});
			});
		}
	}

	$: {
		if (game !== undefined) {
			console.log(game.id);
			console.log(game)
		}
	}
</script>

{#if !connectionStatus.createGame.attempted}
	<LoadingGame createGameStatus={connectionStatus.createGame} on:pageUpdate={handlePageUpdate}
	             on:visibilityChange={handleVisibilityUpdate} on:retryGameStart={handleRetryGameStart}/>
{:else}
	<PlayersJoin quizName={game.quiz.title} {players} colorCode={game.colorCode} on:startPlaying={handleStartPlaying}/>
{/if}