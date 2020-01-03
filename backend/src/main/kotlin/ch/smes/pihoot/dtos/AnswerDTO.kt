package ch.smes.pihoot.dtos

import ch.smes.pihoot.models.AnswerColor

class AnswerDTO(
        var id: String? = null,
        var answer: String? = null,
        var color: AnswerColor? = null,
        var isCorrect: Boolean? = null
)