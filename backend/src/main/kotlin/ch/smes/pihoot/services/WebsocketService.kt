package ch.smes.pihoot.services

import ch.smes.pihoot.models.AnswerColor
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.messaging.simp.SimpMessagingTemplate
import org.springframework.stereotype.Service
import org.springframework.web.bind.annotation.PathVariable

@Service
class WebsocketService {

    @Autowired
    private lateinit var simpMessagingTemplate: SimpMessagingTemplate

    @Autowired
    private lateinit var gameService: GameService

    fun updatePlayersForGame(gameId: String) {
        simpMessagingTemplate.convertAndSend("/ws/web/players/$gameId", gameService.getPlayersOfGame(gameId))
    }

    fun updateQueueingGames() {
        simpMessagingTemplate.convertAndSend("/ws/pi/games", gameService.getQueueingGames())
    }

    fun beginQuestion(gameId: String, answerColors: List<AnswerColor>) {
        simpMessagingTemplate.convertAndSend("/ws/pi/game/$gameId/question/begin", answerColors)
    }

    fun endQuestion(gameId: String) {
        simpMessagingTemplate.convertAndSend("/ws/pi/game/$gameId/question/begin")
    }
}