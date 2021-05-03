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

import com.print-nanny.client.models.AlertMethodEnum
import com.print-nanny.client.models.EventType92fEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param alertMethod 
 * @param time 
 * @param gcodeFile 
 * @param printProgress 
 * @param timeRemaining 
 * @param manageDeviceUrl 
 * @param user 
 * @param octoprintDevice 
 * @param eventType 
 * @param seen 
 * @param sent 
 * @param createdDt 
 * @param updatedDt 
 */

data class Alert (
    @Json(name = "alert_method")
    val alertMethod: AlertMethodEnum,
    @Json(name = "time")
    val time: kotlin.String? = null,
    @Json(name = "gcode_file")
    val gcodeFile: kotlin.String? = null,
    @Json(name = "print_progress")
    val printProgress: kotlin.String? = null,
    @Json(name = "time_remaining")
    val timeRemaining: kotlin.String? = null,
    @Json(name = "manage_device_url")
    val manageDeviceUrl: kotlin.String? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null,
    @Json(name = "event_type")
    val eventType: EventType92fEnum? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "sent")
    val sent: kotlin.Boolean? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

