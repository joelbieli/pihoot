package ch.smes.pihoot.mappers

import ch.smes.pihoot.dtos.PlayerDTO
import ch.smes.pihoot.models.Player
import org.mapstruct.Mapper

@Mapper(componentModel = "spring")
interface PlayerMapper {
    fun toDto(model: Player): PlayerDTO
    fun toModel(dto: PlayerDTO): Player
}