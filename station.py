import station_state, datetime, device


class Station(device.Device):
    

    def __init__(self, address, capture_time):

        super().__init__(address, capture_time)
        self.state = station_state.StationState()


    def new_detection(self, detection_time):
        self.timeline += [detection_time]
        self.update()

    def update(self):

        if self.state.is_initial and (datetime.datetime.now() - self.timeline[-1]).seconds < 2:
            self.state.accept()
        elif self.state.is_potential_in and (datetime.datetime.now() - self.timeline[-1]).seconds < 2:
            self.state.confirm_in()
        elif self.state.is_potential_in and (datetime.datetime.now() - self.timeline[-1]).seconds > 2:
            self.state.restart_in()
        elif self.state.is_present and (datetime.datetime.now() - self.timeline[-1]).seconds > 2:
            self.state.detach()
        elif self.state.is_potential_out and (datetime.datetime.now() - self.timeline[-1]).seconds < 2:
            self.state.back_in()
        elif self.state.is_potential_out and (datetime.datetime.now() - self.timeline[-1]).seconds > 2:
            self.state.confirm_out()
        elif self.state.is_absent and (datetime.datetime.now() - self.timeline[-1]).seconds > 2:
            self.state.restart_out()



