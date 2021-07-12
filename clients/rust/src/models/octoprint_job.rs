/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct OctoprintJob {
    #[serde(rename = "file")]
    pub file: Option<Box<crate::models::OctoprintFile>>,
    #[serde(rename = "estimatedPrintTime", skip_serializing_if = "Option::is_none")]
    pub estimated_print_time: Option<f32>,
    #[serde(rename = "averagePrintTime", skip_serializing_if = "Option::is_none")]
    pub average_print_time: Option<f32>,
    #[serde(rename = "lastPrintTime", skip_serializing_if = "Option::is_none")]
    pub last_print_time: Option<f32>,
    #[serde(rename = "filament")]
    pub filament: Option<::std::collections::HashMap<String, serde_json::Value>>,
}

impl OctoprintJob {
    pub fn new(file: Option<crate::models::OctoprintFile>, filament: Option<::std::collections::HashMap<String, serde_json::Value>>) -> OctoprintJob {
        OctoprintJob {
            file: Box::new(file),
            estimated_print_time: None,
            average_print_time: None,
            last_print_time: None,
            filament,
        }
    }
}

