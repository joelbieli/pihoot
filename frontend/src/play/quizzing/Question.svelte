<script>
	import TimedLoadingBar from '../../util/TimedLoadingBar.svelte';

	export let question;
	export let questionIndex;
	export let questionCount;

	let countDown;

	let climbingI = 0;
	for (let i = 5; i >= 0; i -= 1) {
		setTimeout(() => countDown = i, 1000 * climbingI);
		climbingI += 1;
	}
</script>

<div class="uk-overlay uk-position-top-left">
	{questionIndex+1} of {questionCount}
</div>
<div class="uk-container uk-container-xsmall">
		<h2>
			{question.question}
		</h2>
		<h3>
            {countDown}
		</h3>

		<TimedLoadingBar seconds="5" barColor="#1e87f0" wrapperColor="#bababa"/>
</div>