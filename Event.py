import time 
import schedule 
import tkinter 
import Jango 
import flask


'''class Event:
    def __init__(self, name, time, description=""):
        self.name = name
        self.time = time
        self.description = description

    def __str__(self):
        return f"{self.time}: {self.name} - {self.description}"

class DailySchedule:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]

    def view_schedule(self):
        for event in sorted(self.events, key=lambda x: x.time):
            print(event)

class Event:
    def __init__(self, name, time, description=""):
        self.name = name
        self.time = time
        self.description = description

    def __str__(self):
        return f"{self.time}: {self.name} - {self.description}"

class DailySchedule:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print("Event added successfully!")

    def remove_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]
        print("Event removed successfully!")

    def view_schedule(self):
        if not self.events:
            print("No events scheduled for today.")
        else:
            for event in sorted(self.events, key=lambda x: x.time):
                print(event)

def main():
    schedule = DailySchedule()
    while True:
        print("\nDaily Event Manager")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. View Schedule")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter event name: ")
            time = input("Enter event time (HH:MM): ")
            description = input("Enter event description (optional): ")
            schedule.add_event(Event(name, time, description))

        elif choice == "2":
            event_name = input("Enter the name of the event to remove: ")
            schedule.remove_event(event_name)

        elif choice == "3":
            schedule.view_schedule()

        elif choice == "4":
            print("Exiting the event manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


# Example usage
schedule = DailySchedule()
schedule.add_event(Event("Meeting", "09:00", "Team sync"))
schedule.add_event(Event("Lunch", "12:00", "With client"))
schedule.add_event(Event("Workout", "18:00", "Gym "))'''

class Event:
    def __init__(self, name, time, description=""):
        self.name = name
        self.time = time
        self.description = description

    def __str__(self):
        return f"{self.time}: {self.name} - {self.description}"

class DailySchedule:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print("Event added successfully!")

    def remove_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]
        print("Event removed successfully!")

    def view_schedule(self):
        if not self.events:
            print("No events scheduled for today.")
        else:
            for event in sorted(self.events, key=lambda x: x.time):
                print(event)

def main():
    schedule = DailySchedule()
    while True:
        print("\nDaily Event Manager")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. View Schedule")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter event name: ")
            time = input("Enter event time (HH:MM): ")
            description = input("Enter event description (optional): ")
            schedule.add_event(Event(name, time, description))

        elif choice == "2":
            event_name = input("Enter the name of the event to remove: ")
            schedule.remove_event(event_name)

        elif choice == "3":
            schedule.view_schedule()

        elif choice == "4":
            print("Exiting the event manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
