
# RemoteCommandEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pluginVersion** | **kotlin.String** |  | 
**clientVersion** | **kotlin.String** |  | 
**octoprintVersion** | **kotlin.String** |  | 
**eventType** | [**RemoteCommandEventEventTypeEnum**](RemoteCommandEventEventTypeEnum.md) |  | 
**octoprintDevice** | **kotlin.Int** |  | 
**id** | **kotlin.Int** |  |  [optional] [readonly]
**createdDt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**eventSource** | [**EventSourceEnum**](EventSourceEnum.md) |  |  [optional]
**eventData** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**metadata** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**octoprintJob** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**polymorphicCtype** | **kotlin.Int** |  |  [optional] [readonly]
**user** | **kotlin.Int** |  |  [optional] [readonly]
**printSession** | **kotlin.Int** |  |  [optional]


