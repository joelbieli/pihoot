<script>
	import TimedLoadingBar from '../../util/TimedLoadingBar.svelte';
	import {getHexForColor, getTextHexForColor} from '../../util/playUtils'

	/**
	 * File description:
	 * Provides a component to show the answers a player can choose.
	 */
	// TODO(laniw): Modify text color of cross/tick based on background color.

	export let question;
	export let questionIndex;
	export let questionCount;

	let countDown = 15;

	// Updates the countdown value every second.
	let interval = setInterval(() => {
		if (countDown <= 0) {
			clearInterval(interval);
		} else {
			countDown -= 1;
		}
	}, 1000);
</script>

<style>
	.answer {
		font-weight: bold;
	}
</style>

<div class="uk-overlay uk-position-top-left">
    {questionIndex} of {questionCount}
</div>

<TimedLoadingBar seconds="15" barColor="#1e87f0" wrapperColor="#bababa"/>
<div class="uk-grid uk-margin" uk-grid="">
	<div class="uk-width-expand">
		<h1>
            {question.question}
		</h1>
	</div>
	<div class="uk-width-auto">
		<div class="uk-card uk-card-primary uk-card-body uk-border-rounded uk-card-small">
			<h5>
                {countDown}
			</h5>
		</div>
	</div>
</div>
<div class="uk-grid-small" uk-grid>
    {#each question.answers as answer}
		<div class="uk-width-1-2">
			{#if answer.answer !== ''}
				<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
					 style="background-color: {getHexForColor(answer.color)}">
					<h3 class="answer" style="color: {getTextHexForColor(answer.color)}">
						{answer.answer}
					</h3>
				</div>
			{:else}
				<div class="uk-card uk-card-default uk-card-small"></div>
			{/if}
		</div>
    {/each}
</div>