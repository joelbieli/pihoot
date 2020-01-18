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

    /**
     * Find the quiz with the given id
     */
    fun getOne(quizId: String): Quiz {
        val quiz = quizRepository.findById(quizId)

        if (quiz.isEmpty) {
            // When no quiz with the given id is found, return 404 (not found)
            throw NotFoundException("Quiz with id $quizId could not be found")
        }

        return quiz.get()
    }

    /**
     * Get all quizzes
     */
    fun getAll(): List<Quiz> = quizRepository.findAll()

    /**
     * Save a quiz if it doesn't already exist, otherwise update the existing quiz
     */
    fun saveOrUpdate(quiz: Quiz) = quizRepository.save(quiz)

    /**
     * Delete an existing quiz
     */
    fun delete(quizId: String) = quizRepository.deleteById(quizId)
}