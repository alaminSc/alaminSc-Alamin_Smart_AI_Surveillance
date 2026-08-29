from ultralytics import YOLO

from config import (
    MODEL_PATH,
    CONFIDENCE
)


class Detector:

    def __init__(self):

        self.model = YOLO(
            MODEL_PATH
        )


    def track(self, frame):

        return self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=CONFIDENCE,
            classes=[0],
            verbose=False
        )