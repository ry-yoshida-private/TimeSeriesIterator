# time_series_iterator

## Overview

A program for iterating through time series data such as images and videos in ascending order.

## Components

| Component | Description |
|-----------|-------------|
| [iterator.py](./base.py) | Base class for iteration |
| [parameters.py](./parameters.py) | Program that consolidates parameters used for Iterator |
| [index_base.py](./index_base.py) | Enum defining base index for time series data (ZERO or ONE) |
| [iterators](./iterators/README.md) | Directory containing iterator implementations for different data types |

## Parameters

| Parameter | Description |
|-----------|-------------|
| pre_sampled_freq | The sampling frequency of the pre-sampled time series data |
| sampling_freq | The sampling frequency from input data of the time series data |
| raw_sampling_rate | The sampling rate of the raw time series data (e.g. fps) |
| index_base | The base index of the time series data - ZERO or ONE |
| start_time_id | The start time id of the time series data (counted from index_base) |
| end_time_id | The end time id of the time series data (-1 indicates iteration until the last time) |
| start_video_file_index | The starting index for video file iteration |

