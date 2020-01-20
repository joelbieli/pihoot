<script>
	import Answer from './answerSubcomponents/Answer.svelte';
	import {createEventDispatcher} from 'svelte';

	/**
	 * File description:
	 * Provides a component that shows the players what answers were right.
	 */

	export let question;
	export let questionIndex;
	export let questionCount;

	console.log('loaded');

	const dispatch = createEventDispatcher();

	/**
	 * Passes a returnHome event to its parent component to return back to the home screen.
	 *
	 * @fires returnHome
	 */
	function returnHome() {
		dispatch('returnHome');
	}

	/**
	 * Passes a showScoreboard event to its parent component to display the scoreboard.
	 *
	 * @fires showScoreboard
	 */
	function showScoreboard() {
		dispatch('showScoreboard');
	}
</script>

<div class="uk-overlay uk-position-top-left">
    {questionIndex} of {questionCount}
</div>

<div class="uk-grid uk-margin" uk-grid>
	<div class="uk-width-expand">
		<h1>
            {question.question}
		</h1>
	</div>
	<div class="uk-width-auto">
		<button class="uk-button uk-button-default uk-border-rounded" on:click={returnHome}>Cancel and return home
		</button>
		<button class="uk-button uk-button-primary uk-border-rounded" on:click={showScoreboard}>Show Scoreboard</button>
	</div>
</div>
<div class="uk-grid-small" uk-grid>
    {#each question.answers as answer}
		<Answer {answer} showWhetherAnswerCorrect={true}/>
    {/each}
</div>