package ch.smes.pihoot.models

import ch.smes.pihoot.dtos.Answer
import org.springframework.data.annotation.Id

class Question(
        @Id
        var id: String? = null,
        var question: String,
        var answers: MutableList<Answer>
)