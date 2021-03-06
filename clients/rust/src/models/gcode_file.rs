/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct GcodeFile {
    #[serde(rename = "id", skip_serializing_if = "Option::is_none")]
    pub id: Option<i32>,
    #[serde(rename = "user", skip_serializing_if = "Option::is_none")]
    pub user: Option<i32>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "file")]
    pub file: String,
    #[serde(rename = "file_hash")]
    pub file_hash: String,
    #[serde(rename = "octoprint_device")]
    pub octoprint_device: String,
    #[serde(rename = "url", skip_serializing_if = "Option::is_none")]
    pub url: Option<String>,
}

impl GcodeFile {
    pub fn new(name: String, file: String, file_hash: String, octoprint_device: String) -> GcodeFile {
        GcodeFile {
            id: None,
            user: None,
            name,
            file,
            file_hash,
            octoprint_device,
            url: None,
        }
    }
}


