<script>
	import {createEventDispatcher} from 'svelte';

	export let createGameStatus;
	const dispatch = createEventDispatcher();

	function retryGameStart() {
		dispatch('retryGameStart');
	}

	function returnHome() {
		dispatch('pageUpdate', {target: 'home'});
		let visibilities = {
			navbar: true,
			container: true,
			title: true,
			subtitle: true,
			divider: true,
			text: true
		};
		dispatch('visibilityChange', visibilities);
	}
</script>

<style>
	#container {
		margin-top: 25%;
	}
</style>

<div id="container">
	{#if !createGameStatus.attempted}
		<div class="uk-container uk-container-xsmall uk-text-center">
			<h1>Starting up game...</h1>
			<div class="uk-margin" uk-spinner="ratio: 5"></div>
		</div>
	{:else if createGameStatus.attempted && !createGameStatus.successful}
	<div class="uk-container uk-container-xsmall uk-card uk-card-default uk-card-body uk-text-center uk-border-rounded">
		<h4>An issue was encountered while trying to load the game.</h4>
		<p>
			Would you like to reattempt loading the game?
		</p>
		<button class="uk-button uk-button-primary uk-border-rounded" on:click={retryGameStart}>Retry</button>
		<button class="uk-button uk-button-primary uk-border-rounded uk-margin-small-left" on:click={returnHome}>Return Home</button>
	</div>
	{/if}
</div>