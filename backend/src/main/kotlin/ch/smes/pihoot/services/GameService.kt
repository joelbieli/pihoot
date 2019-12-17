package ch.smes.pihoot.services

import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.models.Game
import ch.smes.pihoot.models.Player
import ch.smes.pihoot.models.PlayerColor
import ch.smes.pihoot.repositories.GameRepository
import ch.smes.pihoot.utils.IdUtils
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class GameService {

    @Autowired
    private lateinit var gameRepository: GameRepository

    @Autowired
    private lateinit var quizService: QuizService

    fun createGame(quizId: String) = gameRepository.save(Game(
            quiz = quizService.getOne(quizId),
            colorCode = generateSequence { AnswerColor.values().random() }.take(8).toList()
    ))

    fun addPlayer(gameId: String): Player? {
        val game = gameRepository.findById(gameId)

        if (game.isEmpty) {
            return null
        }

        val newPlayer = Player(
                IdUtils.generateId(),
                PlayerColor.values().filter { game.get().players.any { player -> player.color == it } }.random()
        )

        game.get().players.add(newPlayer)

        gameRepository.save(game.get())

        return newPlayer
    }
}