<script>
	import {api} from './stores.js';
	import {playableQuizzes} from './stores.js';
	import {onDestroy} from 'svelte';
	import {createEventDispatcher} from 'svelte';

	let apiStore;
	let playableQuizzesStore;
	const dispatch = createEventDispatcher();

	const unsubscribeApi = api.subscribe(value => apiStore = value);
	const unsubscribePlayableQuizzes = playableQuizzes.subscribe(value => playableQuizzesStore = value);
	onDestroy(() => {
		unsubscribeApi();
		unsubscribePlayableQuizzes();
	});

	const dispatchPageUpdate = (target) => dispatch('pageUpdate', {target: target});
</script>

<div class="uk-child-width-expand@s uk-margin-large-top" uk-grid>
	<div class="uk-text-center">
        {#if !apiStore.requestAttempted}
			<button class="uk-button uk-button-primary" disabled>
				<div id="play-button-spinner-container" class="uk-text-center">
					<div id="play-button-spinner" uk-spinner></div>
				</div>
			</button>
			<div class="uk-alert-primary" uk-alert>
				<p>Attempting to connect to server...</p>
			</div>
        {:else if apiStore.accessible}
			<button class="uk-button uk-button-primary" on:click={() => dispatchPageUpdate('edit')}>
				Edit quiz
			</button>
        {:else if !apiStore.accessible}
			<button class="uk-button uk-button-primary" disabled>
				Edit quiz
			</button>
			<div class="uk-alert-danger" uk-alert>
				<p>It looks like we're unable to open a connection to the database. Please contact the site
					administrator for further assistance.</p>
			</div>
        {/if}
	</div>
	<div class="uk-text-center">
        {#if !playableQuizzesStore.requestAttempted}
			<button class="uk-button uk-button-primary" disabled>
				<div id="play-button-spinner-container" class="uk-text-center">
					<div id="play-button-spinner" uk-spinner></div>
				</div>
			</button>
			<div class="uk-alert-primary" uk-alert>
				<p>Attempting to fetch to quizzes...</p>
			</div>
        {:else if !apiStore.accessible}
			<button class="uk-button uk-button-primary" disabled>
				Play quiz
			</button>
			<div class="uk-alert-danger" uk-alert>
				<p>No connection could be established with the database.</p>
			</div>
        {:else if playableQuizzesStore.available}
			<button class="uk-button uk-button-primary" on:click={() => dispatchPageUpdate('play')}>
				Play quiz
			</button>
        {:else if !playableQuizzesStore.available}
			<button class="uk-button uk-button-primary" disabled>
				Play quiz
			</button>
			<div class="uk-alert-primary" uk-alert>
				<p>You don't seem to have enough quizzes to be able to play. Please create some quizzes and try
					again.</p>
			</div>
        {/if}
	</div>
</div>