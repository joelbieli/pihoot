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

<div class="barWrapper uk-border-rounded" style="background-color: {wrapperColor}">
	<div class="bar uk-border-rounded" style="background-color: {barColor}; width: {width}%;"></div>
</div>