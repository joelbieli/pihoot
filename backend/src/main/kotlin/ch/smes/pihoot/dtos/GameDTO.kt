package ch.smes.pihoot.dtos

import ch.smes.pihoot.models.AnswerColor

class GameDTO(
        var id: String? = null,
        var quiz: QuizDTO? = null,
        var players: MutableList<PlayerDTO> = mutableListOf()
        var colorCode: List<AnswerColor> = listOf()
)