from pawpal_system import (
    Owner,
    Pet,
    Task,
    Scheduler,
    save_owner_to_json,
    load_owner_from_json,
)


owner = Owner("Nancy")

milo = Pet("Milo", "Dog")
luna = Pet("Luna", "Cat")

owner.add_pet(milo)
owner.add_pet(luna)

milo.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
luna.add_task(Task("Breakfast feeding", "07:30", 10, "high", "daily"))
milo.add_task(Task("Grooming brush", "18:00", 15, "medium", "weekly"))
luna.add_task(Task("Medication", "08:00", 5, "high", "daily"))

scheduler = Scheduler(owner)
schedule = scheduler.get_daily_schedule()

print(f"Today's Schedule for {owner.name}:")
for task in schedule:
    print(
        f"- {task.time} — {task.pet_name}: {task.description} "
        f"({task.duration} min) [priority: {task.priority}, frequency: {task.frequency}]"
    )

print("\nConflict Warnings:")
conflicts = scheduler.detect_conflicts(schedule)
if conflicts:
    for conflict in conflicts:
        print(f"- {conflict}")
else:
    print("- No conflicts found.")

print("\nRecurring Task Demo:")
next_task = scheduler.complete_task_and_create_next(schedule[0])
if next_task:
    print(
        f"- Completed '{schedule[0].description}'. "
        f"Next occurrence: {next_task.due_date} at {next_task.time}."
    )
else:
    print(f"- Completed '{schedule[0].description}'. No recurring task created.")

print("\nNext Available Slot Demo:")
next_slot = scheduler.find_next_available_slot(schedule, "08:00", 20)
if next_slot:
    print(f"- Next available 20-minute slot after 08:00: {next_slot}")
else:
    print("- No available slot found.")

print("\nPersistence Demo:")
save_owner_to_json(owner, "pawpal_data.json")
loaded_owner = load_owner_from_json("pawpal_data.json")
print(
    f"- Saved and loaded owner '{loaded_owner.name}' "
    f"with {len(loaded_owner.pets)} pets."
)