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


import com.squareup.moshi.Json
import java.io.Serializable

/**
 * 
 * @param cores 
 * @param freq 
 * @param ram 
 */

data class OctoprintHardware (
    @Json(name = "cores")
    val cores: kotlin.Int,
    @Json(name = "freq")
    val freq: kotlin.Float,
    @Json(name = "ram")
    val ram: kotlin.Int
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}
