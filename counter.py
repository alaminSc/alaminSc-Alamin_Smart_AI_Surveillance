class PeopleCounter:

    def __init__(self,line_x,min_distance=10):

        self.line_x = line_x

        self.min_distance = min_distance

        self.previous_positions = {}

        self.entered_count = 0

        self.exited_count = 0


    def update(self, person):

        track_id = person["id"]

        current_x = person["center"][0]

        event = None


        if track_id in self.previous_positions:

            previous_x = self.previous_positions[
                track_id
            ]

            if (

                previous_x < self.line_x

                and current_x >= self.line_x

                and abs(
                    current_x - previous_x
                ) >= self.min_distance

            ):

                self.entered_count += 1

                event = "ENTER"


            elif (

                previous_x > self.line_x

                and current_x <= self.line_x

                and abs(
                    current_x - previous_x
                ) >= self.min_distance

            ):

                self.exited_count += 1

                event = "EXIT"


        self.previous_positions[
            track_id
        ] = current_x


        return event


    def remove_lost_ids(
        self,
        current_ids
    ):

        lost_ids = set(
            self.previous_positions
        ) - current_ids


        for track_id in lost_ids:

            del self.previous_positions[
                track_id
            ]


    @property
    def inside(self):

        return max(
            self.entered_count
            -
            self.exited_count,
            0
        )