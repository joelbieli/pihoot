<script>
	import Head from './templateComponents/Head.svelte';
	import Navbar from './templateComponents/Navbar.svelte';
	import Title from './templateComponents/Title.svelte';
	import Subtitle from './templateComponents/Subtitle.svelte';
	import Text from './templateComponents/Text.svelte';
	import Home from './Home.svelte';
	import Edit from './edit/Edit.svelte';
	import SelectGame from './play/SelectGame.svelte';
	import Play from './play/Play.svelte';

	let showNavbar = true;
	let showContainer = true;
	let showTitle = true;
	let showSubtitle = true;
	let showDivider = true;
	let showText = true;

	let lastPageUpdateData;

	$: pageData = {
		home: {
			tabTitle: 'Pihoot Home',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Welcome to pihoot. This isn\'t just a remake of kahoot. Here you can access the game not with phones, but with Raspberry Pi\'s and some additional LEDs and buttons! Isn\'t that convenient?',
				'You are now looking at the home page of the game master tool that allows you to create sets of quizzes and launch them to let others fight to their death.'
			],
			page: Home,
			data: {}
		},
		edit: {
			tabTitle: 'Pihoot Quiz Editor',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Edit your quizzes to lead the battle as game master.'
			],
			page: Edit,
			data: {}
		},
		select: {
			tabTitle: 'Pihoot Play Quiz',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Select a quiz to start a game.'
			],
			page: SelectGame,
			data: {}
		},
		play: {
			tabTitle: 'Play Pihoot',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Press play when you\'re ready to commence battle!'
			],
			page: Play,
			data: {}
		}
	};
	const pages = {
		HOME: 1,
		EDIT: 2,
		PLAY: 3,
		SELECT: 4
	};
	let currentPage = pages.HOME;
	let currentPageData;
	$: switch (currentPage) {
		case pages.HOME:
			pageData.home.data = lastPageUpdateData;
			currentPageData = pageData.home;
			break;
		case pages.EDIT:
			pageData.edit.data = lastPageUpdateData;
			currentPageData = pageData.edit;
			break;
		case pages.PLAY:
			pageData.play.data = lastPageUpdateData;
			currentPageData = pageData.play;
			break;
		case pages.SELECT:
			pageData.select.data = lastPageUpdateData;
			currentPageData = pageData.select;
			break;
		default:
			console.error(`Unknown page \'${currentPage}\'.`);
	}

	function handlePageUpdate(e) {
		let newCurrentPage;
		let target;
		if (e.detail.target !== 'undefined') {
			target = e.detail.target;
		} else {
			console.error('Undefined page target.');
			return;
		}
		if (e.detail.data !== 'undefined') {
			lastPageUpdateData = e.detail.data;
		}
		switch (target) {
			case 'edit':
				newCurrentPage = pages.EDIT;
				break;
			case 'select':
				newCurrentPage = pages.SELECT;
				break;
			case 'play':
				newCurrentPage = pages.PLAY;
				break;
			case 'home':
				newCurrentPage = pages.HOME;
				break;
			case 'game':
				newCurrentPage = pages.GAME;
				break;
			default:
				console.error(`Unknown page type \'${target}\'.`);
		}
		if (newCurrentPage !== currentPage) {
			currentPage = newCurrentPage;
		}
	}

	function handleVisibilityChange(e) {
		let visibilities;
		if (e.detail !== 'undefined') {
			visibilities = e.detail;
		} else {
			console.error("Invalid visibility change. Visibilities aren't defined.");
			return;
		}
		showNavbar = visibilities.navbar;
		showContainer = visibilities.container;
		showTitle = visibilities.title;
		showSubtitle = visibilities.subtitle;
		showDivider = visibilities.divider;
		showText = visibilities.text;
	}
</script>

<Head title={currentPageData.tabTitle}/>

{#if showNavbar}
	<Navbar on:pageUpdate={handlePageUpdate}/>
{/if}

{#if showContainer}
	<div class="uk-container uk-container-small uk-margin-large-top uk-margin">
        {#if showTitle}
			<Title title={currentPageData.pageTitle}/>
        {/if}
        {#if showSubtitle}
			<Subtitle subtitle={currentPageData.pageSubtitle}/>
        {/if}
        {#if showDivider}
			<hr>
        {/if}
        {#if showText}
			<Text texts={currentPageData.texts}/>
        {/if}
	</div>
{/if}

<svelte:component this={currentPageData.page} data={currentPageData.data} on:pageUpdate={handlePageUpdate}
                  on:visibilityChange={handleVisibilityChange}/>