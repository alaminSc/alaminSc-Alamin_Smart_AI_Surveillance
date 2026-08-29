import os
from datetime import datetime

from config import LOG_DIR


class EventLogger:

    def __init__(self):

        os.makedirs(
            LOG_DIR,
            exist_ok=True
        )

        self.log_file = os.path.join(
            LOG_DIR,
            "events.log"
        )


    def log(
        self,
        event,
        person_id
    ):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        message = (
            f"{timestamp} | "
            f"PERSON {person_id} | "
            f"{event}"
        )

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                message + "\n"
            )

        print(
            f"📝 {message}"
        )


    def log_recording_start(
        self,
        filename
    ):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        message = (
            f"{timestamp} | "
            f"RECORDING START | "
            f"{filename}"
        )

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                message + "\n"
            )


    def log_recording_stop(self):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        message = (
            f"{timestamp} | "
            f"RECORDING STOP"
        )

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                message + "\n"
            )