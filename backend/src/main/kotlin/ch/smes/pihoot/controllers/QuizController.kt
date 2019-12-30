package ch.smes.pihoot.controllers

import ch.smes.pihoot.dtos.QuizDTO
import ch.smes.pihoot.mappers.QuizMapper
import ch.smes.pihoot.services.QuizService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/quiz")
class QuizController {

    @Autowired
    private lateinit var quizService: QuizService

    @Autowired
    private lateinit var quizMapper: QuizMapper

    @GetMapping
    fun getAll(): List<QuizDTO> = quizService.getAll().map { quizMapper.toDto(it) }

    @GetMapping("/{id}")
    fun getOne(@PathVariable id: String): QuizDTO = quizMapper.toDto(quizService.getOne(id))

    @PostMapping
    fun create(@RequestBody quizDTO: QuizDTO): QuizDTO = quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))

    @PutMapping("/{id}")
    fun update(@PathVariable id: String, @RequestBody quizDTO: QuizDTO): QuizDTO {
        quizDTO.id = id;
        return quizMapper.toDto(quizService.saveOrUpdate(quizMapper.toModel(quizDTO)))
    }

    @DeleteMapping("/{id}")
    fun delete(@PathVariable id: String): Unit = quizService.delete(id)
}