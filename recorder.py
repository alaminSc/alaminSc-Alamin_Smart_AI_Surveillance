import cv2
import os

from datetime import datetime

from config import (
    RECORDING_DIR,
    FPS,
    NO_PERSON_TIMEOUT
)


class Recorder:

    def __init__(
        self,
        width,
        height
    ):

        os.makedirs(
            RECORDING_DIR,
            exist_ok=True
        )

        self.width = width

        self.height = height

        self.writer = None

        self.recording = False

        self.last_person_time = 0


    def start(self):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S-%f"
        )


        filename = (
            f"{RECORDING_DIR}/"
            f"surveillance_{timestamp}.mp4"
        )


        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )


        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            FPS,
            (
                self.width,
                self.height
            )
        )


        if not self.writer.isOpened():

            print(
                "❌ Cannot start video recording"
            )

            self.writer = None

            return


        self.recording = True


        print(
            f"🎥 Recording: {filename}"
        )


    def update(
        self,
        frame,
        people_detected,
        current_time
    ):

        if people_detected:

            self.last_person_time = current_time


            if not self.recording:

                self.start()


        if self.recording:

            self.writer.write(
                frame
            )


            if (
                current_time
                -
                self.last_person_time
                >= NO_PERSON_TIMEOUT
            ):

                self.stop()


    def stop(self):

        if self.writer is not None:

            self.writer.release()

            self.writer = None


        if self.recording:

            print(
                "⏹️ Recording stopped"
            )


        self.recording = False


    def is_recording(self):

        return self.recording