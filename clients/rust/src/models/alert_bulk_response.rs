/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */

/// AlertBulkResponse : Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct AlertBulkResponse {
    #[serde(rename = "received")]
    pub received: i32,
    #[serde(rename = "updated")]
    pub updated: i32,
}

impl AlertBulkResponse {
    /// Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    pub fn new(received: i32, updated: i32) -> AlertBulkResponse {
        AlertBulkResponse {
            received,
            updated,
        }
    }
}


