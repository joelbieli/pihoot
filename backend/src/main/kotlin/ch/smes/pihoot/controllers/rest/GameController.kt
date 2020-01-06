package ch.smes.pihoot.controllers.rest

import ch.smes.pihoot.dtos.PlayerDTO
import ch.smes.pihoot.dtos.WSMessage
import ch.smes.pihoot.mappers.PlayerMapper
import ch.smes.pihoot.models.Player
import ch.smes.pihoot.models.PlayerColor
import ch.smes.pihoot.services.GameService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.messaging.simp.SimpMessagingTemplate
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/game")
class GameController {

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var simpMessagingTemplate: SimpMessagingTemplate

    @Autowired
    private lateinit var playerMapper: PlayerMapper

    @PostMapping("/join/{gameId}")
    fun joinGame(@PathVariable gameId: String): PlayerDTO {
        val newPlayer = gameService.addPlayer(gameId)

        simpMessagingTemplate.convertAndSend("/ws/web/players/$gameId", newPlayer)

        return playerMapper.toDto(newPlayer)
    }
}