package ch.smes.pihoot.dtos

class QuizDTO(
        var id: String? = null,
        var title: String? = null,
        var description: String? = null,
        var questions: MutableList<QuestionDTO> = mutableListOf()
)