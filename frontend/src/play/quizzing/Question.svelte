<script>
	import TimedLoadingBar from '../../util/TimedLoadingBar.svelte';

	export let question;
	export let questionIndex;
	export let questionCount;

	let countDown = 5;

	// Update the countdown value every second.
	let interval = setInterval(() => {
		if (countDown <= 0) {
			clearInterval(interval);
		} else {
			countDown -= 1;
		}
	}, 1000);
</script>

<div class="uk-overlay uk-position-top-left">
    {questionIndex} of {questionCount}
</div>

<TimedLoadingBar seconds="5" barColor="#1e87f0" wrapperColor="#bababa"/>
<div class="uk-grid uk-margin" uk-grid="">
	<div class="uk-width-expand">
		<h3>
			Get ready!
		</h3>
	</div>
	<div class="uk-width-auto">
		<div class="uk-card uk-card-primary uk-card-body uk-border-rounded uk-card-small">
			<h5>
				{countDown}
			</h5>
		</div>
	</div>
</div>
<div class="uk-card uk-card-body uk-card-default uk-border-rounded">
	<h2>
        {question.question}
	</h2>
</div>