package ch.smes.pihoot.services

import ch.smes.pihoot.exceptions.NotFoundException
import ch.smes.pihoot.models.Quiz
import ch.smes.pihoot.repositories.QuizRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class QuizService {

    @Autowired
    private lateinit var quizRepository: QuizRepository

    fun getOne(quizId: String): Quiz {
        val quiz = quizRepository.findById(quizId)

        if (quiz.isEmpty) {
            throw NotFoundException("Quiz with id $quizId could not be found")
        }

        return quiz.get()
    }

    fun getAll(): List<Quiz> = quizRepository.findAll()

    fun saveOrUpdate(quiz: Quiz) = quizRepository.save(quiz)

    fun delete(quizId: String) = quizRepository.deleteById(quizId)
}