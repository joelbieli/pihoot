<script>
	import {apiUrl, playableQuizzes, playableQuizzesAvailable} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';

	/**
	 * File description:
	 * Provides a component that lets the user choose what playable game they want to play.
	 */

	const dispatch = createEventDispatcher();
	let apiUrlStore;
	let connectionSuccessful = false;
	let quizzes = [];
	let playableQuizzesArray = [];
	let anyPlayAbleQuizzes = false;

	/**
	 * Updates the playable quizzes array any time something from the quizzes changes.
	 */
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

	/**
	 * Initiates every needed resource for proper functioning of the page.
	 *
	 * - Fetches the quizzes
	 * - Subscribes to stores
	 * - Updates playable quizzes store
	 */
	const init = () => {
		const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);
		onDestroy(() => {
			unsubscribeApiUrl();
		});

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

		fetch(`${apiUrlStore}quiz`, {
			method: 'GET',
			mode: 'cors'
		}).then(res => res.json()).then(data => playableQuizzes.set({
			available: playableQuizzesAvailable(data),
			requestAttempted: true
		})).catch(playableQuizzes.set({
			available: false,
			requestAttempted: true
		}));
	};

	init();

	let selectedQuiz = {};

	/**
	 * Sets the selectedQuiz variable and playAbleQuizSelected when an option in the select is chosen.
	 */
	function selectQuiz() {
		let e = document.getElementById("quiz-select");
		let selectedQuizId = e.options[e.selectedIndex].value;
		if (quizzes.length > 0) {
			quizzes.forEach(quiz => {
				if (quiz.id === selectedQuizId) {
					selectedQuiz = quiz;
				}
			});
		} else {
			console.error('No quizzes to select!');
			return;
		}
		if (selectedQuiz === 'undefined') {
			console.error('Quiz with given id not found!');
			return;
		}
		playableQuizSelected = true;
	}

	/**
	 * Ensures that the selectedQuiz is actually playable.
	 */
	let playableQuizSelected;
	$: {
		playableQuizSelected = false;
		if (selectedQuiz.questions !== undefined && selectedQuiz.questions.length > 0) {
			selectedQuiz.questions.forEach(question => {
				if (question.answers.length > 1) {
					question.answers.forEach(question => {
						if (question.correct) {
							playableQuizSelected = true;
						}
					});
				}
			});
		}
	}

	/**
	 * Passes a pageUpdate event to its parent component to go to the play screen, passing along data as well.
	 *
	 * @fires pageUpdate
	 */
	const dispatchPageUpdate = (target, data) => dispatch('pageUpdate', {target: target, data: data});

	/**
	 * Passes a visibilitiesChange event to its parent component to go to the play screen, passing along data as well.
	 *
	 * @fires visibilitiesChange
	 */
	const dispatchVisibilitiesChange = visibilities => dispatch('visibilityChange', visibilities);

	/**
	 * Launches the needed functions to redirect to the play quiz and pass on the selected quiz.
	 *
	 * @param {Array} quiz The quiz that will be played.
	 * @param {boolean} showNavbar Whether the navbar should be visible.
	 * @param {boolean} showContainer Whether the container with the title, subtitle, divider and text should be visible.
	 * @param {boolean} showTitle Whether the title should be visible.
	 * @param {boolean} showSubtitle Whether the subtitle should be visible.
	 * @param {boolean} showDivider Whether the divider should be visible.
	 * @param {boolean} showText Whether the text should be visible.
	 */
	function playSelectedQuiz(quiz, showNavbar, showContainer, showTitle, showSubtitle, showDivider, showText) {
		dispatchVisibilitiesChange({
			navbar: showNavbar,
			container: showContainer,
			title: showTitle,
			subtitle: showSubtitle,
			divider: showDivider,
			text: showText
		});
		let data = {quiz: quiz};
		dispatchPageUpdate('play', data);
	}
</script>

<div class="uk-container uk-container-small">
    {#if connectionSuccessful && anyPlayAbleQuizzes && quizzes.length !== 0}
		<div class="uk-margin-small">
			<select id="quiz-select" class="uk-select uk-border-rounded" on:change={selectQuiz}>
				<option value="" style="display: none;" disabled selected>Select quiz</option>
                {#each quizzes as quiz, i}
                    {#if playableQuizzesArray[i]}
						<option value="{quiz.id}">
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
            {#if playableQuizSelected}
				<button class="uk-button uk-button-primary uk-border-rounded"
				        on:click={() => playSelectedQuiz(selectedQuiz, false, false, false, false, false, false)}>Play
				</button>
            {:else}
				<button class="uk-button uk-button-primary uk-border-rounded" disabled>Play</button>
            {/if}
		</div>
    {:else if quizzes.length === 0 || anyPlayAbleQuizzes}
		<div class="uk-alert-danger" uk-alert>
			<p>No playable Quizzes could be found. I wonder how you got here you cheeky little goofball. ☉ ‿ ⚆</p>
		</div>
    {:else}
		<div class="uk-alert-danger" uk-alert>
			<p>No connection could be established with the server. Please try again later.</p>
		</div>
    {/if}
</div>