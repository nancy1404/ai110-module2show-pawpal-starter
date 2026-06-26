# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

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

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` / `Scheduler.get_daily_schedule()` | Returns tasks in chronological order using the task's `HH:MM` time string. |
| Filtering | `Scheduler.filter_by_pet()` / `Scheduler.filter_by_status()` | Allows tasks to be filtered by pet name or completion status. |
| Conflict handling | `Scheduler.detect_conflicts()` | Returns warning messages when two tasks are scheduled for the same exact time. |
| Recurring tasks | `Scheduler.complete_task_and_create_next()` | Marks a daily or weekly task complete and creates the next occurrence. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
