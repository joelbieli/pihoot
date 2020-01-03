package ch.smes.pihoot.mappers

import ch.smes.pihoot.dtos.QuizDTO
import ch.smes.pihoot.models.Quiz
import org.mapstruct.Mapper

@Mapper(componentModel = "spring")
interface QuizMapper {
    fun toDto(model: Quiz): QuizDTO
    fun toModel(dto: QuizDTO): Quiz
}