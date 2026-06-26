from pawpal_system import Owner, Pet, Task


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