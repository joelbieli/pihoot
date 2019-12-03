package ch.smes.pihoot.dtos

class GameDTO(
        var id: String,
        var quiz: QuizDTO,
        var players: MutableList<PlayerDTO>
)