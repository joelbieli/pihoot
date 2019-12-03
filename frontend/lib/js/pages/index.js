$(document).ready(function () {
	runPrepFunctions();
});

runInitFunctions();


// ----- Function collection launchers -----

function runInitFunctions() {
	let createButton = $('#create-button');
	let playButton = $('#play-button');
	
	initPlayButton(playButton);
}

function runPrepFunctions() {
	let playButton = $('#play-button');
	
	preparePlayButton(playButton);
}