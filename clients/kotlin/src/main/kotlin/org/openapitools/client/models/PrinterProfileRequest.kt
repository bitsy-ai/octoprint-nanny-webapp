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
 * @param name 
 * @param octoprintKey 
 * @param axesEInverted 
 * @param axesESpeed 
 * @param axesXSpeed 
 * @param axesXInverted 
 * @param axesYInverted 
 * @param axesYSpeed 
 * @param axesZInverted 
 * @param axesZSpeed 
 * @param extruderCount 
 * @param extruderNozzleDiameter 
 * @param extruderSharedNozzle 
 * @param heatedBed 
 * @param heatedChamber 
 * @param model 
 * @param volumeCustomBox 
 * @param volumeDepth 
 * @param volumeFormfactor 
 * @param volumeHeight 
 * @param volumeOrigin 
 * @param volumeWidth 
 */

data class PrinterProfileRequest (
    @Json(name = "octoprint_device")
    val octoprintDevice: kotlin.Int,
    @Json(name = "name")
    val name: kotlin.String,
    @Json(name = "octoprint_key")
    val octoprintKey: kotlin.String,
    @Json(name = "axes_e_inverted")
    val axesEInverted: kotlin.Boolean? = null,
    @Json(name = "axes_e_speed")
    val axesESpeed: kotlin.Int? = null,
    @Json(name = "axes_x_speed")
    val axesXSpeed: kotlin.Int? = null,
    @Json(name = "axes_x_inverted")
    val axesXInverted: kotlin.Boolean? = null,
    @Json(name = "axes_y_inverted")
    val axesYInverted: kotlin.Boolean? = null,
    @Json(name = "axes_y_speed")
    val axesYSpeed: kotlin.Int? = null,
    @Json(name = "axes_z_inverted")
    val axesZInverted: kotlin.Boolean? = null,
    @Json(name = "axes_z_speed")
    val axesZSpeed: kotlin.Int? = null,
    @Json(name = "extruder_count")
    val extruderCount: kotlin.Int? = null,
    @Json(name = "extruder_nozzle_diameter")
    val extruderNozzleDiameter: kotlin.Float? = null,
    @Json(name = "extruder_shared_nozzle")
    val extruderSharedNozzle: kotlin.Boolean? = null,
    @Json(name = "heated_bed")
    val heatedBed: kotlin.Boolean? = null,
    @Json(name = "heated_chamber")
    val heatedChamber: kotlin.Boolean? = null,
    @Json(name = "model")
    val model: kotlin.String? = null,
    @Json(name = "volume_custom_box")
    val volumeCustomBox: kotlin.collections.Map<kotlin.String, AnyType>? = null,
    @Json(name = "volume_depth")
    val volumeDepth: kotlin.Float? = null,
    @Json(name = "volume_formfactor")
    val volumeFormfactor: kotlin.String? = null,
    @Json(name = "volume_height")
    val volumeHeight: kotlin.Float? = null,
    @Json(name = "volume_origin")
    val volumeOrigin: kotlin.String? = null,
    @Json(name = "volume_width")
    val volumeWidth: kotlin.Float? = null
) : Serializable {
    companion object {
        private const val serialVersionUID: Long = 123
    }

}
