
# TelemetryEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventType** | [**TelemetryEventEventTypeEnum**](TelemetryEventEventTypeEnum.md) |  | 
**octoprintEnvironment** | [**OctoprintEnvironment**](OctoprintEnvironment.md) |  | 
**octoprintPrinterData** | [**OctoprintPrinterData**](OctoprintPrinterData.md) |  | 
**printNannyPluginVersion** | **kotlin.String** |  | 
**printNannyClientVersion** | **kotlin.String** |  | 
**octoprintVersion** | **kotlin.String** |  | 
**octoprintDevice** | **kotlin.Int** |  | 
**id** | **kotlin.Int** |  |  [optional] [readonly]
**ts** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] [readonly]
**eventSource** | [**EventSourceEnum**](EventSourceEnum.md) |  |  [optional] [readonly]
**eventData** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**temperature** | [**kotlin.collections.Map&lt;kotlin.String, AnyType&gt;**](AnyType.md) |  |  [optional]
**polymorphicCtype** | **kotlin.Int** |  |  [optional] [readonly]
**user** | **kotlin.Int** |  |  [optional] [readonly]
**printSession** | **kotlin.Int** |  |  [optional]



