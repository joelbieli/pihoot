<script>
	import Head from './templateComponents/Head.svelte';
	import Navbar from './templateComponents/Navbar.svelte';
	import Title from './templateComponents/Title.svelte';
	import Subtitle from './templateComponents/Subtitle.svelte';
	import Text from './templateComponents/Text.svelte';
	import Home from './Home.svelte';
	import Edit from './edit/Edit.svelte';
	import Play from './play/Play.svelte';
	import Game from './game/Game.svelte';

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
			args: {}
		},
		edit: {
			tabTitle: 'Pihoot Quiz Editor',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Edit your quizzes to lead the battle as game master.'
			],
			page: Edit,
			args: {}
		},
		play: {
			tabTitle: 'Pihoot Play Quiz',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Select a quiz to start a game.'
			],
			page: Play,
			args: {}
		},
		game: {
			tabTitle: 'Play Pihoot',
			pageTitle: 'Pihoot',
			pageSubtitle: 'Welcome to Pihoot - a scam of kahoot.it!',
			texts: [
				'Press play when you\'re ready to commence battle!'
			],
			page: Game,
			args: {}
		}
	};
	const pages = {
		HOME: 1,
		EDIT: 2,
		PLAY: 3,
		GAME: 4
	};
	let currentPage = pages.HOME;
	let currentPageData;
	$: switch (currentPage) {
		case pages.HOME:
			currentPageData = pageData.home;
			break;
		case pages.EDIT:
			currentPageData = pageData.edit;
			break;
		case pages.PLAY:
			currentPageData = pageData.play;
			break;
		case pages.GAME:
			currentPageData = pageData.game;
			break;
		default:
			console.error('Unknown page type!');
	}

	function handlePageUpdate(e) {
		let newCurrentPage;
		switch (e.detail.target) {
			case 'edit':
				newCurrentPage = pages.EDIT;
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
				console.error('Unknown page type!');
		}
		if (newCurrentPage !== currentPage) {
			currentPage = newCurrentPage;
		}
	}
</script>

<Head title={currentPageData.tabTitle}/>

<Navbar on:pageUpdate={handlePageUpdate}/>

<div class="uk-container uk-container-small uk-padding-large">
	<Title title={currentPageData.pageTitle}/>
	<Subtitle subtitle={currentPageData.pageSubtitle}/>
	<hr>
	<Text texts={currentPageData.texts}/>

	<svelte:component this={currentPageData.page} on:pageUpdate={handlePageUpdate}/>
</div>