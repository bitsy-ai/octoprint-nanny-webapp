# automatically generated by the FlatBuffers compiler, do not modify

# namespace: TelemetrySchema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TelemetryEvent(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTelemetryEvent(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TelemetryEvent()
        x.Init(buf, n + offset)
        return x

    # TelemetryEvent
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TelemetryEvent
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TelemetryEvent
    def EventDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # TelemetryEvent
    def EventData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # TelemetryEvent
    def EventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # TelemetryEvent
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from PrintNannyEvent.TelemetrySchema.Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def TelemetryEventStart(builder): builder.StartObject(5)
def TelemetryEventAddVersion(builder, version): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)
def TelemetryEventAddEventDataType(builder, eventDataType): builder.PrependUint8Slot(1, eventDataType, 0)
def TelemetryEventAddEventData(builder, eventData): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(eventData), 0)
def TelemetryEventAddEventType(builder, eventType): builder.PrependUint8Slot(3, eventType, 0)
def TelemetryEventAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def TelemetryEventEnd(builder): return builder.EndObject()

import PrintNannyEvent.TelemetrySchema.EventData
import PrintNannyEvent.TelemetrySchema.Metadata
import PrintNannyEvent.TelemetrySchema.MonitoringFrame
try:
    from typing import Optional, Union
except:
    pass

class TelemetryEventT(object):

    # TelemetryEventT
    def __init__(self):
        self.version = None  # type: str
        self.eventDataType = 0  # type: int
        self.eventData = None  # type: Union[None, PrintNannyEvent.TelemetrySchema.MonitoringFrame.MonitoringFrameT]
        self.eventType = 0  # type: int
        self.metadata = None  # type: Optional[PrintNannyEvent.TelemetrySchema.Metadata.MetadataT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        telemetryEvent = TelemetryEvent()
        telemetryEvent.Init(buf, pos)
        return cls.InitFromObj(telemetryEvent)

    @classmethod
    def InitFromObj(cls, telemetryEvent):
        x = TelemetryEventT()
        x._UnPack(telemetryEvent)
        return x

    # TelemetryEventT
    def _UnPack(self, telemetryEvent):
        if telemetryEvent is None:
            return
        self.version = telemetryEvent.Version()
        self.eventDataType = telemetryEvent.EventDataType()
        self.eventData = PrintNannyEvent.TelemetrySchema.EventData.EventDataCreator(self.eventDataType, telemetryEvent.EventData())
        self.eventType = telemetryEvent.EventType()
        if telemetryEvent.Metadata() is not None:
            self.metadata = PrintNannyEvent.TelemetrySchema.Metadata.MetadataT.InitFromObj(telemetryEvent.Metadata())

    # TelemetryEventT
    def Pack(self, builder):
        if self.version is not None:
            version = builder.CreateString(self.version)
        if self.eventData is not None:
            eventData = self.eventData.Pack(builder)
        if self.metadata is not None:
            metadata = self.metadata.Pack(builder)
        TelemetryEventStart(builder)
        if self.version is not None:
            TelemetryEventAddVersion(builder, version)
        TelemetryEventAddEventDataType(builder, self.eventDataType)
        if self.eventData is not None:
            TelemetryEventAddEventData(builder, eventData)
        TelemetryEventAddEventType(builder, self.eventType)
        if self.metadata is not None:
            TelemetryEventAddMetadata(builder, metadata)
        telemetryEvent = TelemetryEventEnd(builder)
        return telemetryEvent
