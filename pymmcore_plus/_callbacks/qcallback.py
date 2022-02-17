import numpy as np
from qtpy.QtCore import QObject, Signal
from useq import MDAEvent, MDASequence


class QCoreCallback(QObject):

    # native MMCore callback events
    propertiesChanged = Signal()
    propertyChanged = Signal(str, str, object)
    channelGroupChanged = Signal(str)
    configGroupChanged = Signal(str, str)
    configSet = Signal(str, str)
    systemConfigurationLoaded = Signal()
    pixelSizeChanged = Signal(float)
    pixelSizeAffineChanged = Signal(float, float, float, float, float, float)
    stagePositionChanged = Signal(str, float)
    XYStagePositionChanged = Signal(str, float, float)
    xYStagePositionChanged = XYStagePositionChanged  # alias
    exposureChanged = Signal(str, float)
    SLMExposureChanged = Signal(str, float)
    sLMExposureChanged = SLMExposureChanged  # alias

    # added for CMMCorePlus
    sequenceStarted = Signal(MDASequence)  # at the start of an MDA sequence
    sequencePauseToggled = Signal(bool)  # when MDA is paused/unpaused
    sequenceCanceled = Signal(MDASequence)  # when mda is canceled
    sequenceFinished = Signal(MDASequence)  # when mda is done (whether canceled or not)
    frameReady = Signal(np.ndarray, MDAEvent)  # after each event in the sequence
    imageSnapped = Signal(np.ndarray)  # after an image is snapped
