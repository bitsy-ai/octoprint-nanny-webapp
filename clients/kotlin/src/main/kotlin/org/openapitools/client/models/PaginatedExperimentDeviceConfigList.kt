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

import org.openapitools.client.models.ExperimentDeviceConfig

import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param count 
 * @param next 
 * @param previous 
 * @param results 
 */

data class PaginatedExperimentDeviceConfigList (
    @Json(name = "count")
    val count: kotlin.Int? = null,
    @Json(name = "next")
    val next: java.net.URI? = null,
    @Json(name = "previous")
    val previous: java.net.URI? = null,
    @Json(name = "results")
    val results: kotlin.collections.List<ExperimentDeviceConfig>? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

