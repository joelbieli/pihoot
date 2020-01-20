<script>
	import {apiUrl} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';
	import Question from './quizzing/Question.svelte';
	import Answer from './quizzing/Answers.svelte';
	import CorrectAnswer from './quizzing/CorrectAnswers.svelte';
	import Scoreboard from './quizzing/Scoreboard.svelte';
	import Endscreen from "./Endscreen.svelte";

	/**
	 * File description:
	 * Provides a component that houses the needed to go through once cycle of question, answer, correct answers and scoreboard.
	 */

	export let game;
	export let players;
	let apiUrlStore;

	const dispatch = createEventDispatcher();

	let answeredCount;
	let currentQuestion;
	let currentQuestionIndex = 0;
	// Properties defining what stage of the game is visible.
	let showOnlyQuestion = false;
	let showAnswers = false;
	let showCorrectAnswers = false;
	let showScoreboard = false;
	let state = {
		startQuestion: {
			attempted: false,
			successful: false
		},
		endQuestion: {
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

	/**
	 * Queues the screens for the next question with the correct timings.
	 */
	function playNextQuestion() {
		currentQuestion = game.quiz.questions[currentQuestionIndex];
		currentQuestion.answers = sortAnswersForHardware(currentQuestion.answers);
		// Clear scoreboard status for next question.
		showScoreboard = false;
		// Show only the question for 5 seconds.
		showOnlyQuestion = true;
		setTimeout(() => {
			showOnlyQuestion = false;
			showAnswers = true;
			startQuestion();
		}, 5000);
		// Show scoreboard after 20 seconds
		setTimeout(() => {
			switchToCorrectAnswers()
		}, 1000 * 20);

		currentQuestionIndex += 1;
	}

	function sortAnswersForHardware(answers) {
		let sortedAnswers = [{}, {}, {}, {}];

		let colorToIndexMapper = {
			'RED': 0,
			'GREEN': 1,
			'BLUE': 2,
			'YELLOW': 3
		};

		answers.forEach(answer => {
			sortedAnswers[colorToIndexMapper[answer.color]] = answer;
		});

		console.log(sortedAnswers);
		return sortedAnswers;
	}

	/**
	 * Switches to the screen showing which answers are correct.
	 */
	function switchToCorrectAnswers() {
		showAnswers = false;
		showCorrectAnswers = showCorrectAnswers ? showCorrectAnswers : true;
		endQuestion();
		if (game.quiz.questions.length <= currentQuestionIndex) {
			stopGame();
		}
	}

	/**
	 * Switches to the scoreboard screen.
	 */
	function switchToScoreboard() {
		console.log('showing');
		showCorrectAnswers = false;
		showScoreboard = true;
	}

	/**
	 * Calls the start question endpoint to signalise to the backend that the players can start answering the question.
	 */
	function startQuestion() {
		fetch(`${apiUrlStore}game/${game.id}/question/${currentQuestion.id}/begin`, {
			method: 'POST',
			mode: 'cors'
		}).then(_ => {
			state.startQuestion.attempted = true;
			state.startQuestion.successful = true;
		}).catch(_ => {
			state.startQuestion.attempted = true;
		});
	}

	/**
	 * Calls the end question endpoint to signalise to the backend that the players can st art answering the question.
	 */
	function endQuestion() {
		fetch(`${apiUrlStore}game/${game.id}/question/${currentQuestion.id}/end`, {
			method: 'POST',
			mode: 'cors'
		}).then(_ => {
			state.endQuestion.attempted = true;
			state.endQuestion.successful = true;
		}).catch(_ => {
			state.endQuestion.attempted = true;
		});
	}

	/**
	 * Initiates every needed resource for proper functioning of the page.
	 *
	 * - Subscribes to stores
	 * - Loads up the first question
	 * - Subscribes to answers websocket
	 */
	function init() {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

		onDestroy(() => {
			unsubscribeApiUrl();
		});

		playNextQuestion();

		let counter = 0;
		let interval = setInterval(() => {
			if (counter < 10) {
				openWebsocketSubscription();
			} else {
				clearInterval(interval);
			}
			counter += 1;
		}, 1000);
	}

	/**
	 * Subscribes to the answers websocket to get notified every time a player answers a question to go to the next screen as soon as all players have answered.
	 */
	async function openWebsocketSubscription() {
		const client = Stomp.client('ws://localhost:8080/ws/connect');
		if (game !== undefined && !state.ws.subscriptionOpen) {
			client.connect({}, _ => {
				state.ws.subscriptionOpen = true;
				client.subscribe(`/ws/game/${game.id}/answers`, rawData => {
					answeredCount = JSON.parse(rawData.body);
					if (answeredCount === players.length) {
						switchToCorrectAnswers();
					}
				});
			});
		}
	}

	/**
	 * Passes on a stopGame event to the parent component.
	 *
	 * @fires stopGame
	 */
	function stopGame() {
		dispatch('stopGame');
	}

	/**
	 * Passes on a returnHome event to the parent component.
	 *
	 * @fires returnHome
	 */
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

<div class="uk-container uk-container-small uk-margin-xlarge-top">
    {#if showOnlyQuestion && !showAnswers && !showCorrectAnswers && !showScoreboard}
		<Question question={currentQuestion} questionIndex={currentQuestionIndex}
		          questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && showAnswers && !showCorrectAnswers && !showScoreboard}
		<Answer question={currentQuestion} questionIndex={currentQuestionIndex}
		        questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && !showAnswers && showCorrectAnswers && !showScoreboard}
		<CorrectAnswer question={currentQuestion} questionIndex={currentQuestionIndex}
		               questionCount={game.quiz.questions.length} on:showScoreboard={switchToScoreboard}
		               on:returnHome={handleReturnHome}/>
    {:else if !showOnlyQuestion && !showAnswers && showScoreboard && currentQuestionIndex !== game.quiz.questions.length}
		<Scoreboard {game} {players} on:nextQuestion={playNextQuestion} on:returnHome={handleReturnHome}/>
    {:else if !showOnlyQuestion && !showAnswers && showScoreboard && currentQuestionIndex === game.quiz.questions.length}
		<Endscreen {game} {players} on:returnHome={handleReturnHome}></Endscreen>
    {:else}
		<div class="uk-alert-danger uk-border-rounded" uk-alert>
			<p>Somebody did a big oopsie here. ts ts ts...</p>
		</div>
    {/if}
</div>
