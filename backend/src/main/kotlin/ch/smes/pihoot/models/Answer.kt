package ch.smes.pihoot.models

import org.springframework.data.annotation.Id

class Answer(
        @Id
        var id: String? = null,
        var answer: String,
        var color: AnswerColor,
        var isCorrect: Boolean
)