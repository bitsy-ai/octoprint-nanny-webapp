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

import org.openapitools.client.models.AnyType
import org.openapitools.client.models.MonitoringModeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param name 
 * @param model 
 * @param platform 
 * @param serial 
 * @param cores 
 * @param ram 
 * @param pythonVersion 
 * @param pipVersion 
 * @param octoprintVersion 
 * @param pluginVersion 
 * @param printNannyClientVersion 
 * @param id 
 * @param deleted 
 * @param createdDt 
 * @param user 
 * @param lastSession 
 * @param publicKey 
 * @param fingerprint 
 * @param cloudiotDevice 
 * @param cloudiotDeviceName 
 * @param cloudiotDevicePath 
 * @param cloudiotDeviceNumId 
 * @param cpuFlags 
 * @param hardware 
 * @param revision 
 * @param virtualenv 
 * @param monitoringActive 
 * @param monitoringMode 
 * @param cloudiotDeviceConfigs 
 * @param manageUrl 
 */

data class OctoPrintDevice (
    @Json(name = "name")
    val name: kotlin.String,
    @Json(name = "model")
    val model: kotlin.String,
    @Json(name = "platform")
    val platform: kotlin.String,
    @Json(name = "serial")
    val serial: kotlin.String,
    @Json(name = "cores")
    val cores: kotlin.Int,
    @Json(name = "ram")
    val ram: kotlin.Int,
    @Json(name = "python_version")
    val pythonVersion: kotlin.String,
    @Json(name = "pip_version")
    val pipVersion: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "plugin_version")
    val pluginVersion: kotlin.String,
    @Json(name = "print_nanny_client_version")
    val printNannyClientVersion: kotlin.String,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "deleted")
    val deleted: java.time.OffsetDateTime? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "last_session")
    val lastSession: kotlin.Int? = null,
    @Json(name = "public_key")
    val publicKey: kotlin.String? = null,
    @Json(name = "fingerprint")
    val fingerprint: kotlin.String? = null,
    @Json(name = "cloudiot_device")
    val cloudiotDevice: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "cloudiot_device_name")
    val cloudiotDeviceName: kotlin.String? = null,
    @Json(name = "cloudiot_device_path")
    val cloudiotDevicePath: kotlin.String? = null,
    @Json(name = "cloudiot_device_num_id")
    val cloudiotDeviceNumId: kotlin.Int? = null,
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "virtualenv")
    val virtualenv: kotlin.String? = null,
    @Json(name = "monitoring_active")
    val monitoringActive: kotlin.Boolean? = null,
    @Json(name = "monitoring_mode")
    val monitoringMode: MonitoringModeEnum? = null,
    @Json(name = "cloudiot_device_configs")
    val cloudiotDeviceConfigs: kotlin.String? = null,
    @Json(name = "manage_url")
    val manageUrl: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

