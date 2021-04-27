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
import org.openapitools.client.models.AlertRequest
import org.openapitools.client.models.AlertTypeEnum
import org.openapitools.client.models.ManualVideoUploadAlertRequest
import org.openapitools.client.models.PrintSessionAlertAlertSubtypeEnum
import org.openapitools.client.models.PrintSessionAlertRequest
import org.openapitools.client.models.ProgressAlertRequest
import org.openapitools.client.models.RemoteControlCommandAlertRequest

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param alertSubtype 
 * @param alertType 
 * @param color 
 * @param icon 
 * @param description 
 * @param title 
 * @param device 
 * @param annotatedVideo 
 * @param printSession 
 * @param seen 
 * @param alertMethods 
 * @param sent 
 * @param progressPercent Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress
 * @param octoprintDevice 
 * @param needsReview 
 */

interface AlertPolymorphicRequest : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

    @Json(name = "alert_subtype")
    val alertSubtype: PrintSessionAlertAlertSubtypeEnum
    @Json(name = "alert_type")
    val alertType: AlertTypeEnum
    @Json(name = "color")
    val color: kotlin.String
    @Json(name = "icon")
    val icon: kotlin.String
    @Json(name = "description")
    val description: kotlin.String
    @Json(name = "title")
    val title: kotlin.String
    @Json(name = "device")
    val device: kotlin.Int
    @Json(name = "annotated_video")
    val annotatedVideo: java.io.File
    @Json(name = "print_session")
    val printSession: kotlin.Int
    @Json(name = "seen")
    val seen: kotlin.Boolean?
    @Json(name = "alert_methods")
    val alertMethods: kotlin.collections.List<AlertMethodsEnum>?
    @Json(name = "sent")
    val sent: kotlin.Boolean?
    /* Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress */
    @Json(name = "progress_percent")
    val progressPercent: kotlin.Int?
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int?
    @Json(name = "needs_review")
    val needsReview: kotlin.Boolean?
}

