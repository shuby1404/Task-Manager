class Task:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.priority =  "Not assigned"
        self.status =  "Pending"
        self.time =  "Not decided"
        self.reminder =  "No"
        self.reminder_time =  "No reminder"

    def complete(self):
        self.status =  "Completed"

    def delete(self):
        self.status =  "Deleted"
