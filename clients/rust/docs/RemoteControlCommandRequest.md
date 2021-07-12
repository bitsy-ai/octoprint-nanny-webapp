# RemoteControlCommandRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | [**crate::models::CommandEnum**](CommandEnum.md) |  | 
**user** | **i32** |  | 
**device** | **i32** |  | 
**received** | Option<**bool**> |  | [optional]
**success** | Option<**bool**> |  | [optional]
**iotcore_response** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]
**metadata** | Option<[**::std::collections::HashMap<String, serde_json::Value>**](serde_json::Value.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

