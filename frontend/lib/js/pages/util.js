// ----- Utils functions -----

function getQuizAmount() {
	return 1;
	// TODO(laniw): Update with code to fetch amount of quizzes.
}


// ----- Initiation functions -----

function initPlayButton(playButton, playButtonMessage) {
	playButton.html('Play quiz');
	if (getQuizAmount() > 0) {
		playButton.addClass('uk-button-primary')
			.removeClass('uk-button-disabled')
			.css('cursor', 'pointer')
			.removeAttr('uk-tooltip');
	} else {
		playButton.removeClass('uk-button-primary')
			.addClass('uk-button-disabled')
			.css('cursor', 'not-allowed')
			.attr('uk-tooltip', 'Quizzes can\'t be played at this moment.');
		playButtonMessage.html('There don\'t seem to to be any quizzes you can play at the moment. Please create some quizzes to play them.');
	}
}