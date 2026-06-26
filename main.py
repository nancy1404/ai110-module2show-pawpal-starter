from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Nancy")

milo = Pet("Milo", "Dog")
luna = Pet("Luna", "Cat")

owner.add_pet(milo)
owner.add_pet(luna)

milo.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
luna.add_task(Task("Breakfast feeding", "07:30", 10, "high", "daily"))
milo.add_task(Task("Grooming brush", "18:00", 15, "medium", "weekly"))

scheduler = Scheduler(owner)
schedule = scheduler.get_daily_schedule()

print(f"Today's Schedule for {owner.name}:")
for task in schedule:
    print(
        f"- {task.time} — {task.pet_name}: {task.description} "
        f"({task.duration} min) [priority: {task.priority}]"
    )