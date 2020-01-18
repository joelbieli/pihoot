<script>
	import {createEventDispatcher} from 'svelte';
	import {getHexForColor} from '../util/playUtils'

	export let quizName;
	export let players;
	export let colorCode;

	const dispatch = createEventDispatcher();

	function startPlaying() {
		dispatch('startPlaying');
	}
</script>

<style>
	.colorDot {
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
			<button class="uk-button uk-button-primary uk-border-rounded" on:click={startPlaying}>Start playing</button>
<!--			TODO(laniw): Disable button if less than 1 player is present.-->
		</div>
	</div>
	<hr>

    {#each colorCode as color}
		<span class="colorDot uk-border-rounded" style="background-color: {getHexForColor(color)}">

        </span>
    {/each}

    {#each players as player}
		<div class="uk-card uk-card-default uk-card-body uk-card-small uk-border-rounded uk-margin"
		     style="background-color: {getHexForColor(player.color)}; color: white;">
            {player.color}
		</div>
    {/each}
<!--	TODO(laniw): Add else when no players have joined yet.-->
</div>
