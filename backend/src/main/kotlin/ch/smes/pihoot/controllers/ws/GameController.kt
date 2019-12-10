package ch.smes.pihoot.controllers.ws

import ch.smes.pihoot.dtos.PlayerDTO
import ch.smes.pihoot.dtos.WSError
import ch.smes.pihoot.dtos.WSMessage
import ch.smes.pihoot.mappers.PlayerMapper
import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.services.GameService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.messaging.handler.annotation.DestinationVariable
import org.springframework.messaging.handler.annotation.MessageMapping
import org.springframework.messaging.handler.annotation.SendTo
import org.springframework.stereotype.Controller

@Controller
class GameController {

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var playerMapper: PlayerMapper

    @MessageMapping("/ws/pi/join")
    @SendTo("/ws/web/players/{gameId}")
    fun addPlayer(colorCode: List<AnswerColor>, @DestinationVariable gameId: String): WSMessage<PlayerDTO> {
        val playerGamePair = gameService.addPlayer(colorCode)

        if (playerGamePair == null) {
            return WSMessage(error = WSError(HttpStatus.NOT_FOUND, "No game with color code found"))
        } else {
            gameId = playerGamePair.second
            return WSMessage(data = playerMapper.toDto(playerGamePair.first))
        }
    }

}