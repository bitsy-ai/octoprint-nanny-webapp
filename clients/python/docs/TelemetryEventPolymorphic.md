# TelemetryEventPolymorphic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**event_type** | [**PrintNannyPluginEventEventTypeEnum**](PrintNannyPluginEventEventTypeEnum.md) |  | 
**octoprint_environment** | **dict(str, object)** |  | 
**octoprint_printer_data** | **dict(str, object)** |  | 
**ts** | **datetime** |  | [optional] [readonly] 
**event_source** | [**EventSourceEnum**](EventSourceEnum.md) |  | [optional] [readonly] 
**event_data** | **dict(str, object)** |  | [optional] 
**temperature** | **dict(str, object)** |  | [optional] 
**print_nanny_plugin_version** | **str** |  | 
**print_nanny_client_version** | **str** |  | 
**octoprint_version** | **str** |  | 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**octoprint_device** | **int** |  | 
**user** | **int** |  | [optional] [readonly] 
**print_session** | **int** |  | [optional] 
**printer_state** | [**PrinterStateEnum**](PrinterStateEnum.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


