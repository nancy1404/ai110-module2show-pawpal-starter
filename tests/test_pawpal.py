from datetime import timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_mark_complete():
    task = Task("Morning walk", "08:00", 30, "high")

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Milo", "Dog")
    task = Task("Morning walk", "08:00", 30, "high")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task
    assert task.pet_name == "Milo"


def test_scheduler_sorts_tasks_by_time():
    owner = Owner("Nancy")
    pet = Pet("Milo", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Evening brush", "18:00", 15, "medium"))
    pet.add_task(Task("Breakfast", "07:30", 10, "high"))
    pet.add_task(Task("Morning walk", "08:00", 30, "high"))

    scheduler = Scheduler(owner)
    schedule = scheduler.get_daily_schedule()

    assert [task.description for task in schedule] == [
        "Breakfast",
        "Morning walk",
        "Evening brush",
    ]


def test_filter_by_pet():
    owner = Owner("Nancy")
    milo = Pet("Milo", "Dog")
    luna = Pet("Luna", "Cat")
    owner.add_pet(milo)
    owner.add_pet(luna)

    milo.add_task(Task("Morning walk", "08:00", 30, "high"))
    luna.add_task(Task("Breakfast feeding", "07:30", 10, "high"))

    scheduler = Scheduler(owner)
    milo_tasks = scheduler.filter_by_pet("Milo")

    assert len(milo_tasks) == 1
    assert milo_tasks[0].description == "Morning walk"


def test_detect_conflicts_for_overlapping_tasks():
    owner = Owner("Nancy")
    pet = Pet("Milo", "Dog")
    owner.add_pet(pet)

    task_one = Task("Morning walk", "08:00", 30, "high")
    task_two = Task("Medication", "08:00", 5, "high")
    pet.add_task(task_one)
    pet.add_task(task_two)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

    assert len(conflicts) == 1
    assert "overlaps with" in conflicts[0]
    assert "Morning walk" in conflicts[0]
    assert "Medication" in conflicts[0]


def test_daily_recurring_task_creates_next_day_task():
    owner = Owner("Nancy")
    pet = Pet("Luna", "Cat")
    owner.add_pet(pet)

    task = Task("Breakfast feeding", "07:30", 10, "high", "daily")
    pet.add_task(task)

    scheduler = Scheduler(owner)
    next_task = scheduler.complete_task_and_create_next(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == task.due_date + timedelta(days=1)
    assert next_task.description == task.description

def test_find_next_available_slot_after_conflict():
    owner = Owner("Nancy")
    pet = Pet("Milo", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Morning walk", "08:00", 30, "high"))
    pet.add_task(Task("Medication", "08:00", 5, "high"))

    scheduler = Scheduler(owner)
    slot = scheduler.find_next_available_slot(owner.get_all_tasks(), "08:00", 20)

    assert slot == "08:30"