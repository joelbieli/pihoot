package ch.smes.pihoot.repositories

import ch.smes.pihoot.models.Game
import org.springframework.data.mongodb.repository.MongoRepository

interface GameRepository: MongoRepository<Game, String> {
}