package ch.smes.pihoot.models

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
class Game(
        @Id
        var id: String? = null,
        var quiz: Quiz? = null,
        var players: MutableList<Player>? = null
)