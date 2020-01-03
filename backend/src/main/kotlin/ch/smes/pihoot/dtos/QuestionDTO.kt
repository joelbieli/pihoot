package ch.smes.pihoot.dtos

class QuestionDTO(
        var id: String? = null,
        var question: String? = null,
        var answers: MutableList<AnswerDTO> = mutableListOf()
)