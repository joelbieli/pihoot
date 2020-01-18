<script>
	import TimedLoadingBar from '../../util/TimedLoadingBar.svelte';
	import {getHexForColor} from '../../util/playUtils'

	export let question;

	let countDown;

	let climbingI = 0;
	for (let i = 15; i >= 0; i -= 1) {
		setTimeout(() => countDown = i, 1000 * climbingI);
		climbingI += 1;
	}
</script>

<style>
	.answer {
		color: white;
	}
</style>

<div class="uk-container uk-container-xsmall">
	<TimedLoadingBar seconds="15" barColor="#1e87f0" wrapperColor="#bababa"/>
	<h1>
        {question.question}
	</h1>
	<div class="uk-grid-small" uk-grid>
		<div class="uk-width-1-2 answer" style="background-color: {getHexForColor(question.answers[0].color)}">
            {question.answers[0].answer}
		</div>
		<div class="uk-width-1-2 answer" style="background-color: {getHexForColor(question.answers[1].color)}">
            {question.answers[1].answer}
		</div>
		<div class="uk-width-1-2 answer" style="background-color: {getHexForColor(question.answers[2].color)}">
            {question.answers[2].answer}
		</div>
		<div class="uk-width-1-2 answer" style="background-color: {getHexForColor(question.answers[3].color)}">
            {question.answers[3].answer}
		</div>
	</div>
</div>