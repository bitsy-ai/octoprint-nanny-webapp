# TelemetryEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**print_session** | **str** |  | [optional] [readonly] 
**event_type** | [**TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**octoprint_environment** | [**OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprint_printer_data** | [**OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**ts** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] [readonly] 
**event_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**octoprint_job** | **dict(str, object)** |  | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


