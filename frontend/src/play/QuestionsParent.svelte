<script>
	import {apiUrl} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';
	import Question from './quizzing/Question.svelte';
	import Answer from './quizzing/Answer.svelte';
	import CorrectAnswer from './quizzing/CorrectAnswer.svelte';
	import Scoreboard from './quizzing/Scoreboard.svelte';

	export let game;
	export let players;
	let apiUrlStore;

	const dispatch = createEventDispatcher();

	let currentQuestion;
	let currentQuestionIndex = 0;
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
		}
	};

	init();

	function playNextQuestion() {
		currentQuestion = game.quiz.questions[currentQuestionIndex];
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
			showAnswers = false;
			showCorrectAnswers = showCorrectAnswers ? showCorrectAnswers : true;
			endQuestion();
			if (game.quiz.questions.length <= currentQuestionIndex) {
				stopGame();
			}
		}, 1000 * 20);

		currentQuestionIndex += 1;
	}

	function switchToScoreboard() {
		showCorrectAnswers = false;
		showScoreboard = true;
	}

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

	function init() {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

		onDestroy(() => {
			unsubscribeApiUrl();
		});

		playNextQuestion();
	}

	function stopGame() {
		dispatch('stopGame');
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

<div class="uk-container uk-container-small uk-margin-xlarge-top">
    {#if showOnlyQuestion && !showAnswers && !showCorrectAnswers && !showScoreboard}
		<Question question={currentQuestion} questionIndex={currentQuestionIndex}
		          questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && showAnswers && !showCorrectAnswers && !showScoreboard}
		<Answer question={currentQuestion} questionIndex={currentQuestionIndex}
		        questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && !showAnswers && showCorrectAnswers && !showScoreboard}
		<CorrectAnswer question={currentQuestion} questionIndex={currentQuestionIndex}
		               questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && !showAnswers && showScoreboard && currentQuestionIndex !== game.quiz.questions.length}
		<Scoreboard {game} {players} on:nextQuestion={playNextQuestion} on:returnHome={handleReturnHome}/>
    {:else if !showOnlyQuestion && !showAnswers && showScoreboard && currentQuestionIndex === game.quiz.questions.length}
		Final scoreboard
    {:else}
		<div class="uk-alert-danger uk-border-rounded" uk-alert>
			<p>Somebody did a big oopsie here. ts ts ts...</p>
		</div>
    {/if}
</div>
