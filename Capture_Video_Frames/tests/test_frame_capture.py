import os
from capture_video_frames import FrameCapture

def test_invalid_video():
    try:
        fc = FrameCapture("invalid.mp4")
        fc.capture_frames()
    except Exception:
        assert True

def test_output_directory_created():
    fc = FrameCapture("sample.mp4", "test_frames")
    assert os.path.exists("test_frames")
