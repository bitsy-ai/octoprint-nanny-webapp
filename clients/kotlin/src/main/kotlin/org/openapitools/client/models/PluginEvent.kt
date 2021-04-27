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
import org.openapitools.client.models.PluginEventEventTypeEnum

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param device 
 * @param pluginVersion 
 * @param clientVersion 
 * @param octoprintVersion 
 * @param eventType 
 * @param id 
 * @param createdDt 
 * @param eventData 
 * @param user 
 * @param url 
 */

data class PluginEvent (
    @Json(name = "device")
    val device: kotlin.Int,
    @Json(name = "plugin_version")
    val pluginVersion: kotlin.String,
    @Json(name = "client_version")
    val clientVersion: kotlin.String,
    @Json(name = "octoprint_version")
    val octoprintVersion: kotlin.String,
    @Json(name = "event_type")
    val eventType: PluginEventEventTypeEnum,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "event_data")
    val eventData: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "user")
    val user: kotlin.Int? = null,
    @Json(name = "url")
    val url: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

