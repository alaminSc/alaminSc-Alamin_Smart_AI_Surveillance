class PersonTracker:

    def update(self, results):
        persons = []
        current_ids = set()

        for result in results:
            if result.boxes is None:
                continue
            for box in result.boxes:
                if box.id is None:
                    continue

                track_id = int(box.id[0])
                x1, y1, x2, y2 = map(int,box.xyxy[0])
                confidence = float(box.conf[0])
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)
                current_ids.add(track_id)
                persons.append({"id": track_id,
                    "bbox": (x1,y1,x2,y2),
                    "center": (center_x,center_y),
                    "confidence": confidence
                })
        return persons, current_ids