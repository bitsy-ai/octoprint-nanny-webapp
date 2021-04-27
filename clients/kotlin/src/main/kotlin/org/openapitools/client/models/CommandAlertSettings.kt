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
package org.openapitools.client.models

import org.openapitools.client.models.AlertMethodsEnum
import org.openapitools.client.models.AlertTypeEnum
import org.openapitools.client.models.MoveNozzleEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param alertType 
 * @param id 
 * @param createdDt 
 * @param updatedDt 
 * @param alertMethods 
 * @param enabled Enable or disable this alert channel
 * @param monitoringStop Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.
 * @param monitoringStart Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.
 * @param printStart Fires on <strong>StopPrint</strong> updates. Get notified as soon as a print job finishes. 
 * @param printStop Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.
 * @param printPause Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.
 * @param printResume Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.
 * @param moveNozzle Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint
 * @param polymorphicCtype 
 * @param user 
 */

data class CommandAlertSettings (
    @Json(name = "alert_type")
    val alertType: AlertTypeEnum,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "alert_methods")
    val alertMethods: kotlin.collections.List<AlertMethodsEnum>? = null,
    /* Enable or disable this alert channel */
    @Json(name = "enabled")
    val enabled: kotlin.Boolean? = null,
    /* Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes. */
    @Json(name = "monitoring_stop")
    val monitoringStop: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem. */
    @Json(name = "monitoring_start")
    val monitoringStart: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>StopPrint</strong> updates. Get notified as soon as a print job finishes.  */
    @Json(name = "print_start")
    val printStart: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem. */
    @Json(name = "print_stop")
    val printStop: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully. */
    @Json(name = "print_pause")
    val printPause: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed. */
    @Json(name = "print_resume")
    val printResume: kotlin.collections.List<MoveNozzleEnum>? = null,
    /* Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint */
    @Json(name = "move_nozzle")
    val moveNozzle: kotlin.collections.List<MoveNozzleEnum>? = null,
    @Json(name = "polymorphic_ctype")
    val polymorphicCtype: kotlin.Int? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

