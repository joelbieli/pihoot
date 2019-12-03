package ch.smes.pihoot.models

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
class Quiz(
        @Id
        var id: String? = null,
        var title: String? = null,
        var description: String? = null,
        var questions: MutableList<Question> = mutableListOf()
)