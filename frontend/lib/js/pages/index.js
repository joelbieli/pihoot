$(document).ready(function () {
	runInitFunctions();
});


// ----- Function collection launchers -----

function runInitFunctions() {
	let playButton = $('#play-button');
	let playButtonMessage = $('#play-button-message');
	
	initPlayButton(playButton, playButtonMessage);
}