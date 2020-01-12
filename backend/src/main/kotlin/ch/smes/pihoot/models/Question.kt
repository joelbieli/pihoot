package ch.smes.pihoot.models

class Question(
        var id: String? = null,
        var question: String? = null,
        var state: QuestionState? = null,
        var answers: MutableList<Answer> = mutableListOf()
)