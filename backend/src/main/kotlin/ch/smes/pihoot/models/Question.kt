package ch.smes.pihoot.models

import java.time.Instant

class Question(
        var id: String? = null,
        var question: String? = null,
        var state: QuestionState? = null,
        var beginTimestamp: Instant? = null,
        var answers: MutableList<Answer> = mutableListOf(),
        var answerCount: Int = 0
)