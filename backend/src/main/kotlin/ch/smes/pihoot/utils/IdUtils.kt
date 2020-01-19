package ch.smes.pihoot.utils

import java.util.*

object IdUtils {

    /**
     * Generate a pseudo random mongodb like id
     */
    fun generateId() = UUID.randomUUID().toString().replace("-", "").take(24)
}