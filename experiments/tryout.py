import csv
import networkx

class Dutch_trains:
    train_rides = []
    train_ride_ids = []

    def existence_check(self, row):
        ride_id = self.get_id(row)
        #TODO check for destination changes, if so change to a set
        if ride_id in self.train_ride_ids:
            return True
        else:
            return False

    def add_trainride(self, row):
        if self.existence_check(row):
            #update trainride
            ride_id = self.train_ride_ids.index(self.get_id(row))
            ride = self.train_rides[ride_id]
            ride.update_data(row)
        else:
            ride = Train_ride(row)
            self.train_rides.append(ride)
            self.train_ride_ids.append(self.get_id(row))

    def test_getter(self):
        for i in range(10):
            print(self.train_rides[i].stations)


    def get_id(self, row):
        #date, train number, destination
        return (row[0], row[2], row[5])

class Train_ride:
    def __init__(self, row):
        self.date = row[0]
        self.stations = [row[1]]
        self.train_number = row[2]
        self.transporter = row[3]
        self.train_type = row[4]
        self.destination_s = [row[5]]
        self.departure_times = [row[6]]
        #self.delay_at_station = None
        #self.cancelled = None

    def update_data(self, row):
        self.stations.append(row[1])
        self.departure_times.append(row[6])


if __name__ == "__main__":
    trains = Dutch_trains()
    with open('../data/developdata.csv') as source_file:
        reader = csv.reader(source_file, delimiter=",")
        for row in reader:
            trains.add_trainride(row)
    trains.test_getter()


class Network:
    def nothing(self):
        pass
