# automatically generated by the FlatBuffers compiler, do not modify

# namespace: monitoring

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MonitoringEvent(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonitoringEvent(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MonitoringEvent()
        x.Init(buf, n + offset)
        return x

    # MonitoringEvent
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MonitoringEvent
    def EventDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # MonitoringEvent
    def EventData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # MonitoringEvent
    def EventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # MonitoringEvent
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.monitoring.Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MonitoringEventStart(builder): builder.StartObject(4)
def MonitoringEventAddEventDataType(builder, eventDataType): builder.PrependUint8Slot(0, eventDataType, 0)
def MonitoringEventAddEventData(builder, eventData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(eventData), 0)
def MonitoringEventAddEventType(builder, eventType): builder.PrependUint8Slot(2, eventType, 0)
def MonitoringEventAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def MonitoringEventEnd(builder): return builder.EndObject()

import print_nanny_client.flatbuffers.monitoring.EventData
import print_nanny_client.flatbuffers.monitoring.Metadata
import print_nanny_client.flatbuffers.monitoring.MonitoringFrame
try:
    from typing import Optional, Union
except:
    pass

class MonitoringEventT(object):

    # MonitoringEventT
    def __init__(self):
        self.eventDataType = 0  # type: int
        self.eventData = None  # type: Union[None, print_nanny_client.flatbuffers.monitoring.MonitoringFrame.MonitoringFrameT]
        self.eventType = 0  # type: int
        self.metadata = None  # type: Optional[print_nanny_client.flatbuffers.monitoring.Metadata.MetadataT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        monitoringEvent = MonitoringEvent()
        monitoringEvent.Init(buf, pos)
        return cls.InitFromObj(monitoringEvent)

    @classmethod
    def InitFromObj(cls, monitoringEvent):
        x = MonitoringEventT()
        x._UnPack(monitoringEvent)
        return x

    # MonitoringEventT
    def _UnPack(self, monitoringEvent):
        if monitoringEvent is None:
            return
        self.eventDataType = monitoringEvent.EventDataType()
        self.eventData = print_nanny_client.flatbuffers.monitoring.EventData.EventDataCreator(self.eventDataType, monitoringEvent.EventData())
        self.eventType = monitoringEvent.EventType()
        if monitoringEvent.Metadata() is not None:
            self.metadata = print_nanny_client.flatbuffers.monitoring.Metadata.MetadataT.InitFromObj(monitoringEvent.Metadata())

    # MonitoringEventT
    def Pack(self, builder):
        if self.eventData is not None:
            eventData = self.eventData.Pack(builder)
        if self.metadata is not None:
            metadata = self.metadata.Pack(builder)
        MonitoringEventStart(builder)
        MonitoringEventAddEventDataType(builder, self.eventDataType)
        if self.eventData is not None:
            MonitoringEventAddEventData(builder, eventData)
        MonitoringEventAddEventType(builder, self.eventType)
        if self.metadata is not None:
            MonitoringEventAddMetadata(builder, metadata)
        monitoringEvent = MonitoringEventEnd(builder)
        return monitoringEvent
