<script>
	import {createEventDispatcher} from 'svelte';
	import {getHexForColor, getTextHexForColor} from '../util/playUtils'

	export let quizName;
	export let players;
	export let colorCode;
	$: playerCount = players.length;

	const dispatch = createEventDispatcher();

	function startPlaying() {
		dispatch('startPlaying');
	}
</script>

<style>
	.colorBar {
		width: calc(calc(100% / 8) - 1%);
		height: 2em;
		display: inline-block;
		margin-right: .5%;
		margin-left: .5%;
	}
</style>

<div class="uk-container uk-container-small uk-margin-xlarge-top">
	<div class="uk-grid-collapse" uk-grid>
		<div class="uk-width-expand">
			<h1>Pihoot</h1>
			<h4>{quizName}</h4>
		</div>
		<div class="uk-width-auto">
            {#if playerCount > 0}
				<button class="uk-button uk-button-primary uk-border-rounded" on:click={startPlaying}>Start playing
				</button>
            {:else}
				<button class="uk-button uk-button-primary uk-border-rounded" on:click={startPlaying} disabled>Start
					playing
				</button>
            {/if}
		</div>
	</div>
	<hr>

	<div class="uk-card uk-card-default uk-card-body uk-card-small uk-border-rounded">
		<p>
			Use the following color code to join the game.
		</p>
        {#each colorCode as color}
			<span class="colorBar uk-border-rounded" style="background-color: {getHexForColor(color)}"></span>
        {/each}
	</div>

	<div class="uk-margin">
        {#each players as player}
			<div class="uk-card uk-card-default uk-card-body uk-card-small uk-text-bold uk-border-rounded uk-margin"
			     style="background-color: {getHexForColor(player.color)}; color: {getTextHexForColor(player.color)};">
                {player.color}
			</div>
        {:else}
			Waiting for players...
        {/each}
	</div>
</div>
