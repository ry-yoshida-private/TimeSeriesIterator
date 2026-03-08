# TimeSeriesIterator

`TimeSeriesIterator` is a Python base class for iterating over time-series data (e.g. images, videos) at a specified sampling interval.  
Use `TimeSeriesIterationParameters` to set start/end IDs and sampling frequency, and obtain an `ImageIterator` or `VideoIterator` via `TimeSeriesIterator.build()` according to `MediaType`.

## Installation

Install dependencies only:

```bash
pip install -r requirements.txt
```

## Usage

```python
import glob
import cv2
from time_series_iterator import TimeSeriesIterator, TimeSeriesIterationParameters, IndexBase
from time_series_iterator.media_type import MediaType

# List of video file paths
paths = sorted(glob.glob("videos/*.mp4"))

# Parameters (start ID=1, every 5 frames, iterate until end)
params = TimeSeriesIterationParameters(
    sampling_freq=5,
    raw_sampling_rate=30,
    index_base=IndexBase.ONE,
    start_time_id=1,
    end_time_id=-1,  # -1 means until the last frame
)

# Build iterator from MediaType
iterator = TimeSeriesIterator.build(
    media_type=MediaType.VIDEO,
    paths=paths,
    parameters=params,
)

print(f"Total frames: {len(iterator)}")

# Iterate: (time_id, frame) tuples
for time_id, frame in iterator:
    if time_id == 10:
        cv2.imwrite("frame_0010.jpg", frame)
    if time_id >= 20:
        break

# Get frame at a specific time_id (VideoIterator)
frame = iterator.get_image(30)
cv2.imwrite("frame_0030.jpg", frame)

# Using with statement (releases resources)
with TimeSeriesIterator.build(MediaType.VIDEO, paths, params) as it:
    for time_id, frame in it:
        if time_id >= 5:
            break
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
