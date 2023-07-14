from enum import Enum


class Truck:
    def __init__(self):
        self.packages = []
        self.distance_traveled = 0
        self.status = Status.HUB
        self.departureTime = None
        self.MAX_CAPACITY = 16

    # load list of packages into truck packages
    # Space-Time Complexity O(1)
    def load(self, packages):
        self.packages = packages

    # return all packages stored in truck
    # Space-Time Complexity O(1)
    def get_all_packages(self):
        return self.packages


class Status(Enum):
    HUB = 1
    DELIVERING = 2