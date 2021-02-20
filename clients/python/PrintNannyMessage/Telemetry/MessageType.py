# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Telemetry

class MessageType(object):
    NONE = 0
    MonitoringFrame = 1
    BoundingBoxes = 2


def MessageTypeCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == MessageType().MonitoringFrame:
        import PrintNannyMessage.Telemetry.MonitoringFrame
        return PrintNannyMessage.Telemetry.MonitoringFrame.MonitoringFrameT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == MessageType().BoundingBoxes:
        import PrintNannyMessage.Telemetry.BoundingBoxes
        return PrintNannyMessage.Telemetry.BoundingBoxes.BoundingBoxesT.InitFromBuf(table.Bytes, table.Pos)
    return None
