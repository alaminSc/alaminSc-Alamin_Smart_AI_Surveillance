import cv2
import os

from datetime import datetime

from config import SNAPSHOT_DIR


class SnapshotManager:

    def __init__(self):

        os.makedirs(
            SNAPSHOT_DIR,
            exist_ok=True
        )


    def save(
        self,
        frame,
        event,
        person_id
    ):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S-%f"
        )


        filename = (
            f"{SNAPSHOT_DIR}/"
            f"{event}_{person_id}_"
            f"{timestamp}.jpg"
        )


        success = cv2.imwrite(
            filename,
            frame
        )


        if success:

            print(
                f"📸 Snapshot: {filename}"
            )

            return filename


        print(
            "❌ Failed to save snapshot"
        )

        return None