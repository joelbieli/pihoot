package ch.smes.pihoot.config

import org.springframework.context.annotation.Configuration
import org.springframework.web.servlet.config.annotation.CorsRegistry
import org.springframework.web.servlet.config.annotation.EnableWebMvc
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer

/**
 * Configuration for web features of Spring
 */
@Configuration
@EnableWebMvc
class WebConfig: WebMvcConfigurer {

    /**
     * Configure CORS to allow requests on any path from any origin with CRUD HTTP methods
     */
    override fun addCorsMappings(registry: CorsRegistry) {
        registry.addMapping("/**")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
    }
}