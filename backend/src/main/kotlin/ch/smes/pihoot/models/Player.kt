package ch.smes.pihoot.models

import org.springframework.data.annotation.Id

class Player(
        @Id
        var id: String? = null,
        var color: PlayerColor? = null,
        var socket: Any? = null
)