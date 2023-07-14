from enum import Enum
import datetime

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.deliveredAt = None
        self.departureTime = None
        self.status = "At Hub"

    # print formatted package information
    # Space-Time Complexity O(1)
    def print(self):
        print(f'[ID]: {self.id}  [Address]: {self.address}, {self.city}, {self.state} {self.zip} '
              f' [Delivery By]: {self.deliveredAt} [Weight]: {self.weight}')

    # update package information based on time
    # Space-Time Complexity O(1)
    def update_status(self, time):
        if self.deliveredAt is not None and time >= self.deliveredAt:
            self.status = "Delivered"
        elif self.departureTime is not None and time > self.departureTime:
            self.status = "En route"
        else:
            self.status = "At Hub"
