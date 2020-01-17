package ch.smes.pihoot.services

import ch.smes.pihoot.models.AnswerColor
import com.fasterxml.jackson.databind.ObjectMapper
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.SmartLifecycle
import org.springframework.core.env.Environment
import org.springframework.stereotype.Service
import org.zeromq.SocketType
import org.zeromq.ZContext
import org.zeromq.ZMQ
import javax.annotation.PostConstruct

@Service
class ZMQPubService: SmartLifecycle {

    @Autowired
    private lateinit var environment: Environment

    @Autowired
    private lateinit var gameService: GameService

    private val logger = LoggerFactory.getLogger(this::class.java)

    private val objectMapper: ObjectMapper = ObjectMapper()

    private lateinit var publisher: ZMQ.Socket

    private var isRunning: Boolean = false

    fun updateQueueingGames() {
        publisher.sendMore("queueingGames")
        publisher.send(objectMapper.writeValueAsString(gameService.getQueueingGames().map { object {
            val id = it.id
            val colorCode = it.colorCode
        } }))
    }

    fun beginQuestion(gameId: String, answerColors: List<AnswerColor>) {
        publisher.sendMore("beginQuestion")
        publisher.send(objectMapper.writeValueAsString(answerColors))
    }

    fun endQuestion(gameId: String) {
        publisher.send("endQuestion")
    }

    override fun isRunning(): Boolean = isRunning

    override fun start() {
        if (!isRunning) {
            val port = environment.getProperty("zmq.publisher.port", "5563")
            val context = ZMQ.context(1)
            publisher = context.socket(SocketType.PUB)

            val thread: Thread = Thread {
                publisher.bind("tcp://*:$port")
                isRunning = true
                logger.info("ZMQ puiblisher listening on port $port")
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