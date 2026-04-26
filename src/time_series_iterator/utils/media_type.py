from enum import Enum

class MediaType(Enum):
    """
    Media type enum.

    Attributes:
    ----------
    IMAGE: Image
    VIDEO: Video
    AUDIO: Audio
    """
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
