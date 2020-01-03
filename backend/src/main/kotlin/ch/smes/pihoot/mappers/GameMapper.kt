package ch.smes.pihoot.mappers

import ch.smes.pihoot.dtos.GameDTO
import ch.smes.pihoot.models.Game
import org.mapstruct.Mapper

@Mapper(componentModel = "spring")
interface GameMapper {
    fun toDto(model: Game): GameDTO
    fun toModel(dto: GameDTO): Game
}