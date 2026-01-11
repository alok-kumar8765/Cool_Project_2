from setuptools import setup, find_packages

setup(
    name="capture-video-frames",
    version="1.0.0",
    description="Extract frames from videos using OpenCV",
    author="Alok Kumar",
    author_email="your-email@example.com",
    url="https://github.com/alok-kumar8765/Cool_Project_2",
    packages=find_packages(),
    install_requires=[
        "opencv-python"
    ],
    entry_points={
        "console_scripts": [
            "capture-frames=capture_video_frames.frame_capture:FrameCapture"
        ]
    },
    python_requires=">=3.7",
)
