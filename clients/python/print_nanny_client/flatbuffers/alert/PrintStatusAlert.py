# automatically generated by the FlatBuffers compiler, do not modify

# namespace: alert

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PrintStatusAlert(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPrintStatusAlert(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PrintStatusAlert()
        x.Init(buf, n + offset)
        return x

    # PrintStatusAlert
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PrintStatusAlert
    def EventSubtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # PrintStatusAlert
    def AnnotatedVideo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from print_nanny_client.flatbuffers.alert.AnnotatedVideo import AnnotatedVideo
            obj = AnnotatedVideo()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def PrintStatusAlertStart(builder): builder.StartObject(2)
def PrintStatusAlertAddEventSubtype(builder, eventSubtype): builder.PrependUint8Slot(0, eventSubtype, 0)
def PrintStatusAlertAddAnnotatedVideo(builder, annotatedVideo): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(annotatedVideo), 0)
def PrintStatusAlertEnd(builder): return builder.EndObject()

import print_nanny_client.flatbuffers.alert.AnnotatedVideo
try:
    from typing import Optional
except:
    pass

class PrintStatusAlertT(object):

    # PrintStatusAlertT
    def __init__(self):
        self.eventSubtype = 0  # type: int
        self.annotatedVideo = None  # type: Optional[print_nanny_client.flatbuffers.alert.AnnotatedVideo.AnnotatedVideoT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        printStatusAlert = PrintStatusAlert()
        printStatusAlert.Init(buf, pos)
        return cls.InitFromObj(printStatusAlert)

    @classmethod
    def InitFromObj(cls, printStatusAlert):
        x = PrintStatusAlertT()
        x._UnPack(printStatusAlert)
        return x

    # PrintStatusAlertT
    def _UnPack(self, printStatusAlert):
        if printStatusAlert is None:
            return
        self.eventSubtype = printStatusAlert.EventSubtype()
        if printStatusAlert.AnnotatedVideo() is not None:
            self.annotatedVideo = print_nanny_client.flatbuffers.alert.AnnotatedVideo.AnnotatedVideoT.InitFromObj(printStatusAlert.AnnotatedVideo())

    # PrintStatusAlertT
    def Pack(self, builder):
        if self.annotatedVideo is not None:
            annotatedVideo = self.annotatedVideo.Pack(builder)
        PrintStatusAlertStart(builder)
        PrintStatusAlertAddEventSubtype(builder, self.eventSubtype)
        if self.annotatedVideo is not None:
            PrintStatusAlertAddAnnotatedVideo(builder, annotatedVideo)
        printStatusAlert = PrintStatusAlertEnd(builder)
        return printStatusAlert
