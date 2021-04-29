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
import com.print-nanny.client.models.EventSubtypeEnum
import com.print-nanny.client.models.OneOfLessThanEventTypeA2eEnumCommaNullEnumGreaterThan

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param annotatedVideo 
 * @param alertMethod 
 * @param eventSubtype 
 * @param printSession 
 * @param createdDt 
 * @param updatedDt 
 * @param eventType 
 * @param user 
 * @param time 
 * @param seen 
 * @param octoprintDevice 
 */

data class PrintStatus (
    @Json(name = "annotated_video")
    val annotatedVideo: java.net.URI,
    @Json(name = "alert_method")
    val alertMethod: AlertMethodEnum,
    @Json(name = "event_subtype")
    val eventSubtype: EventSubtypeEnum,
    @Json(name = "print_session")
    val printSession: kotlin.Int,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "event_type")
    val eventType: OneOfLessThanEventTypeA2eEnumCommaNullEnumGreaterThan? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "time")
    val time: kotlin.String? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}
