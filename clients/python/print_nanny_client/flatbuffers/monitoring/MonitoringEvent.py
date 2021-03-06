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
    def EventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # MonitoringEvent
    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.monitoring.Image import Image
            obj = Image()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MonitoringEvent
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.monitoring.Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MonitoringEvent
    def BoundingBoxes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.monitoring.BoundingBoxes import BoundingBoxes
            obj = BoundingBoxes()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MonitoringEventStart(builder): builder.StartObject(4)
def MonitoringEventAddEventType(builder, eventType): builder.PrependUint8Slot(0, eventType, 0)
def MonitoringEventAddImage(builder, image): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(image), 0)
def MonitoringEventAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def MonitoringEventAddBoundingBoxes(builder, boundingBoxes): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(boundingBoxes), 0)
def MonitoringEventEnd(builder): return builder.EndObject()

import print_nanny_client.flatbuffers.monitoring.BoundingBoxes
import print_nanny_client.flatbuffers.monitoring.Image
import print_nanny_client.flatbuffers.monitoring.Metadata
try:
    from typing import Optional
except:
    pass

class MonitoringEventT(object):

    # MonitoringEventT
    def __init__(self):
        self.eventType = 0  # type: int
        self.image = None  # type: Optional[print_nanny_client.flatbuffers.monitoring.Image.ImageT]
        self.metadata = None  # type: Optional[print_nanny_client.flatbuffers.monitoring.Metadata.MetadataT]
        self.boundingBoxes = None  # type: Optional[print_nanny_client.flatbuffers.monitoring.BoundingBoxes.BoundingBoxesT]

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
        self.eventType = monitoringEvent.EventType()
        if monitoringEvent.Image() is not None:
            self.image = print_nanny_client.flatbuffers.monitoring.Image.ImageT.InitFromObj(monitoringEvent.Image())
        if monitoringEvent.Metadata() is not None:
            self.metadata = print_nanny_client.flatbuffers.monitoring.Metadata.MetadataT.InitFromObj(monitoringEvent.Metadata())
        if monitoringEvent.BoundingBoxes() is not None:
            self.boundingBoxes = print_nanny_client.flatbuffers.monitoring.BoundingBoxes.BoundingBoxesT.InitFromObj(monitoringEvent.BoundingBoxes())

    # MonitoringEventT
    def Pack(self, builder):
        if self.image is not None:
            image = self.image.Pack(builder)
        if self.metadata is not None:
            metadata = self.metadata.Pack(builder)
        if self.boundingBoxes is not None:
            boundingBoxes = self.boundingBoxes.Pack(builder)
        MonitoringEventStart(builder)
        MonitoringEventAddEventType(builder, self.eventType)
        if self.image is not None:
            MonitoringEventAddImage(builder, image)
        if self.metadata is not None:
            MonitoringEventAddMetadata(builder, metadata)
        if self.boundingBoxes is not None:
            MonitoringEventAddBoundingBoxes(builder, boundingBoxes)
        monitoringEvent = MonitoringEventEnd(builder)
        return monitoringEvent
