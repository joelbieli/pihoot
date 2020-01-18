package ch.smes.pihoot.exceptions

import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.ResponseStatus
import java.lang.RuntimeException

/**
 * When this exception is thrown, the it returns a HTTP response with the error code 400
 */
@ResponseStatus(value = HttpStatus.BAD_REQUEST)
class BadRequestException(message: String): RuntimeException(message) {
}