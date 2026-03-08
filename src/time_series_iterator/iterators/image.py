import cv2
import numpy as np

from id_manager import IDManager
from ..iterator import TimeSeriesIterator
from ..parameters import TimeSeriesIterationParameters
from ..media_type import MediaType


class ImageIterator(TimeSeriesIterator):
    """
    Iterator for image data.

    Attributes:
    ----------
    paths: list[str]
        The paths to the images.
    params: TimeSeriesIterationParameters
        The parameters for the image iterator.
    """
    def __init__(
        self, 
        paths: list[str], 
        params: TimeSeriesIterationParameters
        ):
        super().__init__(
            params=params, 
            paths=paths
            )

        self.file_id_manager = IDManager(
            start=self.params.start_index_on_python, 
            step=self.params.sampling_freq
            )

    def _next_data(self) -> np.ndarray | None:
        """
        Get the next data from the image iterator.

        Returns:
        ----------
        np.ndarray | None: The next data from the image iterator.
        """
        index = self.file_id_manager.get_next_id()
        if index >= len(self.paths):
            return None
        return cv2.imread(self.paths[index])

    def close(self):
        pass

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __len__(self) -> int:
        return len(self.paths)

    @property
    def media_type(self) -> MediaType:
        return MediaType.IMAGE

    def get_image(self, frame_id: int) -> np.ndarray:
        """
        Get the image from the image iterator.

        Parameters:
        ----------
        frame_id: int
            The frame id of the image.

        Returns:
        ----------
        np.ndarray: The image from the image iterator.

        Raises:
        ----------
        ValueError: If the frame id is out of range.
        """
        if frame_id < 0:
            raise ValueError(f"Frame id must be greater than or equal to 0, given: {frame_id}")
        if frame_id >= len(self.paths) + self.params.index_base.value:
            raise ValueError(f"Frame id is out of range, given: {frame_id}, max: {len(self.paths) + self.params.index_base.value - 1}")
        target_index = frame_id-self.params.index_base.value
        image = cv2.imread(self.paths[target_index])
        if image is None:
            raise ValueError(f"Failed to load image from path: {self.paths[target_index]}")
        return image

    def __str__(self) -> str:
        return f"ImageIterator(paths[0]={self.paths[0]}, params={self.params})"

    @property
    def fps(self) -> float:
        return self.params.raw_sampling_rate

    @property
    def end_time_id(self) -> int:
        return (len(self.paths)-1)*self.params.pre_sampled_freq*self.params.sampling_freq + self.params.index_base.value

################################################################################

if __name__ == "__main__":
    import tqdm    
    import os, glob
    from .image import ImageIterator
    from ..parameters import TimeSeriesIterationParameters

    params = TimeSeriesIterationParameters(
        pre_sampled_freq=1,
        sampling_freq=2,
        start_time_id=1,
        end_time_id=100
        )

    image_paths = sorted(glob.glob("data/Wildtrack/Image_subsets/C1/*.png"))

    image_iterator = ImageIterator(
        paths=image_paths,
        params=params
        )

    for frame_id, image in tqdm.tqdm(image_iterator):
        # print(frame_id, image.shape)
        pass