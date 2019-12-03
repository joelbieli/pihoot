// ----- Utils functions -----

function getQuizAmount() {
	return 1;
	// TODO(laniw): Update with code to fetch amount of quizzes.
}


// ----- Preparation functions -----

function preparePlayButton(playButton) {
	playButton.html('Play quiz');
	if (!getQuizAmount() > 0) {
		playButton.removeClass('uk-button-primary')
			.addClass('uk-button-disabled')
			.css('cursor', 'not-allowed')
			.attr('uk-tooltip', 'Quizzes can\'t be played at this moment.');
	} else {
		playButton.addClass('uk-button-primary')
			.removeClass('uk-button-disabled')
			.css('cursor', 'pointer')
			.removeAttr('uk-tooltip');
	}
}


// ----- Initiation functions -----

function initPlayButton(playButton) {
	playButton
		.html('<div id="play-button-spinner-container" class="uk-text-center"><div id="play-button-spinner" uk-spinner></div></div>');
}