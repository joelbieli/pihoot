package ch.smes.pihoot.repositories

import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.models.Game
import org.springframework.data.mongodb.repository.MongoRepository
import java.util.*

interface GameRepository: MongoRepository<Game, String> {

    fun findByColorCode(colorCode: List<AnswerColor>): Optional<Game>
}