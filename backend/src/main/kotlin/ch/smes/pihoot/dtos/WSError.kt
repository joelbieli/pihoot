package ch.smes.pihoot.dtos

import org.springframework.http.HttpStatus

class WSError(
        code: HttpStatus,
        message: String
)