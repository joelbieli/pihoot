package ch.smes.pihoot.repositories

import ch.smes.pihoot.models.Game
import ch.smes.pihoot.models.GameState
import org.springframework.data.mongodb.repository.MongoRepository

interface GameRepository : MongoRepository<Game, String> {

    fun findAllByStateIs(state: GameState): List<Game>
}