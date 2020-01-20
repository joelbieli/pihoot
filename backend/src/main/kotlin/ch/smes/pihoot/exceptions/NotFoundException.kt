package ch.smes.pihoot.exceptions

import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.ResponseStatus
import java.lang.RuntimeException

/**
 * When this exception is thrown, the it returns a HTTP response with the error code 404
 */
@ResponseStatus(value = HttpStatus.NOT_FOUND)
class NotFoundException(message: String): RuntimeException(message) {
}