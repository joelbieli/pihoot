<script>
	import {apiUrl, playableQuizzes, playableQuizzesAvailable, animationConfig} from '../stores.js';
	import {onDestroy, createEventDispatcher} from 'svelte';
	import {fade, fly} from 'svelte/transition';
	import {passByVal} from '../util.js'
	import PlayableQuizHint from '../util/PlayableQuizHint.svelte';

	const dispatch = createEventDispatcher();
	let connectionSuccessful = false;
	let animationConf;
	let apiUrlStore;
	let quizzes = '';
	let editedQuizzes = '';
	let unidenticalQuizzes = [];

	$: {
		if (editedQuizzes !== '' && editedQuizzes.length > 0) {
			editedQuizzes.forEach((quiz, i) => {
				unidenticalQuizzes[i] = JSON.stringify(quiz) !== JSON.stringify(quizzes[i]);
			});
		}
	}

	const init = () => {
		fetch(`${apiUrlStore}quiz`, {
			method: 'GET',
			mode: 'cors'
		}).then(res => {
			connectionSuccessful = true;
			return res.json();
		}).then(data => {
					resetQuizData(data);
				}
		).catch(res => {
			// Do Nothing.
		});

		onDestroy(() => {
			unsubscribeApiUrl();
			unsubscribeAnimationConf();
		});

		fetch(`${apiUrlStore}quiz`, {
			method: 'GET',
			mode: 'cors'
		})
				.then(res => res.json())
				.then(data => playableQuizzes.set({
					available: playableQuizzesAvailable(data),
					requestAttempted: true
				}))
				.catch(playableQuizzes.set({
					available: false,
					requestAttempted: true
				}));
	};

	const unsubscribeApiUrl = apiUrl.subscribe(value => apiUrlStore = value);
	const unsubscribeAnimationConf = animationConfig.subscribe(value => animationConf = value);

	init();

	function resetQuizData(data) {
		editedQuizzes = passByVal(data);
		quizzes = passByVal(data);
	}

	function createQuiz() {
		performRequest(requestMethods.POST, `${apiUrlStore}quiz`, result => {
					updateEditedQuizzes();
					displayNotification(
							'Successfully added a quiz.',
							notificationStatus.SUCCESS,
							notificationPosition.BOTTOM_LEFT);
				}, () => displayNotification(
				'Failed to add quiz to the database.',
				notificationStatus.DANGER,
				notificationPosition.BOTTOM_LEFT),
				_ => {
				},
				{
					"title": "",
					"description": ""
				});
	}

	function updateQuiz(quiz) {
		performRequest(requestMethods.PUT, `${apiUrlStore}quiz/${quiz.id}`, result => {
					displayNotification(
							'Successfully saved changes to quiz.',
							notificationStatus.SUCCESS,
							notificationPosition.BOTTOM_LEFT);
					return result.json();
				}, _ => displayNotification(
				'Failed to save changes to the database.',
				notificationStatus.DANGER,
				notificationPosition.BOTTOM_LEFT),
				data => {
					updateEditedQuiz(quiz.id, data);
					performRequest(
							requestMethods.GET,
							`${apiUrlStore}quiz`,
							result => result.json(),
							() => console.error('Failed to update playAbleQuizzes.'),
							data => playableQuizzes.set({
								available: playableQuizzesAvailable(data),
								requestAttempted: true
							}));
				}, quiz
		);
	}

	function undoQuizChanges(quiz) {
		editedQuizzes.forEach((quizItem, i) => {
			if (quizItem.id === quiz.id) {
				editedQuizzes[i] = passByVal(quizzes[i]);
			}
		});
	}

	function deleteQuiz(quizId) {
		performRequest(
				requestMethods.DELETE,
				`${apiUrlStore}quiz/${quizId}`,
				_ => {
					updateEditedQuizzes();
					displayNotification(
							'Quiz successfully deleted from database.',
							notificationStatus.SUCCESS,
							notificationPosition.BOTTOM_LEFT);
					performRequest(
							requestMethods.GET,
							`${apiUrlStore}quiz`,
							result => result.json(),
							() => console.error('Failed to update playAbleQuizzes.'),
							data => playableQuizzes.set({
								available: playableQuizzesAvailable(data),
								requestAttempted: true
							}));
				},
				() => displayNotification(
						'Failed to delete quiz from the database.',
						notificationStatus.DANGER,
						notificationPosition.BOTTOM_LEFT));
	}

	function createQuestion(quizId) {
		editedQuizzes.forEach((quiz, i, quizzes) => {
			if (quiz.id == quizId) {
				editedQuizzes[i].questions = passByVal([...quizzes[i].questions, {
					"question": "",
					"answers": [
						{
							"answer": "",
							"correct": false
						},
						{
							"answer": "",
							"correct": false
						},
						{
							"answer": "",
							"correct": false
						},
						{
							"answer": "",
							"correct": false
						}
					]
				}]);
			}
		});
	}

	function deleteQuestion(quizId, questionIndex) {
		editedQuizzes.forEach((quiz, i) => {
			if (quiz.id == quizId) {
				editedQuizzes[i].questions = passByVal(editedQuizzes[i].questions).filter((quiz, i) => i !== questionIndex);
			}
		});
	}

	function negateAnswerBool(quizId, questionIndex, answerIndex) {
		editedQuizzes.forEach((quiz, i) => {
			if (quiz.id === quizId) {
				quiz.questions[questionIndex].answers[answerIndex].correct = passByVal(!editedQuizzes[i].questions[questionIndex].answers[answerIndex].correct);
				// Force UI update by reassigning root object.
				editedQuizzes = editedQuizzes;
			}
		});
	}

	function updateEditedQuizzes(data = []) {
		if (data.length !== 0) {
			resetQuizData(data);
		} else {
			performRequest(
					requestMethods.GET,
					`${apiUrlStore}quiz`,
					result => result.json(),
					() => console.error('Failed to update edited quizzes.'),
					requestData => resetQuizData(requestData)
			);
		}
	}

	function updateEditedQuiz(quizId, data = []) {
		performRequest(requestMethods.GET, `${apiUrlStore}quiz`, result =>
						result.json(), () => displayNotification(
				'Failed to update quizzes.',
				notificationStatus.DANGER,
				notificationPosition.BOTTOM_LEFT), data => {
					data.forEach((quiz, i) => {
						if (quiz.id === quizId) {
							editedQuizzes[i] = passByVal(quiz);
							quizzes[i] = passByVal(quiz);
						}
					});
				}
		);
	}

	function performRequest(methodEnum, url, callback1, catchClause, callback2 = () => {
	}, data = {}) {
		let method;

		switch (methodEnum) {
			case requestMethods.GET:
				method = 'GET';
				break;
			case requestMethods.PUT:
				method = 'PUT';
				break;
			case requestMethods.POST:
				method = 'POST';
				break;
			case requestMethods.DELETE:
				method = 'DELETE';
				break;
			default:
				console.error('Unknown request method type!')
		}

		if (methodEnum === requestMethods.GET) {
			fetch(url, {
				method: method,
				mode: 'cors'
			}).then(res => callback1(res)).then(data => callback2(data));
		} else if (methodEnum === requestMethods.DELETE) {
			fetch(url, {
				method: method,
				mode: 'cors'
			}).then(res => callback1(res));
		} else if (methodEnum === requestMethods.POST || methodEnum === requestMethods.PUT) {
			fetch(url, {
				method: method,
				mode: 'cors',
				headers: {
					'Content-Type': 'application/JSON'
				},
				body: JSON.stringify(data)
			}).then(res => callback1(res)).then(res2 => callback2(res2));
		}
	}

	function displayNotification(message, statusEnum, positionEnum, timeout = 1000) {
		let status;
		let position;

		switch (statusEnum) {
			case notificationStatus.PRIMARY:
				status = 'primary';
				break;
			case notificationStatus.SUCCESS:
				status = 'success';
				break;
			case notificationStatus.WARNING:
				status = 'warning';
				break;
			case notificationStatus.DANGER:
				status = 'danger';
				break;
			default:
				console.error('Unknown status type!')
		}
		switch (positionEnum) {
			case notificationPosition.TOP_LEFT:
				position = 'top-left';
				break;
			case notificationPosition.TOP_CENTER:
				position = 'top-center';
				break;
			case notificationPosition.TOP_RIGHT:
				position = 'top-right';
				break;
			case notificationPosition.BOTTOM_LEFT:
				position = 'bottom-left';
				break;
			case notificationPosition.BOTTOM_CENTER:
				position = 'bottom-center';
				break;
			case notificationPosition.BOTTOM_RIGHT:
				position = 'bottom-right';
				break;
			default:
				console.error('Unknown position type!')
		}

		UIkit.notification({
			message,
			status,
			pos: position,
			timeout
		});
	}

	const notificationStatus = {
		PRIMARY: 1,
		SUCCESS: 2,
		WARNING: 3,
		DANGER: 4
	};
	const notificationPosition = {
		TOP_LEFT: 1,
		TOP_CENTER: 2,
		TOP_RIGHT: 3,
		BOTTOM_LEFT: 4,
		BOTTOM_CENTER: 5,
		BOTTOM_RIGHT: 6
	};
	const requestMethods = {
		GET: 1,
		PUT: 2,
		POST: 3,
		DELETE: 4
	};
</script>

<style>
	.flip-icon {
		-moz-transform: scale(-1, 1);
		-webkit-transform: scale(-1, 1);
		-o-transform: scale(-1, 1);
		-ms-transform: scale(-1, 1);
		transform: scale(-1, 1);
	}
</style>

<div class="uk-container uk-container-small">
	<button on:click={createQuiz} class="uk-button uk-button-default uk-border-rounded" uk-tooltip="Add quiz">
		<span class="uk-margin-small-top uk-margin-small-bottom" uk-icon="plus"></span>
	</button>

	<PlayableQuizHint animationY={animationConf.y} animationDuration={animationConf.duration}/>

	<div class="uk-card uk-card-default uk-card-body uk-border-rounded uk-margin">
		<ul class="uk-border" uk-accordion>
            {#each editedQuizzes as quiz, i}
				<li transition:fly="{{ y: -animationConf.y, duration: animationConf.duration }}">
					<a class="uk-accordion-title">
                        {quiz.title !== '' ? quiz.title : "No Title"}
                        {#if unidenticalQuizzes[i]}
							<span class="uk-text-small uk-text-warning uk-text-right">Unsaved Changes</span>
                        {/if}
					</a>
					<div class="uk-accordion-content">
						<div>
							<div class="uk-grid-collapse" uk-grid>
								<div class="uk-width-expand">
									<div class="uk-margin-small">
										<input bind:value={quiz.title} class="uk-input uk-form-large uk-border-rounded"
										       type="text"
										       placeholder="Quiz title">
									</div>
									<div class="uk-margin-small">
										<input bind:value={quiz.description} class="uk-input uk-border-rounded"
										       type="text"
										       placeholder="Description">
									</div>
								</div>
								<div class="uk-width-auto">
									<div class="uk-grid-small uk-margin-small-left" uk-grid>
										<div class="uk-width-auto">
											<button on:click={() => deleteQuiz(quiz.id)} uk-tooltip="Delete quiz"
											        class="uk-button uk-button-default uk-border-rounded">
                                            <span class="uk-text-danger uk-margin-small-top uk-margin-small-bottom"
                                                  uk-icon="trash"></span>
											</button>
											<br>
											<button on:click={() => undoQuizChanges(quiz)} uk-tooltip="Undo changes"
											        class="uk-button uk-button-default uk-border-rounded uk-margin-small">
                                            <span class="uk-margin-small-top flip-icon"
                                                  uk-icon="refresh"></span>
											</button>
										</div>
										<div class="uk-width-auto">
											<button on:click={() => updateQuiz(quiz)} uk-tooltip="Save quiz changes"
											        class="uk-button uk-button-default uk-border-rounded">
                                            <span class="uk-text-success uk-margin-small-top uk-margin-small-bottom"
                                                  uk-icon="check"></span>
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
						<hr>
						<div class="uk-margin-medium-top">
                            {#each quiz.questions as question, j}
								<div class="uk-margin"
								     transition:fly="{{ y: -animationY, duration: animationDuration }}">
									<div class="uk-margin uk-inline uk-width-1-1">
										<a on:click={() => deleteQuestion(quiz.id, j)}
										   class="uk-form-icon uk-text-danger uk-form-icon-flip"
										   uk-icon="icon: trash"></a>
										<input bind:value={question.question} class="uk-input uk-border-rounded"
										       type="text"
										       placeholder="Question">
									</div>
									<div class="uk-grid-small" uk-grid>
                                        {#each question.answers as answer, k}
											<div class="uk-width-1-2">
												<div class="uk-inline uk-width-1-1">
                                                    {#if answer.correct}
														<a on:click={() => negateAnswerBool(quiz.id, j, k)}
														   class="uk-form-icon uk-text-success uk-form-icon-flip"
														   uk-icon="icon: check"
														   transition:fade="{{ duration: animationDuration }}"></a>
                                                    {:else}
														<a on:click={() => negateAnswerBool(quiz.id, j, k)}
														   class="uk-form-icon uk-text-danger uk-form-icon-flip"
														   uk-icon="icon: close"
														   transition:fade="{{ duration: animationDuration }}"></a>
                                                    {/if}
													<input bind:value={answer.answer} class="uk-input uk-border-rounded"
													       type="text"
													       placeholder="Answer">
												</div>
											</div>
                                        {/each}
									</div>
								</div>
                            {/each}
						</div>

						<div class="uk-text-center">
							<button on:click={() => createQuestion(quiz.id)}
							        class="uk-button uk-button-default uk-border-rounded"
							        uk-tooltip="Add question">
                                    <span class="uk-margin-small-top uk-margin-small-bottom"
                                          uk-icon="plus"></span>
							</button>
						</div>
					</div>
				</li>
            {:else}
                {#if connectionSuccessful}
					<div class="uk-alert-primary"
					     transition:fly="{{ y: -animationConf.y, duration: animationConf.duration }}"
					     uk-alert>
						<p>You have not created any quizzes yet. To start, click the <code class="uk-alert-primary">ADD
							QUIZ</code> button.</p>
					</div>
                {:else}
					<div class="uk-alert-danger" uk-alert>
						<p>No connection could be established with the server. Please try again later.</p>
					</div>
                {/if}
            {/each}
		</ul>
	</div>
</div>