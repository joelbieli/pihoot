package ch.smes.pihoot.controllers

import ch.smes.pihoot.dtos.QuestionDTO
import ch.smes.pihoot.mappers.QuestionMapper
import ch.smes.pihoot.services.QuestionService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

/**
 * Controller for any question related HTTP request
 */
@RestController
@RequestMapping("/api/quiz/{quizId}/question")
class QuestionController {

    @Autowired
    private lateinit var questionService: QuestionService

    @Autowired
    private lateinit var questionMapper: QuestionMapper

    /**
     * Create a new question for a quiz
     */
    @PostMapping
    fun create(@PathVariable quizId: String, @RequestBody questionDTO: QuestionDTO): QuestionDTO {
        return questionMapper.toDto(questionService.saveOrUpdate(quizId, questionMapper.toModel(questionDTO)))
    }

    /**
     * Update an existing question of a quiz
     */
    @PutMapping("/{id}")
    fun update(@PathVariable quizId: String, @PathVariable id: String, @RequestBody questionDTO: QuestionDTO): QuestionDTO {
        questionDTO.id = id
        return questionMapper.toDto(questionService.saveOrUpdate(quizId, questionMapper.toModel(questionDTO)))
    }
    /**
     * Delete an existing question of a quiz
     */
    @DeleteMapping("/{id}")
    fun delete(@PathVariable quizId: String, @PathVariable id: String): Unit = questionService.delete(quizId, id)
}