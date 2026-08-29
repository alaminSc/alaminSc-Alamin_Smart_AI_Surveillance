import cv2


class Camera:

    def __init__(self, camera_id=0):

        self.cap = cv2.VideoCapture(
            camera_id
        )

        if not self.cap.isOpened():

            raise RuntimeError(
                "❌ Cannot open camera"
            )


    def read(self):

        ret, frame = self.cap.read()

        if ret:
            frame = cv2.flip(frame, 1)

        return ret, frame


    def get_size(self):

        width = int(
            self.cap.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
        )

        height = int(
            self.cap.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
        )

        return width, height


    def release(self):

        self.cap.release()