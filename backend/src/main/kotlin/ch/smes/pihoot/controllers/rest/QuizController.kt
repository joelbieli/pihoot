package ch.smes.pihoot.controllers.rest

import ch.smes.pihoot.dtos.GameDTO
import ch.smes.pihoot.dtos.QuizDTO
import ch.smes.pihoot.mappers.GameMapper
import ch.smes.pihoot.mappers.QuizMapper
import ch.smes.pihoot.services.GameService
import ch.smes.pihoot.services.QuizService
import ch.smes.pihoot.services.WebsocketService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.messaging.simp.SimpMessagingTemplate
import org.springframework.web.bind.annotation.*

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
    private lateinit var websocketService: WebsocketService

    @GetMapping
    fun getAll(): List<QuizDTO> = quizService.getAll().map { quizMapper.toDto(it) }

    @GetMapping("/{id}")
    fun getOne(@PathVariable id: String): QuizDTO = quizMapper.toDto(quizService.getOne(id))

    @PostMapping
    fun create(@RequestBody quizDTO: QuizDTO): QuizDTO = quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))

    @PostMapping("/play/{quizId}")
    fun playQuiz(@PathVariable quizId: String): GameDTO {
        val newGame = gameService.createGame(quizId)

        websocketService.updateQueueingGames()

        return gameMapper.toDto(newGame)
    }

    @PutMapping("/{id}")
    fun update(@PathVariable id: String, @RequestBody quizDTO: QuizDTO): QuizDTO {
        quizDTO.id = id;
        return quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))
    }

    @DeleteMapping("/{id}")
    fun delete(@PathVariable id: String): Unit = quizService.delete(id)
}