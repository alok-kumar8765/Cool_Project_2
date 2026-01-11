import os
import shutil
import cv2

class FrameCapture:
    """
    Extract frames from a video file using OpenCV.
    """

    def __init__(self, file_path, output_dir="captured_frames"):
        self.file_path = file_path
        self.output_dir = output_dir

        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def capture_frames(self):
        cap = cv2.VideoCapture(self.file_path)
        frame_number = 0

        while True:
            success, frame = cap.read()
            if not success:
                break

            cv2.imwrite(
                f"{self.output_dir}/frame{frame_number}.jpg",
                frame
            )
            frame_number += 1

        cap.release()
        return frame_number
