# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## System Design

PawPal+ is built around four core Python classes:

- `Owner`: Stores the owner's name and manages a list of pets.
- `Pet`: Stores identifying information about each pet and keeps a list of that pet's care tasks.
- `Task`: Represents one pet care activity, including its description, time, duration, priority, frequency, due date, pet name, and completion status.
- `Scheduler`: Organizes tasks across all pets owned by an owner. It can sort tasks by time, filter tasks by pet or completion status, detect scheduling conflicts, and create the next occurrence for recurring tasks.

The system follows a CLI-first workflow. The backend logic is implemented in `pawpal_system.py`, demonstrated through `main.py`, tested with `pytest`, and connected to the Streamlit interface in `app.py`.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Running `python3 main.py` generates a readable daily schedule from the backend logic:

```text
Today's Schedule for Nancy:
- 07:30 — Luna: Breakfast feeding (10 min) [priority: high, frequency: daily]
- 08:00 — Milo: Morning walk (30 min) [priority: high, frequency: daily]
- 08:00 — Luna: Medication (5 min) [priority: high, frequency: daily]
- 18:00 — Milo: Grooming brush (15 min) [priority: medium, frequency: weekly]

Conflict Warnings:
- Conflict at 08:00: Morning walk and Medication

Recurring Task Demo:
- Completed 'Breakfast feeding'. Next occurrence: 2026-06-27 at 07:30.
```

## 🧪 Testing PawPal+

Run the full test suite with:

```bash
python3 -m pytest
```

The tests cover core PawPal+ behaviors:

- Marking a task complete
- Adding a task to a pet
- Sorting tasks by time
- Filtering tasks by pet
- Detecting duplicate-time conflicts
- Creating the next daily recurring task

Sample test output:

```text
============ test session starts ============
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/kwaknakyung/projects/codepath/AI110/ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 6 items

tests/test_pawpal.py ......           [100%]

============= 6 passed in 0.04s =============
```

**Confidence Level:** ⭐⭐⭐⭐☆  
I am fairly confident in the current scheduler because the main backend behaviors are covered by automated tests. I would still add more edge case tests later for invalid time formats and overlapping durations.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` / `Scheduler.get_daily_schedule()` | Returns tasks in chronological order using the task's `HH:MM` time string. |
| Filtering | `Scheduler.filter_by_pet()` / `Scheduler.filter_by_status()` | Allows tasks to be filtered by pet name or completion status. |
| Conflict handling | `Scheduler.detect_conflicts()` | Returns warning messages when two tasks are scheduled for the same exact time. |
| Recurring tasks | `Scheduler.complete_task_and_create_next()` | Marks a daily or weekly task complete and creates the next occurrence. |

## 📸 Demo Walkthrough

1. The user opens the PawPal+ Streamlit app and enters the owner's name.
2. The user adds a pet by entering the pet's name and species.
3. The user creates care tasks for that pet, including a task title, time, duration, priority, and frequency.
4. The app stores the owner, pet, and task data in `st.session_state` so the information stays available while the user interacts with the page.
5. When the user clicks **Generate schedule**, the app uses the `Scheduler` class to display tasks in chronological order.
6. The app can show pending tasks only, helping the owner focus on unfinished care tasks.
7. If two tasks are scheduled for the same time, the app displays a conflict warning using the scheduler's conflict detection logic.

Example CLI output from `python3 main.py`:

```text
Today's Schedule for Nancy:
- 07:30 — Luna: Breakfast feeding (10 min) [priority: high, frequency: daily]
- 08:00 — Milo: Morning walk (30 min) [priority: high, frequency: daily]
- 08:00 — Luna: Medication (5 min) [priority: high, frequency: daily]
- 18:00 — Milo: Grooming brush (15 min) [priority: medium, frequency: weekly]

Conflict Warnings:
- Conflict at 08:00: Morning walk and Medication

Recurring Task Demo:
- Completed 'Breakfast feeding'. Next occurrence: 2026-06-27 at 07:30.
```

**Screenshot or video** *(optional)*: Not included.