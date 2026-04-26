# TimeSeriesIterator

## Overview

TimeSeriesIterator (`time_series_iterator`) is a Python package for iterating time-series media data (images and videos) with configurable sampling intervals.
Use `TimeSeriesIterationParameters` to control start/end IDs, sampling frequency, and index base, then build an iterator from `MediaType`.

For package-level details, see [src/time_series_iterator/README.md](src/time_series_iterator/README.md).

## Installation

From the package root (the directory containing `pyproject.toml`):

```bash
pip install .
```

For development:

```bash
pip install -e .
```

If you only need dependencies:

```bash
pip install -r requirements.txt
```

## Example

```python
import glob
import cv2
from time_series_iterator import (
    IndexBase,
    MediaType,
    TimeSeriesIterationParameters,
    TimeSeriesIterator,
)

paths = sorted(glob.glob("videos/*.mp4"))

params = TimeSeriesIterationParameters(
    sampling_freq=5,
    raw_sampling_rate=30,
    index_base=IndexBase.ONE,
    start_time_id=1,
    end_time_id=-1,
)

iterator = TimeSeriesIterator.build(
    media_type=MediaType.VIDEO,
    paths=paths,
    parameters=params,
)

print(f"Total frames: {len(iterator)}")

for time_id, frame in iterator:
    if time_id == 10:
        cv2.imwrite("frame_0010.jpg", frame)
    if time_id >= 20:
        break

frame = iterator.get_image(30)
cv2.imwrite("frame_0030.jpg", frame)

with TimeSeriesIterator.build(MediaType.VIDEO, paths, params) as it:
    for time_id, frame in it:
        if time_id >= 5:
            break
```
