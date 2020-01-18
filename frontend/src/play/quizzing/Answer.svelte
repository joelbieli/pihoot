<script>
	import TimedLoadingBar from '../../util/TimedLoadingBar.svelte';
	import {getHexForColor} from '../../util/playUtils'

	export let question;
	export let questionIndex;
	export let questionCount;


	let countDown = 15;

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
		color: white;
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
	<div class="uk-width-1-2 answer">
        {#if question.answers[0].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[0].color)}">
				<h2>
                    {question.answers[0].answer}
				</h2>
			</div>
        {/if}
	</div>
	<div class="uk-width-1-2 answer">
        {#if question.answers[1].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[1].color)}">
				<h2>
                    {question.answers[1].answer}
				</h2>
			</div>
        {/if}
	</div>
	<div class="uk-width-1-2 answer">
        {#if question.answers[2].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[2].color)}">
				<h2>
                    {question.answers[2].answer}
				</h2>
			</div>
        {/if}
	</div>
	<div class="uk-width-1-2 answer">
        {#if question.answers[3].answer !== ''}
			<div class="uk-card uk-card-default uk-card-small uk-card-body uk-box-shadow-large uk-border-rounded"
			     style="background-color: {getHexForColor(question.answers[3].color)}">
				<h2>
                    {question.answers[3].answer}
				</h2>
			</div>
        {/if}
	</div>
</div>