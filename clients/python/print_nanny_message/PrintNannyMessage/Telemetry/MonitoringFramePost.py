# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Telemetry

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MonitoringFramePost(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonitoringFramePost(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MonitoringFramePost()
        x.Init(buf, n + offset)
        return x

    # MonitoringFramePost
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MonitoringFramePost
    def Ts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MonitoringFramePost
    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from PrintNannyMessage.Telemetry.Image import Image
            obj = Image()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MonitoringFramePost
    def EventType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 2

def MonitoringFramePostStart(builder): builder.StartObject(3)
def MonitoringFramePostAddTs(builder, ts): builder.PrependUint32Slot(0, ts, 0)
def MonitoringFramePostAddImage(builder, image): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(image), 0)
def MonitoringFramePostAddEventType(builder, eventType): builder.PrependInt8Slot(2, eventType, 2)
def MonitoringFramePostEnd(builder): return builder.EndObject()

import PrintNannyMessage.Telemetry.Image
try:
    from typing import Optional
except:
    pass

class MonitoringFramePostT(object):

    # MonitoringFramePostT
    def __init__(self):
        self.ts = 0  # type: int
        self.image = None  # type: Optional[PrintNannyMessage.Telemetry.Image.ImageT]
        self.eventType = 2  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        monitoringFramePost = MonitoringFramePost()
        monitoringFramePost.Init(buf, pos)
        return cls.InitFromObj(monitoringFramePost)

    @classmethod
    def InitFromObj(cls, monitoringFramePost):
        x = MonitoringFramePostT()
        x._UnPack(monitoringFramePost)
        return x

    # MonitoringFramePostT
    def _UnPack(self, monitoringFramePost):
        if monitoringFramePost is None:
            return
        self.ts = monitoringFramePost.Ts()
        if monitoringFramePost.Image() is not None:
            self.image = PrintNannyMessage.Telemetry.Image.ImageT.InitFromObj(monitoringFramePost.Image())
        self.eventType = monitoringFramePost.EventType()

    # MonitoringFramePostT
    def Pack(self, builder):
        if self.image is not None:
            image = self.image.Pack(builder)
        MonitoringFramePostStart(builder)
        MonitoringFramePostAddTs(builder, self.ts)
        if self.image is not None:
            MonitoringFramePostAddImage(builder, image)
        MonitoringFramePostAddEventType(builder, self.eventType)
        monitoringFramePost = MonitoringFramePostEnd(builder)
        return monitoringFramePost
