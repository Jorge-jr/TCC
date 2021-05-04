

class Device(object):

    def __init__(self, address, detection_time):

        self.address = address
        self.timeline = [detection_time]

    def get_timeline(self):
        return self.timeline


    def new_detection(self, detection_time):
        self.timeline += [detection_time]

    
    def get_address(self):
        return self.address

