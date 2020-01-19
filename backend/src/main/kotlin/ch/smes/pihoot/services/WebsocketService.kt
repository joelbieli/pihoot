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

    /**
     * Notify the frontend about a new player
     */
    fun updatePlayersForGame(gameId: String) {
        simpMessagingTemplate.convertAndSend("/ws/game/$gameId/players", gameService.getPlayersOfGame(gameId).map { playerMapper.toDto(it) })
    }

    /**
     * Notify the frontend about a new answer
     */
    fun updateAnswerCountForGame(gameId: String, answerCount: Int) {
        simpMessagingTemplate.convertAndSend("/ws/game/$gameId/answers", answerCount)
    }
}