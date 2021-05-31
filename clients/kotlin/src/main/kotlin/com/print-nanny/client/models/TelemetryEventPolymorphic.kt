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

import com.print-nanny.client.models.AnyType
import com.print-nanny.client.models.EventSourceEnum
import com.print-nanny.client.models.OctoPrintEvent
import com.print-nanny.client.models.PrintNannyPluginEvent
import com.print-nanny.client.models.PrintNannyPluginEventEventTypeEnum
import com.print-nanny.client.models.PrintStatusEvent
import com.print-nanny.client.models.PrinterStateEnum
import com.print-nanny.client.models.RemoteCommandEvent
import com.print-nanny.client.models.TelemetryEvent

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param eventType 
 * @param octoprintEnvironment 
 * @param octoprintPrinterData 
 * @param printNannyPluginVersion 
 * @param printNannyClientVersion 
 * @param octoprintVersion 
 * @param octoprintDevice 
 * @param id 
 * @param ts 
 * @param eventSource 
 * @param eventData 
 * @param temperature 
 * @param polymorphicCtype 
 * @param user 
 * @param printSession 
 * @param printerState 
 */

interface TelemetryEventPolymorphic : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

    @Json(name = "event_type")
    val eventType: PrintNannyPluginEventEventTypeEnum
    @Json(name = "octoprint_environment")
    val octoprintEnvironment: kotlin.collections.Map<kotlin.String, AnyType>
    @Json(name = "octoprint_printer_data")
    val octoprintPrinterData: kotlin.collections.Map<kotlin.String, AnyType>
    @Json(name = "print_nanny_plugin_version")
    val printNannyPluginVersion: kotlin.String
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int
    @Json(name = "id")
    val id: kotlin.Int?
    @Json(name = "ts")
    val ts: java.time.OffsetDateTime?
    @Json(name = "event_source")
    val eventSource: EventSourceEnum?
    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, AnyType>?
    @Json(name = "temperature")
    val temperature: kotlin.collections.Map<kotlin.String, AnyType>?
    @Json(name = "polymorphic_ctype")
    val polymorphicCtype: kotlin.Int?
    @Json(name = "user")
    val user: kotlin.Int?
    @Json(name = "print_session")
    val printSession: kotlin.Int?
    @Json(name = "printer_state")
    val printerState: PrinterStateEnum?
}

