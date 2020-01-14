package ch.smes.pihoot.utils

import java.util.*

object IdUtils {

    fun generateId() = UUID.randomUUID().toString().replace("-", "")
}