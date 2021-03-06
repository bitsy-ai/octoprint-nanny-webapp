/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CommandEnum {
    #[serde(rename = "monitoring_stop")]
    MonitoringStop,
    #[serde(rename = "monitoring_start")]
    MonitoringStart,
    #[serde(rename = "print_start")]
    PrintStart,
    #[serde(rename = "print_stop")]
    PrintStop,
    #[serde(rename = "print_pause")]
    PrintPause,
    #[serde(rename = "print_resume")]
    PrintResume,
    #[serde(rename = "move_nozzle")]
    MoveNozzle,
    #[serde(rename = "connect_test_mqtt_pong")]
    ConnectTestMqttPong,

}

impl ToString for CommandEnum {
    fn to_string(&self) -> String {
        match self {
            Self::MonitoringStop => String::from("monitoring_stop"),
            Self::MonitoringStart => String::from("monitoring_start"),
            Self::PrintStart => String::from("print_start"),
            Self::PrintStop => String::from("print_stop"),
            Self::PrintPause => String::from("print_pause"),
            Self::PrintResume => String::from("print_resume"),
            Self::MoveNozzle => String::from("move_nozzle"),
            Self::ConnectTestMqttPong => String::from("connect_test_mqtt_pong"),
        }
    }
}




