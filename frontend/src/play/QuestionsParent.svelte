<script>
	import {apiUrl} from '../stores.js';
	import {onDestroy} from 'svelte';
	import Question from './quizzing/Question.svelte';
	import Answer from './quizzing/Answer.svelte';
	import Scoreboard from './quizzing/Scoreboard.svelte';

	export let game;
	let apiUrlStore;

	let currentQuestion;
	let currentQuestionIndex = 0;
	let showOnlyQuestion = false;
	let showAnswers = false;
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
			showScoreboard = showScoreboard ? showScoreboard : true;
			endQuestion();
		}, 1000 * 20);

		currentQuestionIndex += 1;
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
</script>

<div class="uk-container uk-container-small uk-margin-xlarge-top">
    {#if showOnlyQuestion && !showScoreboard}
		<Question question={currentQuestion} questionIndex={currentQuestionIndex}
		          questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && !showScoreboard && showAnswers}
		<Answer question={currentQuestion} questionIndex={currentQuestionIndex}
				questionCount={game.quiz.questions.length}/>
    {:else if !showOnlyQuestion && showScoreboard && currentQuestionIndex !== game.quiz.questions.length}
		<Scoreboard on:nextQuestion={playNextQuestion}/>
    {:else}
		<div class="uk-alert-danger uk-border-rounded" uk-alert>
			<p>Somebody did a big oopsie here. ts ts ts...</p>
		</div>
    {/if}
</div>
