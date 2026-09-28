class TaskManager:
    def __init__(self, tasks, status):
        self.tasks = tasks
        self.status = status  

    def complete_task(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            self.status[task_number - 1] = "Completed"

    def delete_task(self, task_number):

        if task_number >= 1 and task_number <= len(self.tasks):
            self.tasks[task_number - 1] = "Deleted"
            self.status[task_number - 1] = "Deleted"

    def add_task(self, task):
        self.tasks.append(task)

