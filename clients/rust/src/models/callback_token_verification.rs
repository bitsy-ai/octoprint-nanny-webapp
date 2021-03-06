/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */

/// CallbackTokenVerification : Takes a user and a token, verifies the token belongs to the user and validates the alias that the token was sent from.



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct CallbackTokenVerification {
    #[serde(rename = "email", skip_serializing_if = "Option::is_none")]
    pub email: Option<String>,
    #[serde(rename = "mobile", skip_serializing_if = "Option::is_none")]
    pub mobile: Option<String>,
    #[serde(rename = "token")]
    pub token: String,
}

impl CallbackTokenVerification {
    /// Takes a user and a token, verifies the token belongs to the user and validates the alias that the token was sent from.
    pub fn new(token: String) -> CallbackTokenVerification {
        CallbackTokenVerification {
            email: None,
            mobile: None,
            token,
        }
    }
}


