package ch.smes.pihoot.models

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
class Game(
        @Id
        var id: String? = null,
        var quiz: Quiz? = null,
        var state: GameState = GameState.QUEUING,
        var colorCode: List<AnswerColor> = listOf(),
        var players: MutableList<Player> = mutableListOf()
)