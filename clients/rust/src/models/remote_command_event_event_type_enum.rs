/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum RemoteCommandEventEventTypeEnum {
    #[serde(rename = "remote_command_received")]
    Received,
    #[serde(rename = "remote_command_failed")]
    Failed,
    #[serde(rename = "remote_command_success")]
    Success,

}

impl ToString for RemoteCommandEventEventTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::Received => String::from("remote_command_received"),
            Self::Failed => String::from("remote_command_failed"),
            Self::Success => String::from("remote_command_success"),
        }
    }
}




