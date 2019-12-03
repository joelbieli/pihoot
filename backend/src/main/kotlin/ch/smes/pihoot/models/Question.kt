package ch.smes.pihoot.models

import ch.smes.pihoot.models.Answer
import org.springframework.data.annotation.Id

class Question(
        @Id
        var id: String? = null,
        var question: String? = null,
        var answers: MutableList<Answer>? = null
)