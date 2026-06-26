import json
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
    
    def _time_to_minutes(self, time_text):
        """Convert an HH:MM time string into minutes since midnight."""
        hours, minutes = time_text.split(":")
        return int(hours) * 60 + int(minutes)

    def sort_by_time(self, tasks):
        """Sort tasks by their HH:MM time string."""
        return sorted(tasks, key=lambda task: self._time_to_minutes(task.time))

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
        """Return warnings for tasks with overlapping time ranges."""
        conflicts = []
        sorted_tasks = self.sort_by_time(tasks)

        for i in range(len(sorted_tasks)):
            current_task = sorted_tasks[i]
            current_start = self._time_to_minutes(current_task.time)
            current_end = current_start + current_task.duration

            for j in range(i + 1, len(sorted_tasks)):
                next_task = sorted_tasks[j]
                next_start = self._time_to_minutes(next_task.time)
                next_end = next_start + next_task.duration

                if next_start >= current_end:
                    break

                if current_start < next_end and next_start < current_end:
                    conflicts.append(
                        f"Conflict: {current_task.description} "
                        f"({current_task.time}, {current_task.duration} min) overlaps with "
                        f"{next_task.description} "
                        f"({next_task.time}, {next_task.duration} min)"
                    )

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
    
    def find_next_available_slot(self, tasks, preferred_time, duration):
        """Find the next available HH:MM slot that does not overlap existing tasks."""
        candidate_start = self._time_to_minutes(preferred_time)

        while candidate_start + duration <= 24 * 60:
            candidate_end = candidate_start + duration
            has_conflict = False

            for task in tasks:
                task_start = self._time_to_minutes(task.time)
                task_end = task_start + task.duration

                if candidate_start < task_end and task_start < candidate_end:
                    has_conflict = True
                    candidate_start = task_end
                    break

            if not has_conflict:
                hours = candidate_start // 60
                minutes = candidate_start % 60
                return f"{hours:02d}:{minutes:02d}"

        return None
    
def save_owner_to_json(owner, filename):
    """Save an owner's pets and tasks to a JSON file."""
    data = {
        "name": owner.name,
        "pets": []
    }

    for pet in owner.pets:
        pet_data = {
            "name": pet.name,
            "species": pet.species,
            "tasks": []
        }

        for task in pet.tasks:
            pet_data["tasks"].append(
                {
                    "description": task.description,
                    "time": task.time,
                    "duration": task.duration,
                    "priority": task.priority,
                    "frequency": task.frequency,
                    "pet_name": task.pet_name,
                    "completed": task.completed,
                    "due_date": task.due_date.isoformat(),
                }
            )

        data["pets"].append(pet_data)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_owner_from_json(filename):
    """Load an owner, pets, and tasks from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    owner = Owner(data["name"])

    for pet_data in data["pets"]:
        pet = Pet(pet_data["name"], pet_data["species"])

        for task_data in pet_data["tasks"]:
            task = Task(
                description=task_data["description"],
                time=task_data["time"],
                duration=task_data["duration"],
                priority=task_data["priority"],
                frequency=task_data["frequency"],
                pet_name=task_data["pet_name"],
                completed=task_data["completed"],
                due_date=date.fromisoformat(task_data["due_date"]),
            )
            pet.add_task(task)

        owner.add_pet(pet)

    return owner