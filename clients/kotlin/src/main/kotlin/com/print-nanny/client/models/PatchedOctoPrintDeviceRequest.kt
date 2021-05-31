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

import com.print-nanny.client.models.MonitoringModeEnum
import com.print-nanny.client.models.MonitoringStatusEnum
import com.print-nanny.client.models.PrintJobStatusEnum
import com.print-nanny.client.models.PrinterStateEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param name 
 * @param lastSession 
 * @param model 
 * @param platform 
 * @param cpuFlags 
 * @param hardware 
 * @param revision 
 * @param serial 
 * @param cores 
 * @param ram 
 * @param pythonVersion 
 * @param pipVersion 
 * @param virtualenv 
 * @param monitoringActive 
 * @param monitoringMode 
 * @param octoprintVersion 
 * @param pluginVersion 
 * @param printNannyClientVersion 
 * @param monitoringStatus 
 * @param printJobStatus 
 * @param printerState 
 */

data class PatchedOctoPrintDeviceRequest (
    @Json(name = "name")
    val name: kotlin.String? = null,
    @Json(name = "last_session")
    val lastSession: kotlin.Int? = null,
    @Json(name = "model")
    val model: kotlin.String? = null,
    @Json(name = "platform")
    val platform: kotlin.String? = null,
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "serial")
    val serial: kotlin.String? = null,
    @Json(name = "cores")
    val cores: kotlin.Int? = null,
    @Json(name = "ram")
    val ram: kotlin.Int? = null,
    @Json(name = "python_version")
    val pythonVersion: kotlin.String? = null,
    @Json(name = "pip_version")
    val pipVersion: kotlin.String? = null,
    @Json(name = "virtualenv")
    val virtualenv: kotlin.String? = null,
    @Json(name = "monitoring_active")
    val monitoringActive: kotlin.Boolean? = null,
    @Json(name = "monitoring_mode")
    val monitoringMode: MonitoringModeEnum? = null,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String? = null,
    @Json(name = "plugin_version")
    val pluginVersion: kotlin.String? = null,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String? = null,
    @Json(name = "monitoring_status")
    val monitoringStatus: MonitoringStatusEnum? = null,
    @Json(name = "print_job_status")
    val printJobStatus: PrintJobStatusEnum? = null,
    @Json(name = "printer_state")
    val printerState: PrinterStateEnum? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

