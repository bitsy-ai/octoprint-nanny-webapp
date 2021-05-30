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
 * @param completion 
 * @param filepos 
 * @param printTime 
 * @param printTimeLeft 
 * @param printTimeOrigin 
 */

data class OctoprintProgress (
    @Json(name = "completion")
    val completion: kotlin.Float?,
    @Json(name = "filepos")
    val filepos: kotlin.Int?,
    @Json(name = "printTime")
    val printTime: kotlin.Int?,
    @Json(name = "printTimeLeft")
    val printTimeLeft: kotlin.Int?,
    @Json(name = "printTimeOrigin")
    val printTimeOrigin: kotlin.String?
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}

