from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    duration: int
    priority: str
    frequency: str = "once"
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_daily_schedule(self):
        pass

    def sort_by_time(self, tasks):
        pass

    def filter_by_pet(self, pet_name):
        pass

    def filter_by_status(self, completed):
        pass

    def detect_conflicts(self, tasks):
        pass