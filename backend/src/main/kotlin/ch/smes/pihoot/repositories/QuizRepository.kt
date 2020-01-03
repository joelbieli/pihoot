package ch.smes.pihoot.repositories

import ch.smes.pihoot.models.Quiz
import org.springframework.data.mongodb.repository.MongoRepository

interface QuizRepository: MongoRepository<Quiz, String> {
}