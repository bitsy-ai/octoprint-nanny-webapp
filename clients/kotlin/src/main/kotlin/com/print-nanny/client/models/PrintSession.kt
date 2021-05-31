/**
* 
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 0.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package com.print-nanny.client.models


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param octoprintDevice 
 * @param session 
 * @param id 
 * @param createdDt 
 * @param updatedDt 
 * @param filepos 
 * @param printProgress 
 * @param timeElapsed 
 * @param timeRemaining 
 * @param user 
 * @param printerProfile 
 * @param gcodeFile 
 * @param gcodeFilename 
 * @param url 
 */

data class PrintSession (
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "session")
    val session: kotlin.String,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "filepos")
    val filepos: kotlin.Int? = null,
    @Json(name = "print_progress")
    val printProgress: kotlin.Int? = null,
    @Json(name = "time_elapsed")
    val timeElapsed: kotlin.Int? = null,
    @Json(name = "time_remaining")
    val timeRemaining: kotlin.Int? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "printer_profile")
    val printerProfile: kotlin.Int? = null,
    @Json(name = "gcode_file")
    val gcodeFile: kotlin.Int? = null,
    @Json(name = "gcode_filename")
    val gcodeFilename: kotlin.String? = null,
    @Json(name = "url")
    val url: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

