import csv
from collections import deque
import datetime
class Navigation:

    def __init__(self):
        self.addresses = []
        self.distances = []

        self.load_addresses()
        self.load_distances()

    def load_distances(self):
        # load distances
        with open('distances.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.distances.append(row)

    def load_addresses(self):
        # load addresses
        with open('addresses.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                address = row[0].split('\n')[1].strip()
                self.addresses.append(address)

    # return the distance between two addresses
    # Space-Time Complexity O(1)
    def get_distance(self, address_from, address_to):
        start = self.addresses.index(address_from)
        end = self.addresses.index(address_to)

        distance = self.distances[start][end]
        if distance == '':
            distance = self.distances[end][start]

        return float(distance)

    # return the min distance and the package associated with it
    # Space-Time Complexity O(N)
    def find_min_distance(self, start, packages):
        min_dist = float('inf')
        min_package = None
        for package in packages:

            temp_dist = float(self.get_distance(start, package.address))
            if temp_dist < min_dist:
                min_dist = temp_dist
                min_package = package

        return [min_dist, min_package]

    # return optimized route and its mileage based on start time and given packages
    # Space-Time Complexity O(N^2)
    def optimize_route(self, packages, time):
        optimized = []
        mileage = 0
        departure_time = time
        next_package = None
        # set start location to hub
        curr_location = "4001 South 700 East"

        # find the closest package whose destination is closest to the current location
        # add package to route
        # continue until there are no more packages left to be added to route
        while len(packages) > 0:
            dist, next_package = self.find_min_distance(curr_location, packages)

            mileage += dist
            time = time + datetime.timedelta(hours=dist / 18)
            next_package.deliveredAt = time
            next_package.departureTime = departure_time
            optimized.append(next_package)
            curr_location = next_package.address
            packages.remove(next_package)

        # add mileage for travelling back to hub
        mileage += self.get_distance(curr_location, "4001 South 700 East")

        return [optimized, mileage]



