<script>
	import {fly} from 'svelte/transition';

	export let animationY;
	export let animationDuration;

	let playableQuizHintDisplayed = false;
	let playableQuizHintExpanderDisplayed = true;

	/**
	 * Shows the hing and hides the summary.
	 */
	function displayHint() {
		playableQuizHintExpanderDisplayed = false;
		// Since I'm working with an animation I have to add a delay to make the elements appear and disappear at the correct time.
		setTimeout(() => playableQuizHintDisplayed = true, animationDuration);
	}

	/**
	 * Shows the summary and hides the hint.
	 */
	function hideHint() {
		playableQuizHintDisplayed = false;
		// Since I'm working with an animation I have to add a delay to make the elements appear and disappear at the correct time.
		setTimeout(() => playableQuizHintExpanderDisplayed = true, animationDuration);
	}
</script>

<style>
	/* Turns the mouse into a hand to show that something is clickable. */
	.mouse-hand {
		cursor: pointer;
	}
</style>

<div class="uk-alert-primary uk-border-rounded uk-text-left mouse-hand"
     on:click={() => playableQuizHintDisplayed ? hideHint() : displayHint()}
     uk-alert>
	<span class="uk-text-primary" uk-icon="info"></span>
    {#if playableQuizHintExpanderDisplayed}
		<span transition:fly="{{ y: -animationY, duration: animationDuration }}">Don't know what makes a quiz playable? Click here to find out.</span>
    {/if}
    {#if playableQuizHintDisplayed}
		<div transition:fly="{{ y: -animationY/2, duration: animationDuration}}">
			<p class="uk-margin-small-top uk-margin-remove-bottom">For the play quiz page to become available the
				following must be true:</p>
			<ul class="uk-margin-small-top">
				<li>At least one quiz has to be saved</li>
				<li>One quiz must have at least one question</li>
				<li>At least one of the answers to a question must be true</li>
			</ul>
			<p class="uk-margin-top uk-margin-remove-bottom">Once you are on the play quiz page very similar criteria
				determine whether a quiz can be chosen or not:</p>
			<ul class="uk-margin-small-top">
				<li>The quiz has to have at least one question</li>
				<li>At least one question must have a correct answer.</li>
			</ul>
			<span class="uk-text-warning">
				If you find that you can open the play quiz page but no quizzes show up, plesae contact the system administrator.
			</span>
		</div>
    {/if}
</div>