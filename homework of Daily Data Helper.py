# Daily Data Helper

class DailyData:
    def __init__(self):
        self.data = ["Study", "Exercise", "Read"]
        print("Daily Data Helper Started")

    def show_data(self):
        for i, value in enumerate(self.data):
            print(i, "-", value)

    def __del__(self):
        print("Daily Data Helper Closed")

helper = DailyData()
helper.show_data()

del helper