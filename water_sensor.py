"""Compatibility shim for tests.

Tests expect a top-level `water_sensor.py`. The implementation lives in
`src/water_sensor.py` so re-export the function here.
"""
from src.water_sensor import streaming_median

__all__ = ["streaming_median"]

if __name__ == "__main__":
    print(streaming_median([5,15,1,3]))
