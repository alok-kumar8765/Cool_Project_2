import time
from capture_video_frames import FrameCapture

video = "sample.mp4"
start = time.time()

fc = FrameCapture(video)
total_frames = fc.capture_frames()

end = time.time()

print("Benchmark Results")
print("-----------------")
print(f"Total Frames  : {total_frames}")
print(f"Time Taken   : {end - start:.2f} seconds")
print(f"FPS          : {total_frames / (end - start):.2f}")
