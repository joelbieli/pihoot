package ch.smes.pihoot.models

import org.springframework.data.annotation.Id

class Answer(
        @Id
        var id: String? = null,
        var answer: String? = null,
        var color: AnswerColor? = null,
        var isCorrect: Boolean? = null
)