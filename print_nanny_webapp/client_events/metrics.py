import prometheus_client
from .models import PrintJob


print_job_status = prometheus_client.Enum(
    'print_job_status',
    'Last seen status of a print job',
    states=PrintJob.StatusChoices.values
)

predict_frames_per_minute = prometheus_client.Summary(
    'predict_events_per_minute',
    'Raw number of events seen. Calculated via schedule_active_jobs_analysis() periodic runs'
)

detections_per_minute = prometheus_client.Summary(
    'detections_per_minute',
    'Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run',
    ['label']
)

detections_per_frame = prometheus_client.Summary(
    'detections_per_frame',
    'Number of detections above confidence threshold. Calculated via schedule_active_jobs_analysis() periodic run',
    ['label']   
)

detections_confidence_per_label = prometheus_client.Summary(
    'confidence_per_label',
    'Raw confidence score per detection per label',
    ['label']
)

detections_failure_ratio = prometheus_client.Summary(
    'detections_failure_ratio',
    'Num detected failure / num detected neutral frames',
)