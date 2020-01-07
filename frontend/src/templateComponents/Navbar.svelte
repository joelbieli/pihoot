<script>
	import {api} from '../stores.js';
	import {playableQuizzes} from '../stores.js';
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

<nav class="uk-navbar-container" uk-navbar>
	<div class="uk-navbar-left">

		<ul class="uk-navbar-nav">
			<a class="uk-navbar-item uk-logo" on:click={() => dispatchPageUpdate('home')}>Pihoot</a>
			<li>
				<a>Actions <span uk-icon="chevron-down"></span></a>
				<div class="uk-navbar-dropdown">
					<ul class="uk-nav uk-navbar-dropdown-nav">
						<li>
                            {#if !apiStore.requestAttempted}
								<span uk-spinner="ratio: .5"></span>
                            {:else if apiStore.accessible}
								<a on:click={() => dispatchPageUpdate('edit')}>Edit quiz</a>
                            {:else if !apiStore.accessible}
								<a class="uk-link-muted" uk-tooltip="Connection to database could not be established.">Edit
									quiz</a>
                            {/if}
						</li>
						<li>
                            {#if !playableQuizzesStore.requestAttempted}
								<span uk-spinner="ratio: .5"></span>
                            {:else if !apiStore.accessible}
								<a class="uk-link-muted" uk-tooltip="Connection to database could not be established.">Play
									quiz</a>
                            {:else if playableQuizzesStore.available}
								<a on:click={() => dispatchPageUpdate('play')}>Play quiz</a>
                            {:else if !playableQuizzesStore.available}
								<a class="uk-link-muted" uk-tooltip="No playable quizzes found.">Play quiz</a>
                            {/if}
						</li>
					</ul>
				</div>
			</li>
		</ul>
	</div>
</nav>