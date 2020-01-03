<script>
	import {apiUrl, playableQuizzes, playableQuizzesAvailable} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';

	const dispatch = createEventDispatcher();
	let apiUrlStore;
	let connectionSuccessful = false;
	let quizzes = [];
	let playableQuizzesArray = [];
	let anyPlayAbleQuizzes = false;

	$: {
		playableQuizzesArray.length = quizzes.length;
		if (quizzes.length > 0) {
			quizzes.forEach((quiz, i) => {
				playableQuizzesArray[i] = false;
				if (quiz.questions.length > 0) {
					quiz.questions.forEach(question => {
						if (question.answers.length > 1) {
							question.answers.forEach(question => {
								if (question.correct) {
									playableQuizzesArray[i] = true;
								}
							});
						}
					});
				}
			});
			anyPlayAbleQuizzes = false;
			playableQuizzesArray.forEach(playable => {
				if (playable) {
					anyPlayAbleQuizzes = playable;
				}
			});
		}
	}

	const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);

	const init = () => {
		fetch(`${apiUrlStore}quiz`, {
			method: 'GET',
			mode: 'cors'
		}).then(res => {
			connectionSuccessful = true;
			return res.json();
		}).then(data =>
				quizzes = data
		).catch(res => {
			// Do Nothing.
		});

		onDestroy(() => {
			unsubscribeApiUrl();
		});

		fetch(`${apiUrlStore}quiz`, {
			method: 'GET',
			mode: 'cors'
		})
				.then(res => res.json())
				.then(data => playableQuizzes.set({
					available: playableQuizzesAvailable(data),
					requestAttempted: true
				}))
				.catch(playableQuizzes.set({
					available: false,
					requestAttempted: true
				}));
	};

	init();

	let selectedQuiz = {};

	const dispatchPageUpdate = (target, quiz) => dispatch('pageUpdate', {target: target, quiz: quiz});
</script>

{#if connectionSuccessful && anyPlayAbleQuizzes && quizzes.length !== 0}
	<div class="uk-margin-small">
		<select class="uk-select">
			<option value="" style="display: none;" disabled selected>Select quiz</option>
            {#each quizzes as quiz, i}
                {#if playableQuizzesArray[i]}
					<option value="{quiz.id}" on:click={() => selectedQuiz = quiz}>
                        {#if quiz.title === ''}
							No Title
                        {:else}
                            {quiz.title}
                        {/if}
					</option>
                {/if}
            {/each}
		</select>
	</div>

	<div class="uk-margin-small">
		<!-- TODO(laniw): Pass data along when changing page. -->
		<button class="uk-button uk-button-default" on:click={dispatchPageUpdate('game', selectedQuiz)}>Play</button>
	</div>
{:else if quizzes.length === 0 || anyPlayAbleQuizzes}
	<div class="uk-alert-danger" uk-alert>
		<p>No playable Quizzes could be found. I wonder how you got here you cheeky little bastard. ☉ ‿ ⚆</p>
	</div>
{:else}
	<div class="uk-alert-danger" uk-alert>
		<p>No connection could be established with the server. Please try again later.</p>
	</div>
{/if}