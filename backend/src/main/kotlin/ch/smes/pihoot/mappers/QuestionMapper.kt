package ch.smes.pihoot.mappers

import ch.smes.pihoot.dtos.QuestionDTO
import ch.smes.pihoot.models.Question
import org.mapstruct.Mapper

@Mapper(componentModel = "spring")
interface QuestionMapper {
    fun toDto(model: Question): QuestionDTO
    fun toModel(dto: QuestionDTO): Question
}