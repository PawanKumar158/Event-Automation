import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from plyer import notification
import time
import threading

class Event:
    def __init__(self, name, time, description=""):
        self.name = name
        self.time = time
        self.description = description

    def to_dict(self):
        return {"name": self.name, "time": self.time, "description": self.description}

class DailySchedule:
    def __init__(self, filename="schedule.json"):
        self.events = []
        self.filename = filename
        self.load_events()

    def add_event(self, event):
        self.events.append(event)
        self.save_events()

    def remove_event(self, event_name):
        self.events = [event for event in self.events if event.name != event_name]
        self.save_events()

    def save_events(self):
        with open(self.filename, "w") as f:
            json.dump([event.to_dict() for event in self.events], f)

    def load_events(self):
        try:
            with open(self.filename, "r") as f:
                events_data = json.load(f)
                self.events = [Event(**data) for data in events_data]
        except FileNotFoundError:
            pass

    def send_notifications(self):
        current_time = time.strftime("%H:%M")
        for event in self.events:
            if event.time == current_time:
                notification.notify(
                    title=f"Reminder: {event.name}",
                    message=event.description or "No description",
                    timeout=10
                )

class EventManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Manager")
        self.schedule = DailySchedule()

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=20)

        add_button = tk.Button(root, text="Add Event", command=self.add_event)
        add_button.pack(side=tk.LEFT, padx=10)

        remove_button = tk.Button(root, text="Remove Event", command=self.remove_event)
        remove_button.pack(side=tk.LEFT, padx=10)

        self.update_listbox()
        self.start_notification_thread()

    def add_event(self):
        name = simpledialog.askstring("Event Name", "Enter event name:")
        time_ = simpledialog.askstring("Event Time", "Enter event time (HH:MM):")
        description = simpledialog.askstring("Event Description", "Enter event description:")
        
        if name and time_:
            self.schedule.add_event(Event(name, time_, description))
            self.update_listbox()

    def remove_event(self):
        selected = self.listbox.curselection()
        if selected:
            event_name = self.listbox.get(selected).split(": ")[1].split(" - ")[0]
            self.schedule.remove_event(event_name)
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for event in sorted(self.schedule.events, key=lambda x: x.time):
            self.listbox.insert(tk.END, f"{event.time}: {event.name} - {event.description}")

    def start_notification_thread(self):
        def notifications():
            while True:
                self.schedule.send_notifications()
                time.sleep(60)

        thread = threading.Thread(target=notifications, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagerApp(root)
    root.mainloop()
