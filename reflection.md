# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Before writing code, I identified three core actions a user should be able to perform in PawPal+:

1. Add basic owner and pet information so the system knows who is managing care and which pets need support.
2. Add care tasks for each pet, such as feeding, walks, medication, grooming, or appointments.
3. Generate and view a daily schedule that organizes tasks by time, priority, and completion status.

My initial UML design includes four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. The `Owner` class manages one or more pets. The `Pet` class stores details about an individual pet and keeps a list of that pet's tasks. The `Task` class represents one care activity with information such as description, time, duration, priority, frequency, pet name, due date, and completion status. The `Scheduler` class acts as the system's organizing layer by collecting tasks from the owner's pets and preparing daily schedules.

**b. Design changes**

After asking my AI coding assistant to review the initial skeleton, I made one small design change. The AI pointed out that once tasks are collected into one flat schedule, each `Task` should still know which pet it belongs to. Without that relationship, methods like `filter_by_pet()` would be harder to implement.

I accepted this suggestion and added a `pet_name` field to the `Task` class. Later, I also added a `due_date` field to support recurring daily and weekly tasks. I did not add extra classes, databases, IDs, or notification features because those would make the design more complex than necessary for the project scope.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers several simple constraints: task time, completion status, pet name, frequency, and exact-time conflicts. The most important constraint is time because the daily schedule needs to appear in chronological order. Completion status is also important because the UI can show pending tasks only. Frequency matters for recurring tasks because daily and weekly tasks should be able to generate a future occurrence.

**b. Tradeoffs**

One tradeoff is that my conflict detection only checks whether two tasks have the exact same start time. It does not calculate overlapping durations, such as one task from 8:00 to 8:30 and another from 8:15 to 8:25. This is reasonable for the current project because exact-time conflict detection is simpler, easier to explain, and easier to test. In a future version, I would convert each task's time and duration into time ranges and detect overlapping intervals.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools to brainstorm the system design, review my class skeleton, generate implementation ideas, and think through testing. The most helpful prompts were specific and limited in scope, such as asking whether the `Owner`, `Pet`, `Task`, and `Scheduler` classes had missing relationships before implementation. This helped me avoid adding unnecessary complexity while still improving the design.

**b. Judgment and verification**

One AI suggestion I accepted was adding a `pet_name` field to `Task` so flattened task lists could still be filtered by pet. However, I did not accept every possible improvement. For example, I avoided adding extra IDs, databases, notification systems, or complex datetime handling because those were outside the project scope. I verified the AI-supported code by running `python3 main.py`, checking the Streamlit UI manually, and writing pytest tests for the most important behaviors.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, adding tasks to pets, sorting tasks by time, filtering tasks by pet, detecting duplicate-time conflicts, and creating the next daily recurring task. These tests are important because they cover the core behavior of the scheduler and the relationships between the main classes.

**b. Confidence**

I am fairly confident that the scheduler works for the current project scope because the CLI demo, Streamlit UI, and automated tests all verify the same backend logic. My confidence level is 4 out of 5 stars. If I had more time, I would test invalid time formats, overlapping task durations, weekly recurrence, and tasks for pets with no scheduled care.

---

## 5. Reflection

**a. What went well**

The best part of this project was building the logic layer before connecting the UI. Creating `pawpal_system.py` first made it easier to test the system in the terminal and helped keep the Streamlit app from becoming too messy.

**b. What you would improve**

In another iteration, I would improve the scheduler by adding real time parsing and overlap detection. I would also make priority sorting more advanced so high-priority tasks could be placed earlier when there are limited time slots.

**c. Key takeaway**

My main takeaway is that AI is most useful when I stay in the role of lead architect. The AI can suggest code and design ideas, but I still need to decide what fits the project scope, test the behavior, and keep the system understandable.