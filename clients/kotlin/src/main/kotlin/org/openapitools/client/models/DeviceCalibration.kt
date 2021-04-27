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

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param octoprintDevice 
 * @param mask 
 * @param id 
 * @param createdDt 
 * @param updatedDt 
 * @param fpm 
 * @param coordinates 
 * @param configFile 
 * @param url 
 */

data class DeviceCalibration (
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "mask")
    val mask: kotlin.collections.List<java.math.BigDecimal>,
    @Json(name = "id")
    val id: kotlin.Int? = null,
    @Json(name = "created_dt")
    val createdDt: java.time.OffsetDateTime? = null,
    @Json(name = "updated_dt")
    val updatedDt: java.time.OffsetDateTime? = null,
    @Json(name = "fpm")
    val fpm: kotlin.Int? = null,
    @Json(name = "coordinates")
    val coordinates: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "config_file")
    val configFile: java.net.URI? = null,
    @Json(name = "url")
    val url: java.net.URI? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

