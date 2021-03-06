<script>
	import {api, playableQuizzes, animationConfig} from './stores.js';
	import {onDestroy} from 'svelte';
	import {createEventDispatcher} from 'svelte';
	import PlayableQuizHint from './util/PlayableQuizHint.svelte';

	/**
	 * File description:
	 * The home page with the two navigation buttons to edit and play quizzes.
	 */

	let apiStore;
	let animationConf;
	let playableQuizzesStore;
	const dispatch = createEventDispatcher();

	// Setup the various stores.
	const unsubscribeApi = api.subscribe(value => apiStore = value);
	const unsubscribePlayableQuizzes = playableQuizzes.subscribe(value => playableQuizzesStore = value);
	const unsubscribeAnimationConf = animationConfig.subscribe(value => animationConf = value);
	onDestroy(() => {
		unsubscribeApi();
		unsubscribePlayableQuizzes();
		unsubscribeAnimationConf();
	});

	/**
	 * Fires an event to update the page contents.
	 *
	 * @fires pageUpdate
	 *
	 * @param {string} target The name of the page that should be displayed.
	 */
	const dispatchPageUpdate = (target) => dispatch('pageUpdate', {target: target});
</script>

<div class="uk-container uk-container-small">
	<div class="uk-child-width-expand@s uk-margin-large-top" uk-grid>
		<div class="uk-text-center">
			<!-- The edit button -->
            {#if !apiStore.requestAttempted}
				<button class="uk-button uk-button-primary uk-border-rounded" disabled>
					<div id="play-button-spinner-container" class="uk-text-center">
						<div id="play-button-spinner" uk-spinner></div>
					</div>
				</button>
				<div class="uk-alert-primary uk-border-rounded" uk-alert>
					<p>Attempting to connect to server...</p>
				</div>
            {:else if apiStore.accessible}
				<button class="uk-button uk-button-primary uk-border-rounded"
				        on:click={() => dispatchPageUpdate('edit')}>
					Edit quiz
				</button>
            {:else if !apiStore.accessible}
				<button class="uk-button uk-button-primary uk-border-rounded" disabled>
					Edit quiz
				</button>
				<div class="uk-alert-danger uk-border-rounded" uk-alert>
					<p>It looks like we're unable to open a connection to the database. Please contact the site
						administrator for further assistance.</p>
				</div>
            {/if}
		</div>
		<div class="uk-text-center">
			<!-- The play button -->
            {#if !playableQuizzesStore.requestAttempted}
				<button class="uk-button uk-button-primary uk-border-rounded" disabled>
					<div id="play-button-spinner-container" class="uk-text-center">
						<div id="play-button-spinner" uk-spinner></div>
					</div>
				</button>
				<div class="uk-alert-primary uk-border-rounded" uk-alert>
					<p>Attempting to fetch to quizzes...</p>
				</div>
            {:else if !apiStore.accessible}
				<button class="uk-button uk-button-primary" disabled>
					Play quiz
				</button>
				<div class="uk-alert-danger uk-border-rounded" uk-alert>
					<p>No connection could be established with the database.</p>
				</div>
            {:else if playableQuizzesStore.available}
				<button class="uk-button uk-button-primary uk-border-rounded"
				        on:click={() => dispatchPageUpdate('select')}>
					Play quiz
				</button>
            {:else if !playableQuizzesStore.available}
				<button class="uk-button uk-button-primary uk-border-rounded" disabled>
					Play quiz
				</button>
				<div class="uk-alert-primary uk-border-rounded" uk-alert>
					<p>You don't seem to have enough quizzes to be able to play. Please create some quizzes and try
						again.</p>
				</div>
				<!-- A hint telling the user what makes a quiz playable in case they can't figure it out. -->
				<PlayableQuizHint animationY={animationConf.y} animationDuration={animationConf.duration}/>
            {/if}
		</div>
	</div>
</div>