package ch.smes.pihoot

import ch.smes.pihoot.models.QuestionState
import ch.smes.pihoot.services.GameService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean

@SpringBootApplication
class Application {

    @Autowired
    private lateinit var gameService: GameService

    @Bean
    fun runner() = CommandLineRunner {
        gameService.updateQuestionState("5e145f4f75de237bd9c5c446", "8468623edb774d3eaf979d27bb84d768", QuestionState.ENDED)
    }
}

fun main(args: Array<String>) {
    runApplication<Application>(*args)
}
