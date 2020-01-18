package ch.smes.pihoot.config

import org.springframework.context.annotation.Configuration
import org.springframework.messaging.simp.config.MessageBrokerRegistry
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker
import org.springframework.web.socket.config.annotation.StompEndpointRegistry
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer

/**
 * Configuration for websocket features of Spring
 */
@Configuration
@EnableWebSocketMessageBroker
class WebsocketConfig : WebSocketMessageBrokerConfigurer {

    /**
     * Configure prefix for all WS routes
     */
    override fun configureMessageBroker(registry: MessageBrokerRegistry) {
        registry.setApplicationDestinationPrefixes("/ws")
    }

    /**
     * Configure connection endpoint for WS and allow any origin
     */
    override fun registerStompEndpoints(registry: StompEndpointRegistry) {
        registry.addEndpoint("/ws/connect")
                .setAllowedOrigins("*")
    }
}