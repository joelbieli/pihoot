package ch.smes.pihoot.services

import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.mappers.PlayerMapper
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.messaging.simp.SimpMessagingTemplate
import org.springframework.stereotype.Service

@Service
class WebsocketService {

    @Autowired
    private lateinit var simpMessagingTemplate: SimpMessagingTemplate

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var playerMapper: PlayerMapper

    fun updatePlayersForGame(gameId: String) {
        simpMessagingTemplate.convertAndSend("/ws/web/players/$gameId", gameService.getPlayersOfGame(gameId).map { playerMapper.toDto(it) })
    }
}