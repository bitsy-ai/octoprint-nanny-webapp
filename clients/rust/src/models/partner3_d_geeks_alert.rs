/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */

/// Partner3DGeeksAlert : Do not use underscores in this serializer - linitation of Firebase Cloud Messaging



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct Partner3DGeeksAlert {
    #[serde(rename = "event", skip_serializing_if = "Option::is_none")]
    pub event: Option<String>,
    #[serde(rename = "token", skip_serializing_if = "Option::is_none")]
    pub token: Option<String>,
    #[serde(rename = "printer", skip_serializing_if = "Option::is_none")]
    pub printer: Option<String>,
    #[serde(rename = "print", skip_serializing_if = "Option::is_none")]
    pub print: Option<String>,
    #[serde(rename = "currentTime", skip_serializing_if = "Option::is_none")]
    pub current_time: Option<i32>,
    #[serde(rename = "timeLeft", skip_serializing_if = "Option::is_none")]
    pub time_left: Option<i32>,
    #[serde(rename = "percent", skip_serializing_if = "Option::is_none")]
    pub percent: Option<i32>,
    #[serde(rename = "image", skip_serializing_if = "Option::is_none")]
    pub image: Option<String>,
    #[serde(rename = "action", skip_serializing_if = "Option::is_none")]
    pub action: Option<String>,
}

impl Partner3DGeeksAlert {
    /// Do not use underscores in this serializer - linitation of Firebase Cloud Messaging
    pub fn new() -> Partner3DGeeksAlert {
        Partner3DGeeksAlert {
            event: None,
            token: None,
            printer: None,
            print: None,
            current_time: None,
            time_left: None,
            percent: None,
            image: None,
            action: None,
        }
    }
}

