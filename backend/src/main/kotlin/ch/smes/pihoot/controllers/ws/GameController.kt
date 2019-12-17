package ch.smes.pihoot.controllers.ws

import ch.smes.pihoot.dtos.WSMessage
import ch.smes.pihoot.mappers.PlayerMapper
import ch.smes.pihoot.models.Player
import ch.smes.pihoot.models.PlayerColor
import ch.smes.pihoot.services.GameService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.messaging.handler.annotation.DestinationVariable
import org.springframework.messaging.handler.annotation.Header
import org.springframework.messaging.handler.annotation.MessageMapping
import org.springframework.messaging.simp.SimpMessageHeaderAccessor
import org.springframework.messaging.simp.SimpMessagingTemplate
import org.springframework.stereotype.Controller

@Controller
class GameController {

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var simpMessagingTemplate: SimpMessagingTemplate

    @Autowired
    private lateinit var playerMapper: PlayerMapper

    @MessageMapping("/pi/join/{gameId}")
    fun addPlayer(@DestinationVariable gameId: String, headerAccessor: SimpMessageHeaderAccessor) {
        val sessionId = headerAccessor.sessionAttributes?.get("sessionId").toString()
        val newPlayer = gameService.addPlayer(gameId)

        if (newPlayer != null) {
            simpMessagingTemplate.convertAndSend("/ws/web/players/$gameId", WSMessage(data = playerMapper.toDto(Player("sad", PlayerColor.BLUE))))
            simpMessagingTemplate.convertAndSend("/ws/pi/$sessionId/color", WSMessage(data = newPlayer.color))
        }
    }

}