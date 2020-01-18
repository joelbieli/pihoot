package ch.smes.pihoot.controllers

import ch.smes.pihoot.dtos.GameDTO
import ch.smes.pihoot.dtos.QuizDTO
import ch.smes.pihoot.mappers.GameMapper
import ch.smes.pihoot.mappers.QuizMapper
import ch.smes.pihoot.services.GameService
import ch.smes.pihoot.services.QuizService
import ch.smes.pihoot.services.WebsocketService
import ch.smes.pihoot.services.ZMQPubService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

/**
 * Controller for any quiz related HTTP request
 */
@RestController
@RequestMapping("/api/quiz")
class QuizController {

    @Autowired
    private lateinit var quizService: QuizService

    @Autowired
    private lateinit var quizMapper: QuizMapper

    @Autowired
    private lateinit var gameService: GameService

    @Autowired
    private lateinit var gameMapper: GameMapper

    @Autowired
    private lateinit var zmqPubService: ZMQPubService

    /**
     * Get all quizzes
     */
    @GetMapping
    fun getAll(): List<QuizDTO> = quizService.getAll().map { quizMapper.toDto(it) }

    /**
     * Get a specific quiz
     */
    @GetMapping("/{id}")
    fun getOne(@PathVariable id: String): QuizDTO = quizMapper.toDto(quizService.getOne(id))

    /**
     * Create a new quiz
     */
    @PostMapping
    fun create(@RequestBody quizDTO: QuizDTO): QuizDTO = quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))

    /**
     * Play a quiz
     *
     * To create new a game, one must use this endpoint to play a quiz
     */
    @PostMapping("/{quizId}/play")
    fun playQuiz(@PathVariable quizId: String): GameDTO {
        val newGame = gameService.createGame(quizId)

        zmqPubService.updateQueueingGames()

        return gameMapper.toDto(newGame)
    }

    /**
     * Update an existing quiz
     */
    @PutMapping("/{id}")
    fun update(@PathVariable id: String, @RequestBody quizDTO: QuizDTO): QuizDTO {
        quizDTO.id = id;
        return quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))
    }

    /**
     * Delete an existing quiz
     */
    @DeleteMapping("/{id}")
    fun delete(@PathVariable id: String): Unit = quizService.delete(id)
}