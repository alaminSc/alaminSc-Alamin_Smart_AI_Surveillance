import time
from config import (CAMERA_ID,LINE_POSITION_RATIO,MIN_DISTANCE)
from logger import EventLogger
from camera import Camera
from detector import Detector
from tracker import PersonTracker
from counter import PeopleCounter
from snapshot import SnapshotManager
from recorder import Recorder
from display import Display

snapshot = SnapshotManager()
display = Display()
logger = EventLogger()

camera = Camera(CAMERA_ID)
ret, frame = camera.read()
if not ret:

    print("❌ Cannot read camera")
    camera.release()
    display.close()
    exit()

height, width = frame.shape[:2]
detector = Detector()
line_x = int(width * LINE_POSITION_RATIO)
tracker = PersonTracker()
counter = PeopleCounter(line_x,MIN_DISTANCE)
recorder = Recorder(width,height)

while True:
    ret, frame = camera.read()
    if not ret:
        print("❌ Camera error")
        break
    results = detector.track(frame)
    persons, current_ids = tracker.update(results)
    display.draw_line(frame,line_x)
    for person in persons:
        display.draw_person(frame,person)
        event = counter.update(person)
        if event:
            person_id = person["id"]
            logger.log(event,person_id)
            if event == "ENTER":
                print(f"🟢 Person {person_id} ENTERED")
            elif event == "EXIT":
                print(f"🔴 Person {person_id} EXITED")
            snapshot.save(frame,event,person_id)
    counter.remove_lost_ids(current_ids)
    recorder.update(frame,people_detected=(len(current_ids) > 0),current_time=time.time())
    display.dashboard(frame,visible=len(current_ids),
        entered=counter.entered_count,
        exited=counter.exited_count,
        inside=counter.inside,
        recording=recorder.is_recording()
    )

    display.show(frame)
    if display.should_quit():
        break
recorder.stop()
camera.release()
display.close()
print("SMART AI SURVEILLANCE STOPPED")
print(f"Entered: {counter.entered_count}")
print(f"Exited: {counter.exited_count}")
print(f"Inside: {counter.inside}")