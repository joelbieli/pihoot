package ch.smes.pihoot.controllers

import ch.smes.pihoot.dtos.QuestionDTO
import ch.smes.pihoot.mappers.QuestionMapper
import ch.smes.pihoot.services.QuestionService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@CrossOrigin
@RestController
@RequestMapping("/api/question")
class QuestionController {

    @Autowired
    private lateinit var questionService: QuestionService

    @Autowired
    private lateinit var questionMapper: QuestionMapper

    @PostMapping("/{quizId}")
    fun create(@PathVariable quizId: String, @RequestBody questionDTO: QuestionDTO): QuestionDTO {
        return questionMapper.toDto(questionService.saveOrUpdate(quizId, questionMapper.toModel(questionDTO)))
    }


    @PutMapping("/{quizId}/{id}")
    fun update(@PathVariable quizId: String, @PathVariable id: String, @RequestBody questionDTO: QuestionDTO): QuestionDTO {
        questionDTO.id = id
        return questionMapper.toDto(questionService.saveOrUpdate(quizId, questionMapper.toModel(questionDTO)))
    }

    @DeleteMapping("/{quizId}/{id}")
    fun delete(@PathVariable quizId: String, @PathVariable id: String): Unit = questionService.delete(quizId, id)
}