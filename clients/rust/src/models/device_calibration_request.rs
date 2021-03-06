/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct DeviceCalibrationRequest {
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "fps", skip_serializing_if = "Option::is_none")]
    pub fps: Option<f32>,
    #[serde(rename = "xy", skip_serializing_if = "Option::is_none")]
    pub xy: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "height", skip_serializing_if = "Option::is_none")]
    pub height: Option<i32>,
    #[serde(rename = "width", skip_serializing_if = "Option::is_none")]
    pub width: Option<i32>,
}

impl DeviceCalibrationRequest {
    pub fn new(octoprint_device: i32) -> DeviceCalibrationRequest {
        DeviceCalibrationRequest {
            octoprint_device,
            fps: None,
            xy: None,
            height: None,
            width: None,
        }
    }
}


