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

import com.print-nanny.client.models.PrintSessionRequest

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
 * @param cpuFlags 
 * @param hardware 
 * @param revision 
 * @param virtualenv 
 * @param activeSession 
 */

data class OctoPrintDeviceRequest (
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
    @Json(name = "cpu_flags")
    val cpuFlags: kotlin.collections.List<kotlin.String>? = null,
    @Json(name = "hardware")
    val hardware: kotlin.String? = null,
    @Json(name = "revision")
    val revision: kotlin.String? = null,
    @Json(name = "virtualenv")
    val virtualenv: kotlin.String? = null,
    @Json(name = "active_session")
    val activeSession: PrintSessionRequest? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

