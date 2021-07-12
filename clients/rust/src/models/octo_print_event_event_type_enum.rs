/*
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum OctoPrintEventEventTypeEnum {
    #[serde(rename = "ClientAuthed")]
    ClientAuthed,
    #[serde(rename = "ClientClosed")]
    ClientClosed,
    #[serde(rename = "ClientDeauthed")]
    ClientDeauthed,
    #[serde(rename = "ClientOpened")]
    ClientOpened,
    #[serde(rename = "SettingsUpdated")]
    SettingsUpdated,
    #[serde(rename = "UserLoggedIn")]
    UserLoggedIn,
    #[serde(rename = "UserLoggedOut")]
    UserLoggedOut,
    #[serde(rename = "FileAdded")]
    FileAdded,
    #[serde(rename = "FileRemoved")]
    FileRemoved,
    #[serde(rename = "FolderAdded")]
    FolderAdded,
    #[serde(rename = "FolderRemoved")]
    FolderRemoved,
    #[serde(rename = "TransferDone")]
    TransferDone,
    #[serde(rename = "TransferFailed")]
    TransferFailed,
    #[serde(rename = "TransferStarted")]
    TransferStarted,
    #[serde(rename = "UpdatedFiles")]
    UpdatedFiles,
    #[serde(rename = "Upload")]
    Upload,
    #[serde(rename = "CaptureDone")]
    CaptureDone,
    #[serde(rename = "CaptureFailed")]
    CaptureFailed,
    #[serde(rename = "CaptureStart")]
    CaptureStart,
    #[serde(rename = "MovieDone")]
    MovieDone,
    #[serde(rename = "MovieFailed")]
    MovieFailed,
    #[serde(rename = "MovieRendering")]
    MovieRendering,
    #[serde(rename = "PostRollEnd")]
    PostRollEnd,
    #[serde(rename = "PostRollStart")]
    PostRollStart,
    #[serde(rename = "SlicingCancelled")]
    SlicingCancelled,
    #[serde(rename = "SlicingDone")]
    SlicingDone,
    #[serde(rename = "SlicingFailed")]
    SlicingFailed,
    #[serde(rename = "SlicingProfileAdded")]
    SlicingProfileAdded,
    #[serde(rename = "SlicingProfileDeleted")]
    SlicingProfileDeleted,
    #[serde(rename = "SlicingProfileModified")]
    SlicingProfileModified,
    #[serde(rename = "SlicingStarted")]
    SlicingStarted,
    #[serde(rename = "PrinterProfileAdded")]
    PrinterProfileAdded,
    #[serde(rename = "PrinterProfileDeleted")]
    PrinterProfileDeleted,
    #[serde(rename = "PrinterProfileModified")]
    PrinterProfileModified,
    #[serde(rename = "PrintProgress")]
    PrintProgress,
    #[serde(rename = "plugin_pi_support_throttle_state")]
    PluginPiSupportThrottleState,
    #[serde(rename = "Shutdown")]
    Shutdown,
    #[serde(rename = "Startup")]
    Startup,

}

impl ToString for OctoPrintEventEventTypeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::ClientAuthed => String::from("ClientAuthed"),
            Self::ClientClosed => String::from("ClientClosed"),
            Self::ClientDeauthed => String::from("ClientDeauthed"),
            Self::ClientOpened => String::from("ClientOpened"),
            Self::SettingsUpdated => String::from("SettingsUpdated"),
            Self::UserLoggedIn => String::from("UserLoggedIn"),
            Self::UserLoggedOut => String::from("UserLoggedOut"),
            Self::FileAdded => String::from("FileAdded"),
            Self::FileRemoved => String::from("FileRemoved"),
            Self::FolderAdded => String::from("FolderAdded"),
            Self::FolderRemoved => String::from("FolderRemoved"),
            Self::TransferDone => String::from("TransferDone"),
            Self::TransferFailed => String::from("TransferFailed"),
            Self::TransferStarted => String::from("TransferStarted"),
            Self::UpdatedFiles => String::from("UpdatedFiles"),
            Self::Upload => String::from("Upload"),
            Self::CaptureDone => String::from("CaptureDone"),
            Self::CaptureFailed => String::from("CaptureFailed"),
            Self::CaptureStart => String::from("CaptureStart"),
            Self::MovieDone => String::from("MovieDone"),
            Self::MovieFailed => String::from("MovieFailed"),
            Self::MovieRendering => String::from("MovieRendering"),
            Self::PostRollEnd => String::from("PostRollEnd"),
            Self::PostRollStart => String::from("PostRollStart"),
            Self::SlicingCancelled => String::from("SlicingCancelled"),
            Self::SlicingDone => String::from("SlicingDone"),
            Self::SlicingFailed => String::from("SlicingFailed"),
            Self::SlicingProfileAdded => String::from("SlicingProfileAdded"),
            Self::SlicingProfileDeleted => String::from("SlicingProfileDeleted"),
            Self::SlicingProfileModified => String::from("SlicingProfileModified"),
            Self::SlicingStarted => String::from("SlicingStarted"),
            Self::PrinterProfileAdded => String::from("PrinterProfileAdded"),
            Self::PrinterProfileDeleted => String::from("PrinterProfileDeleted"),
            Self::PrinterProfileModified => String::from("PrinterProfileModified"),
            Self::PrintProgress => String::from("PrintProgress"),
            Self::PluginPiSupportThrottleState => String::from("plugin_pi_support_throttle_state"),
            Self::Shutdown => String::from("Shutdown"),
            Self::Startup => String::from("Startup"),
        }
    }
}



