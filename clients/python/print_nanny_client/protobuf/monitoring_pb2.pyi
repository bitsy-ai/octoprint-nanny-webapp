"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MonitoringImage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METADATA_FIELD_NUMBER: builtins.int
    TS_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    ts: builtins.float = ...
    height: builtins.int = ...
    width: builtins.int = ...
    data: builtins.bytes = ...

    @property
    def metadata(self) -> common_pb2.Metadata: ...

    def __init__(self,
        *,
        metadata : typing.Optional[common_pb2.Metadata] = ...,
        ts : builtins.float = ...,
        height : builtins.int = ...,
        width : builtins.int = ...,
        data : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data",u"height",b"height",u"metadata",b"metadata",u"ts",b"ts",u"width",b"width"]) -> None: ...
global___MonitoringImage = MonitoringImage

class Box(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    YMIN_FIELD_NUMBER: builtins.int
    XMIN_FIELD_NUMBER: builtins.int
    YMAX_FIELD_NUMBER: builtins.int
    XMAX_FIELD_NUMBER: builtins.int
    ymin: builtins.float = ...
    xmin: builtins.float = ...
    ymax: builtins.float = ...
    xmax: builtins.float = ...

    def __init__(self,
        *,
        ymin : builtins.float = ...,
        xmin : builtins.float = ...,
        ymax : builtins.float = ...,
        xmax : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"xmax",b"xmax",u"xmin",b"xmin",u"ymax",b"ymax",u"ymin",b"ymin"]) -> None: ...
global___Box = Box

class DeviceCalibration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COORDINATES_FIELD_NUMBER: builtins.int
    MASK_FIELD_NUMBER: builtins.int
    FPS_FIELD_NUMBER: builtins.int
    coordinates: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float] = ...
    mask: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool] = ...
    fps: builtins.float = ...

    def __init__(self,
        *,
        coordinates : typing.Optional[typing.Iterable[builtins.float]] = ...,
        mask : typing.Optional[typing.Iterable[builtins.bool]] = ...,
        fps : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"coordinates",b"coordinates",u"fps",b"fps",u"mask",b"mask"]) -> None: ...
global___DeviceCalibration = DeviceCalibration

class BoxAnnotations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NUM_DETECTIONS_FIELD_NUMBER: builtins.int
    DETECTION_SCORES_FIELD_NUMBER: builtins.int
    DETECTION_CLASSES_FIELD_NUMBER: builtins.int
    DETECTION_BOXES_FIELD_NUMBER: builtins.int
    num_detections: builtins.int = ...
    detection_scores: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float] = ...
    detection_classes: google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int] = ...

    @property
    def detection_boxes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Box]: ...

    def __init__(self,
        *,
        num_detections : builtins.int = ...,
        detection_scores : typing.Optional[typing.Iterable[builtins.float]] = ...,
        detection_classes : typing.Optional[typing.Iterable[builtins.int]] = ...,
        detection_boxes : typing.Optional[typing.Iterable[global___Box]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"detection_boxes",b"detection_boxes",u"detection_classes",b"detection_classes",u"detection_scores",b"detection_scores",u"num_detections",b"num_detections"]) -> None: ...
global___BoxAnnotations = BoxAnnotations

class AnnotatedMonitoringImage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IMAGE_FIELD_NUMBER: builtins.int
    ANNOTATIONS_ALL_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FILTERED_FIELD_NUMBER: builtins.int
    SCORE_THRESHOLD_FIELD_NUMBER: builtins.int
    MIN_CALIBRATION_AREA_OVERLAP_FIELD_NUMBER: builtins.int
    CALIBRATION_FIELD_NUMBER: builtins.int
    score_threshold: builtins.float = ...
    min_calibration_area_overlap: builtins.float = ...

    @property
    def image(self) -> global___MonitoringImage: ...

    @property
    def annotations_all(self) -> global___BoxAnnotations: ...

    @property
    def annotations_filtered(self) -> global___BoxAnnotations: ...

    @property
    def calibration(self) -> global___DeviceCalibration: ...

    def __init__(self,
        *,
        image : typing.Optional[global___MonitoringImage] = ...,
        annotations_all : typing.Optional[global___BoxAnnotations] = ...,
        annotations_filtered : typing.Optional[global___BoxAnnotations] = ...,
        score_threshold : builtins.float = ...,
        min_calibration_area_overlap : builtins.float = ...,
        calibration : typing.Optional[global___DeviceCalibration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"annotations_all",b"annotations_all",u"annotations_filtered",b"annotations_filtered",u"calibration",b"calibration",u"image",b"image"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"annotations_all",b"annotations_all",u"annotations_filtered",b"annotations_filtered",u"calibration",b"calibration",u"image",b"image",u"min_calibration_area_overlap",b"min_calibration_area_overlap",u"score_threshold",b"score_threshold"]) -> None: ...
global___AnnotatedMonitoringImage = AnnotatedMonitoringImage

class AnnotatedMonitoringImagesWindow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _WindowType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WindowType.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        GLOBAL = AnnotatedMonitoringImagesWindow.WindowType.V(0)
        FIXED = AnnotatedMonitoringImagesWindow.WindowType.V(1)
        SLIDING = AnnotatedMonitoringImagesWindow.WindowType.V(2)
        SESSION = AnnotatedMonitoringImagesWindow.WindowType.V(3)
    class WindowType(metaclass=_WindowType):
        V = typing.NewType('V', builtins.int)
    GLOBAL = AnnotatedMonitoringImagesWindow.WindowType.V(0)
    FIXED = AnnotatedMonitoringImagesWindow.WindowType.V(1)
    SLIDING = AnnotatedMonitoringImagesWindow.WindowType.V(2)
    SESSION = AnnotatedMonitoringImagesWindow.WindowType.V(3)

    ANNOTATED_IMAGES_FIELD_NUMBER: builtins.int
    WINDOW_START_FIELD_NUMBER: builtins.int
    WINDOW_END_FIELD_NUMBER: builtins.int
    WINDOW_TYPE_FIELD_NUMBER: builtins.int
    HEALTH_WEIGHT_FIELD_NUMBER: builtins.int
    window_start: builtins.float = ...
    window_end: builtins.float = ...
    window_type: global___AnnotatedMonitoringImagesWindow.WindowType.V = ...
    health_weight: builtins.float = ...

    @property
    def annotated_images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AnnotatedMonitoringImage]: ...

    def __init__(self,
        *,
        annotated_images : typing.Optional[typing.Iterable[global___AnnotatedMonitoringImage]] = ...,
        window_start : builtins.float = ...,
        window_end : builtins.float = ...,
        window_type : global___AnnotatedMonitoringImagesWindow.WindowType.V = ...,
        health_weight : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"annotated_images",b"annotated_images",u"health_weight",b"health_weight",u"window_end",b"window_end",u"window_start",b"window_start",u"window_type",b"window_type"]) -> None: ...
global___AnnotatedMonitoringImagesWindow = AnnotatedMonitoringImagesWindow
