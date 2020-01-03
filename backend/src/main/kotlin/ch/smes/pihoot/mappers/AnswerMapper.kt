package ch.smes.pihoot.mappers

import ch.smes.pihoot.dtos.AnswerDTO
import ch.smes.pihoot.models.Answer
import org.mapstruct.Mapper

@Mapper(componentModel = "spring")
interface AnswerMapper {
    fun toDto(model: Answer): AnswerDTO
    fun toModel(dto: AnswerDTO): Answer
}