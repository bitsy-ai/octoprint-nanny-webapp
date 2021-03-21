# AlertSettingsPolymorphic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**created_dt** | **datetime** |  | [optional] [readonly] 
**updated_dt** | **datetime** |  | [optional] [readonly] 
**alert_type** | [**AlertTypeEnum**](AlertTypeEnum.md) |  | 
**alert_methods** | [**list[AlertMethodsEnum]**](AlertMethodsEnum.md) |  | [optional] 
**enabled** | **bool** | Enable or disable this alert channel | [optional] 
**polymorphic_ctype** | **int** |  | [optional] [readonly] 
**snapshot** | [**list[SnapshotEnum]**](SnapshotEnum.md) | Fires on web camera &lt;strong&gt;Snapshot&lt;/strong&gt; command | [optional] 
**monitoring_stop** | [**list[MonitoringStopEnum]**](MonitoringStopEnum.md) | Fires on &lt;strong&gt;MonitoringStop&lt;strong&gt; updates.   Helps debug unexpected Print Nanny crashes. | [optional] 
**monitoring_start** | [**list[MonitoringStartEnum]**](MonitoringStartEnum.md) | Fires on &lt;strong&gt;MonitoringStop&lt;/strong&gt; updates. Helpful if you want to confirm monitoring started without a problem. | [optional] 
**print_start** | [**list[PrintStartEnum]**](PrintStartEnum.md) | Fires on &lt;strong&gt;StopPrint&lt;/strong&gt; updates. Get notified as soon as a print job finishes.  | [optional] 
**print_stop** | [**list[PrintStopEnum]**](PrintStopEnum.md) | Fires on &lt;strong&gt;PrintStart&lt;/strong&gt; command status changes. Helpful for verifying a print job started without a problem. | [optional] 
**print_pause** | [**list[PrintPauseEnum]**](PrintPauseEnum.md) | Fires on &lt;strong&gt;PausePrint&lt;/strong&gt; command status changes. Helpful for verifying a print was paused successfully. | [optional] 
**print_resume** | [**list[PrintResumeEnum]**](PrintResumeEnum.md) | Fires on &lt;strong&gt;ResumePrint&lt;/strong&gt; command status changes Helpful for verifying a print was resumed. | [optional] 
**move_nozzle** | [**list[MoveNozzleEnum]**](MoveNozzleEnum.md) | Fires on &lt;strong&gt;MoveNozzle&lt;/strong&gt;command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint | [optional] 
**user** | **int** |  | [optional] [readonly] 
**session** | **str** |  | 
**on_progress_percent** | **int** | Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


