package ch.smes.pihoot.services

import ch.smes.pihoot.models.Question
import ch.smes.pihoot.utils.IdUtils
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class QuestionService {

    @Autowired
    private lateinit var quizService: QuizService

    fun saveOrUpdate(quizId: String, question: Question): Question {
        val quiz = quizService.getOne(quizId)

        if (question.id == null) question.id = IdUtils.generateId()
        question.answers.filter { it.id == null }.forEach { it.id = IdUtils.generateId() }

        quiz.questions.removeIf { it.id == question.id }
        quiz.questions.add(question)

        quizService.saveOrUpdate(quiz)
        return question
    }

    fun delete(quizId: String, questionId: String) {
        val quiz = quizService.getOne(quizId)

        quiz.questions.removeIf { it.id == questionId }

        quizService.saveOrUpdate(quiz)
    }
}