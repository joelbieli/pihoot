import {readable, writable} from 'svelte/store';

/**
 * File description:
 * Contains stores and logic to write to stores.
 */

/**
 * A store that knows about the accessibility status to the API.
 */
export const api = writable({
    accessible: false,
    requestAttempted: false
});
/**
 * A store that knows whether playable quizzes are available.
 */
export const playableQuizzes = writable({
    available: false,
    requestAttempted: false
});
/**
 * A store that knows about the address of the backend.
 */
export const apiUrl = writable('http://localhost:8080/api/');
/**
 * A store that knows about animation configurations that should be used globally.
 */
export const animationConfig = readable({
    duration: 200,
    y: 80
}, _ => {
});

let quizEndpointUrl = 'http://localhost:8080/api/quiz';

/**
 * Loads data into the accessibility store when the application is started.
 */
fetch(quizEndpointUrl, {
    method: 'GET',
    mode: 'cors'
})
    .then(res => res.json())
    .then(_ => api.set({
        accessible: true,
        requestAttempted: true
    }))
    .catch(_ => {
        console.error("Failed to fetch quizzes for api accessibility store.");
        api.set({
            accessible: false,
            requestAttempted: true
        });
    });

/**
 * Loads data into the playable quizzes store when the application is started.
 */
fetch(quizEndpointUrl, {
    method: 'GET',
    mode: 'cors'
})
    .then(res => res.json())
    .then(data => playableQuizzes.set({
        available: playableQuizzesAvailable(data),
        requestAttempted: true
    }))
    .catch(_ => {
        console.error("Failed to fetch quizzes for playableQuizzes store.");
        playableQuizzes.set({
            available: false,
            requestAttempted: true
        });
    });

/**
 * Updates the playable quizzes store when called.
 *
 * @global
 *
 * @param {Array} quizzes The quizzes that will be taken into account when updating the playable quizzes store.
 *
 * @return {boolean} Boolean describing the playable quizzes situation.
 */
export function playableQuizzesAvailable(quizzes) {
    let oneValidQuiz = false;
    if (quizzes.length < 1) {
        return false;
    }
    quizzes.forEach(quiz => {
        if (quiz.questions.length > 0) {
            quiz.questions.forEach(question => {
                if (question.answers.length > 1) {
                    question.answers.forEach(answer => {
                        if (answer.correct && answer.answer.length > 0) {
                            oneValidQuiz = true;
                        }
                    });
                }
            });
        }
    });
    return oneValidQuiz;
}
