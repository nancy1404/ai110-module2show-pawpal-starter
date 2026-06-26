from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str = "once"
    pet_name: str = ""
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a care task to this pet."""
        task.pet_name = self.name
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_daily_schedule(self):
        """Return all tasks sorted by time."""
        return self.sort_by_time(self.owner.get_all_tasks())

    def sort_by_time(self, tasks):
        """Sort tasks by their HH:MM time string."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_by_pet(self, pet_name):
        """Return tasks for one pet."""
        return [
            task for task in self.owner.get_all_tasks()
            if task.pet_name.lower() == pet_name.lower()
        ]

    def filter_by_status(self, completed):
        """Return tasks matching completion status."""
        return [
            task for task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def detect_conflicts(self, tasks):
        """Return warnings for tasks scheduled at the same time."""
        seen_times = {}
        conflicts = []

        for task in tasks:
            if task.time in seen_times:
                other_task = seen_times[task.time]
                conflicts.append(
                    f"Conflict at {task.time}: {other_task.description} "
                    f"and {task.description}"
                )
            else:
                seen_times[task.time] = task

        return conflicts
    
    def complete_task_and_create_next(self, task):
        """Mark a task complete and create the next recurring task if needed."""
        task.mark_complete()

        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=task.description,
            time=task.time,
            duration=task.duration,
            priority=task.priority,
            frequency=task.frequency,
            pet_name=task.pet_name,
            due_date=next_date,
        )