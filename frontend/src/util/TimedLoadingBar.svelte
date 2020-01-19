<script>
	export let seconds;
	export let barColor;
	export let wrapperColor;

	let width = 0;
	let bar = document.getElementsByClassName('bar');
	let interval = setInterval(() => {
		if (width >= 100) {
			clearInterval(interval);
		} else {
			// The longer this should run, the smaller the value by which the loader width should be increased by should be.
			width += 1 / seconds;
		}
	}, 10);
</script>

<style>
	.barWrapper {
		width: 100%;
	}

	.bar {
		width: 0;
		height: 10px;
	}
</style>

<!-- The loading bar wrapper that shows "how far to the right it can load". -->
<div class="barWrapper uk-border-rounded" style="background-color: {wrapperColor}">
	<!-- The loading bar that expands to show a loading animation. -->
	<div class="bar uk-border-rounded" style="background-color: {barColor}; width: {width}%;"></div>
</div>