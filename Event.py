import time 
import schedule 
import tkinter 
import Jango 
import flask


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

    def remove_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]

    def view_schedule(self):
        for event in sorted(self.events, key=lambda x: x.time):
            print(event)

# Example usage
schedule = DailySchedule()
schedule.add_event(Event("Meeting", "09:00", "Team sync"))
schedule.add_event(Event("Lunch", "12:00", "With client"))
schedule.add_event(Event("Workout", "18:00", "Gym session"))
schedule.add_event(Event("Dinner", "20:00", "Table"))
schedule.add_event(Event("Book", "21:00", "Novels"))
schedule.add_event(Event("SLEEP", "22:00","On Bed"))

schedule.view_schedule()
