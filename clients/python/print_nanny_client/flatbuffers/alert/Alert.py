# automatically generated by the FlatBuffers compiler, do not modify

# namespace: alert

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Alert(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAlert(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Alert()
        x.Init(buf, n + offset)
        return x

    # Alert
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Alert
    def EventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Alert
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.alert.Metadata import Metadata
            obj = Metadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Alert
    def AnnotatedVideo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.alert.AnnotatedVideo import AnnotatedVideo
            obj = AnnotatedVideo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def AlertStart(builder): builder.StartObject(3)
def AlertAddEventType(builder, eventType): builder.PrependUint8Slot(0, eventType, 0)
def AlertAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def AlertAddAnnotatedVideo(builder, annotatedVideo): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(annotatedVideo), 0)
def AlertEnd(builder): return builder.EndObject()

import print_nanny_client.flatbuffers.alert.AnnotatedVideo
import print_nanny_client.flatbuffers.alert.Metadata
try:
    from typing import Optional
except:
    pass

class AlertT(object):

    # AlertT
    def __init__(self):
        self.eventType = 0  # type: int
        self.metadata = None  # type: Optional[print_nanny_client.flatbuffers.alert.Metadata.MetadataT]
        self.annotatedVideo = None  # type: Optional[print_nanny_client.flatbuffers.alert.AnnotatedVideo.AnnotatedVideoT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        alert = Alert()
        alert.Init(buf, pos)
        return cls.InitFromObj(alert)

    @classmethod
    def InitFromObj(cls, alert):
        x = AlertT()
        x._UnPack(alert)
        return x

    # AlertT
    def _UnPack(self, alert):
        if alert is None:
            return
        self.eventType = alert.EventType()
        if alert.Metadata() is not None:
            self.metadata = print_nanny_client.flatbuffers.alert.Metadata.MetadataT.InitFromObj(alert.Metadata())
        if alert.AnnotatedVideo() is not None:
            self.annotatedVideo = print_nanny_client.flatbuffers.alert.AnnotatedVideo.AnnotatedVideoT.InitFromObj(alert.AnnotatedVideo())

    # AlertT
    def Pack(self, builder):
        if self.metadata is not None:
            metadata = self.metadata.Pack(builder)
        if self.annotatedVideo is not None:
            annotatedVideo = self.annotatedVideo.Pack(builder)
        AlertStart(builder)
        AlertAddEventType(builder, self.eventType)
        if self.metadata is not None:
            AlertAddMetadata(builder, metadata)
        if self.annotatedVideo is not None:
            AlertAddAnnotatedVideo(builder, annotatedVideo)
        alert = AlertEnd(builder)
        return alert
