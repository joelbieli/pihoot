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

	/**
	 * Dispatches a page update with the given page target.
	 *
	 * @fires pageUpdate
	 *
	 * @param {string} target The page that should be displayed.
	 */
	const dispatchPageUpdate = (target) => dispatch('pageUpdate', {target: target});
</script>

<style>
	/* Overwrites the color and pointer when no playable quizzes are found to remove any hover effects. */
	.disabled-link {
		color: #cdcdcd;
		cursor: default;
	}

	.disabled-link:hover {
		color: #cdcdcd;
	}
</style>

<div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky">
	<nav class="uk-navbar-container" uk-navbar>
		<div class="uk-navbar-left">

			<ul class="uk-navbar-nav">
				<a class="uk-navbar-item uk-logo" on:click={() => dispatchPageUpdate('home')}>
					<img data-src="/lib/images/logo.png" width="120em" alt="Pihoot Logo" uk-img>
				</a>
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
									<a class="uk-link-muted"
									   uk-tooltip="Connection to database could not be established.">Edit
										quiz</a>
                                {/if}
							</li>
							<li>
                                {#if !playableQuizzesStore.requestAttempted}
									<span uk-spinner="ratio: .5"></span>
                                {:else if !apiStore.accessible}
									<a class="uk-disabled"
									   uk-tooltip="Connection to database could not be established.">Play
										quiz</a>
                                {:else if playableQuizzesStore.available}
									<a on:click={() => dispatchPageUpdate('select')}>Play quiz</a>
                                {:else if !playableQuizzesStore.available}
									<a class="disabled-link" uk-tooltip="No playable quizzes found.">Play quiz</a>
                                {/if}
							</li>
						</ul>
					</div>
				</li>
			</ul>
		</div>
	</nav>
</div>