<script>
	import {createEventDispatcher} from 'svelte';

	/**
	 * File description:
	 * Provides a component that shows a loading screen before the game has been created and an error screen if the game could not be created.
	 */

	export let createGameStatus;
	const dispatch = createEventDispatcher();

	/**
	 * Fires a retryGameStart event to its parent to retry the game start.
	 *
	 * @fires retryGameStart
	 */
	function retryGameStart() {
		dispatch('retryGameStart');
	}

	/**
	 * Dispatches a pageUpdate and visibilitiesChange event to go back to the home screen.
	 *
	 * @fires pageUpdate
	 * @fires visibilitiesChange
	 */
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

{#if !createGameStatus.attempted}
	<div class="uk-container uk-container-xsmall uk-text-center uk-position-center">
		<h1>Starting up game...</h1>
		<div class="uk-margin" uk-spinner="ratio: 5"></div>
	</div>
{:else if createGameStatus.attempted && !createGameStatus.successful}
	<div class="uk-container uk-container-xsmall uk-card uk-card-default uk-card-body uk-text-center uk-border-rounded uk-position-center">
		<h4>An issue was encountered while trying to load the game.</h4>
		<p>
			Would you like to reattempt loading the game?
		</p>
		<button class="uk-button uk-button-primary uk-border-rounded" on:click={retryGameStart}>Retry</button>
		<button class="uk-button uk-button-primary uk-border-rounded uk-margin-small-left" on:click={returnHome}>Return
			Home
		</button>
	</div>
{/if}