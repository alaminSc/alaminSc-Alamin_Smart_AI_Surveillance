import cv2

from config import WINDOW_NAME


class Display:

    def __init__(self):

        cv2.namedWindow(
            WINDOW_NAME,
            cv2.WINDOW_NORMAL
        )

        cv2.setWindowProperty(
            WINDOW_NAME,
            cv2.WND_PROP_FULLSCREEN,
            cv2.WINDOW_FULLSCREEN
        )


    def draw_line(self,frame,line_x):
        height = frame.shape[0]
        cv2.line(frame,(line_x, 0),(line_x, height),(255, 255, 0),2)
        cv2.putText(frame,"ENTRY / EXIT",(line_x + 8,30),
            cv2.FONT_HERSHEY_SIMPLEX,0.45,(255, 255, 0),1,cv2.LINE_AA)


        # Enter

        cv2.putText(
            frame,
            "ENTER ->",
            (
                line_x + 10,
                height // 2
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 255, 0),
            1,
            cv2.LINE_AA
        )


        # Exit

        cv2.putText(
            frame,
            "<- EXIT",
            (
                line_x - 90,
                height // 2
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 0, 255),
            1,
            cv2.LINE_AA
        )


    def draw_person(self,frame,person):
        x1, y1, x2, y2 = person["bbox"]
        center_x, center_y = person["center"]
        track_id = person["id"]
        confidence = person["confidence"]
        cv2.rectangle(frame,(x1, y1),(x2, y2),(0, 255, 0),2)
        cv2.circle(frame,(center_x,center_y),5,(0, 0, 255),-1)
        label = (f"ID:{track_id} "f"{confidence:.2f}")
        cv2.putText(frame,label,(x1,y1 - 7),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0, 255, 0),1,cv2.LINE_AA)


    def dashboard(self,frame,visible,entered,exited,inside,recording):

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"SURVEILLANCE Screen System",(20, 30),font,0.55,(255, 255, 255),1,cv2.LINE_AA)
        cv2.putText(frame,f"Visible: {visible}",(20, 55),font,0.45,(255, 255, 255),1,cv2.LINE_AA)
        cv2.putText(frame,f"ENTERED: {entered}",(20, 80),font,0.45,(0, 255, 0),1,cv2.LINE_AA)
        cv2.putText(frame,f"EXITED: {exited}",(20, 105),font,0.45,(0, 0, 255),1,cv2.LINE_AA)
        cv2.putText(frame,f"INSIDE: {inside}",(20, 130),font,0.45,(0, 255, 255),1,cv2.LINE_AA)

        if recording:

            cv2.putText(frame,"● REC",(frame.shape[1] - 80,30),font,0.5,(0, 0, 255),1,cv2.LINE_AA)


    def show(self, frame):
        cv2.imshow(
            WINDOW_NAME,
            frame
        )


    def should_quit(self):

        return (
            cv2.waitKey(1) & 0xFF
        ) == 27


    def close(self):

        cv2.destroyAllWindows()