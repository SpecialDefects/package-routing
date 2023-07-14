import csv
import datetime
from package import Package
from hashtable import HashTable
from truck import Truck
from navigation import Navigation


class WGUPS:

    def __init__(self):
        self.packages = HashTable(10)
        self.navigation = Navigation()
        self.load_packages()
        self.time = datetime.timedelta(hours=8.0)
        self.trucks = []

    # retrieve all package statuses
    # Space-Time Complexity O(1) since the for loop is a constant that does not change
    def get_all_package_status(self, time):
        for i in range(41):
            package = self.packages.search(i)
            if package is not None:
                package.update_status(time)
                if package.status in ["Delivered"]:
                    print("ID: " + str(
                        package.id) + " -- Status: " + package.status + " -- Destination: " + package.address + " -- Deadline: " + package.deadline + " -- Delivered at: " + str(
                        package.deliveredAt)[:-3])
                else:
                    print("ID: " + str(
                        package.id) + " -- Status: " + package.status + " -- Destination: " + package.address + " -- Deadline: " + package.deadline)

    # retrieve a package status based on id
    # Space-Time Complexity O(1)
    def get_package_status(self, id, time):
        package = self.packages.search(id)
        if package is not None:
            package.update_status(time)
            if package.status in ["Delivered"]:
                print("ID: " + str(
                    package.id) + " -- Status: " + package.status + " -- Destination: " + package.address + " -- Deadline: " + package.deadline + " -- Delivered at: " + str(
                    package.deliveredAt)[:-3])
            else:
                print("ID: " + str(
                    package.id) + " -- Status: " + package.status + " -- Destination: " + package.address + " -- Deadline: " + package.deadline)
    # load packages for csv
    # Space-Time Complexity O(n)
    def load_packages(self):
        # load packages
        with open('packages.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                loading_package = Package(int(row['ID']), row['Address'], row['City'], row['State'], row['Zip'],
                                          row['Deliver By'], row['Weight'], row['Notes'])
                self.packages.insert(loading_package.id, loading_package)

    # Load trucks with manually determined package ids
    # Space-Time Complexity O(N^2) due to call to optimize_route on trucks
    def load_trucks(self):
        # create trucks
        truck_one = Truck()
        truck_two = Truck()
        truck_three = Truck()

        # package ids for each truck
        truck_one_ids = [1, 13, 14, 15, 16, 20, 29, 30, 31,
                         34, 37, 40]
        truck_two_ids = [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
        truck_three_ids = [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]

        # declare truck departure times
        truck_one_departure_time = datetime.timedelta(hours=8)
        truck_two_departure_time = datetime.timedelta(hours=10, minutes=15)
        truck_three_departure_time = datetime.timedelta(hours=9, minutes=25)

        # create list of packages from package ids
        truck_one_packages = self.package_list_convert(truck_one_ids)

        # get truck 1s route and its mileage
        truck_one_route, truck_one_mileage = self.navigation.optimize_route(truck_one_packages,
                                                                            truck_one_departure_time)

        # set truck 1s mileage and route
        truck_one.distance_traveled = truck_one_mileage
        truck_one.load(truck_one_route)
        print("Truck #1 has been loaded with packages: " + ''.join(str(x) + ', ' for x in truck_one_ids)[:-2])

        # create list of packages from package ids
        truck_two_packages = self.package_list_convert(truck_two_ids)

        # get truck 2s route and its mileage
        truck_two_route, truck_two_mileage = self.navigation.optimize_route(truck_two_packages,
                                                                            truck_two_departure_time)

        # set truck 2s mileage and route
        truck_two.distance_traveled = truck_two_mileage
        truck_two.load(truck_two_route)
        print("Truck #2 has been loaded with packages: " + ''.join(str(x) + ', ' for x in truck_two_ids)[:-2])

        # create list of packages from package ids
        truck_three_packages = self.package_list_convert(truck_three_ids)

        # get truck 3s route and its mileage
        truck_three_route, truck_three_mileage = self.navigation.optimize_route(truck_three_packages,
                                                                                truck_three_departure_time)

        # set truck 3s mileage and route
        truck_three.distance_traveled = truck_three_mileage
        truck_three.load(truck_three_route)
        print("Truck #3 has been loaded with packages: " + ''.join(str(x) + ', ' for x in truck_three_ids)[:-2])

        self.trucks = [truck_one, truck_two, truck_three]

    # convert list of package ids to list of package objects
    # Space-Time Complexity O(N)
    def package_list_convert(self, package_ids):
        package_list = []
        for i in package_ids:
            package = self.packages.search(i)

            if package is not None:
                package_list.append(package)

        return package_list

    # return total mileage of all truck routes
    # Space-Time Complexity O(N)
    def get_mileage(self):
        total_mileage = 0.0
        for truck in self.trucks:
            total_mileage += truck.distance_traveled
        return total_mileage
