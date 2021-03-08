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

def MetadataStart(builder): builder.StartObject(3)
def MetadataAddUserId(builder, userId): builder.PrependUint32Slot(0, userId, 0)
def MetadataAddDeviceId(builder, deviceId): builder.PrependUint32Slot(1, deviceId, 0)
def MetadataAddDeviceCloudiotId(builder, deviceCloudiotId): builder.PrependUint64Slot(2, deviceCloudiotId, 0)
def MetadataEnd(builder): return builder.EndObject()


class MetadataT(object):

    # MetadataT
    def __init__(self):
        self.userId = 0  # type: int
        self.deviceId = 0  # type: int
        self.deviceCloudiotId = 0  # type: int

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

    # MetadataT
    def Pack(self, builder):
        MetadataStart(builder)
        MetadataAddUserId(builder, self.userId)
        MetadataAddDeviceId(builder, self.deviceId)
        MetadataAddDeviceCloudiotId(builder, self.deviceCloudiotId)
        metadata = MetadataEnd(builder)
        return metadata