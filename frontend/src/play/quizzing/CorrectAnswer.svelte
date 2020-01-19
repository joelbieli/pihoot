<script>
	import {createEventDispatcher} from 'svelte';
	import {getHexForColor, getTextHexForColor} from '../../util/playUtils'

	export let question;
	export let questionIndex;
	export let questionCount;

	console.log('loaded');

	const dispatch = createEventDispatcher();

	function returnHome() {
		dispatch('returnHome');
	}

	function showScoreboard() {
		console.log('showScoreboard');
		dispatch('showScoreboard');
	}
</script>

<style>
	.answer {
		font-weight: bold;
	}
</style>

<div class="uk-overlay uk-position-top-left">
    {questionIndex} of {questionCount}
</div>

<div class="uk-grid uk-margin" uk-grid="">
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
<!-- TODO(laniw): Sort answers by color to be the same as on the answering hardware. -->
<div class="uk-grid-small" uk-grid>
    {#each question.answers as answer}
		<div class="uk-width-1-2">
            {#if answer.answer !== ''}
				<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
				     style="{answer.correct ? `background-color: ${getHexForColor(answer.color)}` : ''}">
					<div class="uk-grid-small" uk-grid>
						<div class="uk-width-expand">
							<h3 class="answer"
							    style="{answer.correct ? `color: ${getTextHexForColor(answer.color)}` : ''}">
                                {answer.answer}
							</h3>
						</div>
						<div class="uk-width-auto">
                            {#if answer.correct}
								<span uk-icon="icon: check; ratio: 1.5"></span>
                            {:else}
								<span uk-icon="icon: close; ratio: 1.5"></span>
                            {/if}
						</div>
					</div>
				</div>
            {:else}
				<div class="uk-card uk-card-default uk-card-small"></div>
            {/if}
		</div>
    {/each}
</div>