/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoPrintEventRequest {
    #[serde(rename = "event_type")]
    pub event_type: crate::models::OctoPrintEventEventTypeEnum,
    #[serde(rename = "event_data", skip_serializing_if = "Option::is_none")]
    pub event_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "octoprint_environment", skip_serializing_if = "Option::is_none")]
    pub octoprint_environment: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "octoprint_printer_data", skip_serializing_if = "Option::is_none")]
    pub octoprint_printer_data: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "temperature", skip_serializing_if = "Option::is_none")]
    pub temperature: Option<::std::collections::HashMap<String, serde_json::Value>>,
    #[serde(rename = "print_nanny_plugin_version")]
    pub print_nanny_plugin_version: String,
    #[serde(rename = "print_nanny_client_version")]
    pub print_nanny_client_version: String,
    #[serde(rename = "octoprint_version")]
    pub octoprint_version: String,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: i32,
    #[serde(rename = "print_session", skip_serializing_if = "Option::is_none")]
    pub print_session: Option<i32>,
}

impl OctoPrintEventRequest {
    pub fn new(event_type: crate::models::OctoPrintEventEventTypeEnum, print_nanny_plugin_version: String, print_nanny_client_version: String, octoprint_version: String, octoprint_device: i32) -> OctoPrintEventRequest {
        OctoPrintEventRequest {
            event_type,
            event_data: None,
            octoprint_environment: None,
            octoprint_printer_data: None,
            temperature: None,
            print_nanny_plugin_version,
            print_nanny_client_version,
            octoprint_version,
            octoprint_device,
            print_session: None,
        }
    }
}

