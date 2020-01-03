package ch.smes.pihoot.dtos

class GameDTO(
        var id: String? = null,
        var quiz: QuizDTO? = null,
        var players: MutableList<PlayerDTO> = mutableListOf()
)