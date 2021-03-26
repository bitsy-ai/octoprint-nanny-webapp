# automatically generated by the FlatBuffers compiler, do not modify

# namespace: telemetry_event

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Metadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMetadata(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Metadata()
        x.Init(buf, n + offset)
        return x

    # Metadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Metadata
    def UserId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Metadata
    def DeviceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Metadata
    def DeviceCloudiotId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Metadata
    def Ts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Metadata
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Metadata
    def ClientVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Metadata
    def ModelVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Metadata
    def Fpm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def MetadataStart(builder): builder.StartObject(8)
def MetadataAddUserId(builder, userId): builder.PrependUint32Slot(0, userId, 0)
def MetadataAddDeviceId(builder, deviceId): builder.PrependUint32Slot(1, deviceId, 0)
def MetadataAddDeviceCloudiotId(builder, deviceCloudiotId): builder.PrependUint64Slot(2, deviceCloudiotId, 0)
def MetadataAddTs(builder, ts): builder.PrependUint32Slot(3, ts, 0)
def MetadataAddSession(builder, session): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(session), 0)
def MetadataAddClientVersion(builder, clientVersion): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(clientVersion), 0)
def MetadataAddModelVersion(builder, modelVersion): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(modelVersion), 0)
def MetadataAddFpm(builder, fpm): builder.PrependUint8Slot(7, fpm, 0)
def MetadataEnd(builder): return builder.EndObject()


class MetadataT(object):

    # MetadataT
    def __init__(self):
        self.userId = 0  # type: int
        self.deviceId = 0  # type: int
        self.deviceCloudiotId = 0  # type: int
        self.ts = 0  # type: int
        self.session = None  # type: str
        self.clientVersion = None  # type: str
        self.modelVersion = None  # type: str
        self.fpm = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        metadata = Metadata()
        metadata.Init(buf, pos)
        return cls.InitFromObj(metadata)

    @classmethod
    def InitFromObj(cls, metadata):
        x = MetadataT()
        x._UnPack(metadata)
        return x

    # MetadataT
    def _UnPack(self, metadata):
        if metadata is None:
            return
        self.userId = metadata.UserId()
        self.deviceId = metadata.DeviceId()
        self.deviceCloudiotId = metadata.DeviceCloudiotId()
        self.ts = metadata.Ts()
        self.session = metadata.Session()
        self.clientVersion = metadata.ClientVersion()
        self.modelVersion = metadata.ModelVersion()
        self.fpm = metadata.Fpm()

    # MetadataT
    def Pack(self, builder):
        if self.session is not None:
            session = builder.CreateString(self.session)
        if self.clientVersion is not None:
            clientVersion = builder.CreateString(self.clientVersion)
        if self.modelVersion is not None:
            modelVersion = builder.CreateString(self.modelVersion)
        MetadataStart(builder)
        MetadataAddUserId(builder, self.userId)
        MetadataAddDeviceId(builder, self.deviceId)
        MetadataAddDeviceCloudiotId(builder, self.deviceCloudiotId)
        MetadataAddTs(builder, self.ts)
        if self.session is not None:
            MetadataAddSession(builder, session)
        if self.clientVersion is not None:
            MetadataAddClientVersion(builder, clientVersion)
        if self.modelVersion is not None:
            MetadataAddModelVersion(builder, modelVersion)
        MetadataAddFpm(builder, self.fpm)
        metadata = MetadataEnd(builder)
        return metadata
