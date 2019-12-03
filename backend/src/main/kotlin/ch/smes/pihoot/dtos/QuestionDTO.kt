package ch.smes.pihoot.dtos

class QuestionDTO(
        var id: String? = null,
        var question: String,
        var answers: MutableList<AnswerDTO>
)