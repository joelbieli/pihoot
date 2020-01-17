package ch.smes.pihoot.controllers

import ch.smes.pihoot.dtos.PlayerDTO
import ch.smes.pihoot.mappers.PlayerMapper
import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.models.GameState
import ch.smes.pihoot.models.QuestionState
import ch.smes.pihoot.services.GameService
import ch.smes.pihoot.services.WebsocketService
import ch.smes.pihoot.services.ZMQPubService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/game")
class GameController {

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var websocketService: WebsocketService

    @Autowired
    private lateinit var zmqPubService: ZMQPubService

    @Autowired
    private lateinit var playerMapper: PlayerMapper

    @PostMapping("/start/{gameId}")
    fun startGame(@PathVariable gameId: String) {
        gameService.updateGameState(gameId, GameState.IN_GAME)

        zmqPubService.updateQueueingGames()
    }

    @PostMapping("/end/{gameId}")
    fun endGame(@PathVariable gameId: String) {
        gameService.updateGameState(gameId, GameState.ENDED)
    }

    @PostMapping("/{gameId}/question/{questionId}/begin")
    fun beginQuestion(@PathVariable gameId: String, @PathVariable questionId: String) {
        gameService.updateQuestionState(gameId, questionId, QuestionState.IN_PROGRESS)

        val game = gameService.getOne(gameId)

        zmqPubService.beginQuestion(gameId, game.quiz
                ?.questions
                ?.find { it.id == questionId }
                ?.answers
                ?.map { it.color }
                ?.requireNoNulls()
                .orEmpty())
    }

    @PostMapping("/{gameId}/question/{questionId}/end")
    fun endQuestion(@PathVariable gameId: String, @PathVariable questionId: String) {
        gameService.updateQuestionState(gameId, questionId, QuestionState.ENDED)

        zmqPubService.endQuestion(gameId)
    }

    @PostMapping("/join/{gameId}")
    fun joinGame(@PathVariable gameId: String): PlayerDTO {
        val newPlayer = gameService.addPlayer(gameId)

        websocketService.updatePlayersForGame(gameId)

        return playerMapper.toDto(newPlayer)
    }


    @PostMapping("/{gameId}/answer/{playerId}")
    fun answerQuestion(
            @RequestBody answer: AnswerColor,
            @PathVariable gameId: String,
            @PathVariable playerId: String
    ): Boolean = gameService.checkAnswerAndUpdateScore(gameId, playerId, answer)

    @PostMapping("/{gameId}/score")
    fun getScore(@PathVariable gameId: String): Map<String, Int> = gameService.getScore(gameId)
}