<script>
	import {apiUrl, animationConfig} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';
	import PreGame from './PreGame.svelte';
	import PlayersJoin from './PlayersJoin.svelte';
	import QuestionsParent from './QuestionsParent.svelte';

	/**
	 * File description:
	 * Provides a component that contains all of the logic to play a quiz.
	 */

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
		},
		startGame: {
			attempted: false,
			successful: false
		},
		endGame: {
			attempted: false,
			successful: false
		}
	};

	init();

	/**
	 * Accepts an event and passes on the pageUpdate event to the router.
	 *
	 * @param {Object} e The event data.
	 */
	function handlePageUpdate(e) {
		dispatch('pageUpdate', e.detail);
	}

	/**
	 * Accepts an event and passes on the visibilityChange event to the router.
	 *
	 * @param {Object} e The event data.
	 */
	function handleVisibilityUpdate(e) {
		dispatch('visibilityChange', e.detail);
	}

	/**
	 * Retries to start a game if it failed before.
	 *
	 * @param {Object} _ The event data.
	 */
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

	/**
	 * Handles the startPlaying event and starts the game.
	 *
	 * @param {Object} _ The event data.
	 */
	function handleStartPlaying(_) {
		startGame();
	}

	/**
	 * Calls the endpoint that starts the game for the backend so no new players can join the game.
	 */
	function startGame() {
		fetch(`${apiUrlStore}game/${game.id}/start`, {
			method: 'POST',
			mode: 'cors'
		}).then(_ => {
			connectionStatus.startGame.attempted = true;
			connectionStatus.startGame.successful = true;
		}).catch(_ => {
			connectionStatus.startGame.attempted = true;
		});
	}

	/**
	 * Calls the endpoint that starts the game for the backend so no new players can join the game.
	 */
	function endGame() {
		fetch(`${apiUrlStore}game/${game.id}/end`, {
			method: 'POST',
			mode: 'cors'
		}).then(_ => {
			connectionStatus.endGame.attempted = true;
			connectionStatus.endGame.successful = true;
		}).catch(_ => {
			connectionStatus.endGame.attempted = true;
		});
	}

	/**
	 * Initiates every needed resource for proper functioning of the page.
	 *
	 * - Subscribes to stores
	 * - Gets the game object
	 * - Subscribes to player websocket
	 */
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
		}).catch(_ => {
			connectionStatus.createGame.attempted = true;
		});

		let count = 0;
		setInterval(() => openWebsocketSubscription(), 1000);
		for (let i = 1000; i <= 10000; i += 1000) {
			setTimeout(() => openWebsocketSubscription(), i);
		}
	}

	/**
	 * Subscribes to the player websocket to get notified every time a new player joins.
	 */
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

	/**
	 * Handles the return home event and ends the game.
	 *
	 * When the user commands that he wants to go back to the home screen this function ends the game, updates the displayed page and visibilities.
	 *
	 * @param {Object} e The event data.
	 */
	function handleReturnHome(e){
		endGame();
		handlePageUpdate(e);
		handleVisibilityUpdate(e)
	}

	// DEBUGGING Prints the game id to the console to be able to participate in the game over simple REST requests.
	$: {
		if (game !== undefined) {
			console.log(game.id);
		}
	}
</script>

{#if !connectionStatus.createGame.attempted}
	<PreGame createGameStatus={connectionStatus.createGame} on:pageUpdate={handlePageUpdate}
	         on:visibilityChange={handleVisibilityUpdate} on:retryGameStart={handleRetryGameStart}/>
{:else if !connectionStatus.startGame.successful}
	<PlayersJoin quizName={game.quiz.title} {players} colorCode={game.colorCode} on:startPlaying={handleStartPlaying}/>
{:else if connectionStatus.startGame.successful}
	<QuestionsParent {game} {players} on:stopGame={endGame} on:returnHome={handleReturnHome}/>
{/if}