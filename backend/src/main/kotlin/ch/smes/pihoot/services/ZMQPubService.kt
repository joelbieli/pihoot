package ch.smes.pihoot.services

import ch.smes.pihoot.models.AnswerColor
import com.fasterxml.jackson.databind.ObjectMapper
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.SmartLifecycle
import org.springframework.core.env.Environment
import org.springframework.stereotype.Service
import org.zeromq.SocketType
import org.zeromq.ZMQ

@Service
class ZMQPubService : SmartLifecycle {

    @Autowired
    private lateinit var environment: Environment

    @Autowired
    private lateinit var gameService: GameService

    private val logger = LoggerFactory.getLogger(this::class.java)

    private val objectMapper: ObjectMapper = ObjectMapper()

    private lateinit var publisher: ZMQ.Socket

    private var isRunning: Boolean = false

    /**
     * Notify the Raspberry Pis when a new game was created an is queuing
     */
    fun updateQueueingGames() {
        publisher.sendMore("queueingGames")
        publisher.send(objectMapper.writeValueAsString(gameService.getQueueingGames().map {
            object { // Create a new object with only the id and color code
                val id = it.id
                val colorCode = it.colorCode
            }
        }))
    }

    /**
     * Notify the Raspberry Pis when a question has begun and it can start accepting and sending answers
     */
    fun beginQuestion(gameId: String, answerColors: List<AnswerColor>) {
        publisher.sendMore("beginQuestion/$gameId")
        publisher.send(objectMapper.writeValueAsString(answerColors))
    }

    /**
     * Notify the Raspberry Pis when a question has ended and it can stop accepting and sending answers
     */
    fun endQuestion(gameId: String) {
        publisher.send("endQuestion/$gameId")
    }

    override fun isRunning(): Boolean = isRunning

    /**
     * This is run when the application starts
     *
     * It creates a publisher socket and runs it in a new daemon thread
     */
    override fun start() {
        if (!isRunning) {
            val port = environment.getProperty("zmq.publisher.port", "5563")
            val context = ZMQ.context(1)
            publisher = context.socket(SocketType.PUB)

            val thread = Thread {
                publisher.bind("tcp://*:$port")
                isRunning = true
                logger.info("ZMQ publisher listening on port $port")
            }

            thread.isDaemon = true
            thread.start()
        }
    }


    override fun stop() {
        if (isRunning) {
            publisher.close()

            isRunning = false
        }

    }
}