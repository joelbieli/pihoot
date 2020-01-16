package ch.smes.pihoot

import ch.smes.pihoot.models.AnswerColor
import ch.smes.pihoot.services.ZMQPubService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.CommandLineRunner
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean

@SpringBootApplication
class Application {

    @Autowired
    private lateinit var zmqPublisherService: ZMQPubService

    @Bean
    fun doStuff() = CommandLineRunner {
        Thread.sleep(2000)
        zmqPublisherService.updateQueueingGames()
        Thread.sleep(2000)
        zmqPublisherService.beginQuestion("akdhksa", listOf(AnswerColor.BLUE))
        Thread.sleep(2000)
        zmqPublisherService.endQuestion("akdhksa")
    }
}

fun main(args: Array<String>) {
    runApplication<Application>(*args)
}
