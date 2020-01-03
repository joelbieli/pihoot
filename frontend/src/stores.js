import {writable} from 'svelte/store';

export const api = writable({
    accessible: false,
    requestAttempted: false
});
export const playableQuizzes = writable({
    available: false,
    requestAttempted: false
});
export const apiUrl = writable('http://localhost:8091/api/');

let quizEndpointUrl = 'http://localhost:8091/api/quiz';

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

export function playableQuizzesAvailable(quizzes) {
    let oneValidQuiz = false;
    if (quizzes.length < 1) {
        return false;
    }
    console.log("func", quizzes);
    quizzes.forEach(quiz => {
        if (quiz.questions.length > 0) {
            quiz.questions.forEach(question => {
                if (question.answers.length > 1) {
                    question.answers.forEach(question => {
                        if (question.correct) {
                            oneValidQuiz = true;
                        }
                    });
                }
            });
        }
    });
    return oneValidQuiz;
}
