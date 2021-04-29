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

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param alertMethod 
 * @param seen 
 * @param octoprintDevice 
 */

data class PatchedAlertRequest (
    @Json(name = "alert_method")
    val alertMethod: AlertMethodEnum? = null,
    @Json(name = "seen")
    val seen: kotlin.Boolean? = null,
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

