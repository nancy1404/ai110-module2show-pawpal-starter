# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude in VS Code to review my `pawpal_system.py` class skeleton before implementation. The goal was to identify missing relationships or potential logic bottlenecks in my `Owner`, `Pet`, `Task`, and `Scheduler` design while keeping the system beginner-friendly and within the project scope.

**What did the agent do?**

Claude reviewed the skeleton and identified that the `Task` class did not know which `Pet` it belonged to. It explained that once `Owner.get_all_tasks()` collects tasks into one flat list, methods like `Scheduler.filter_by_pet()` would be harder to implement unless each task preserved pet information.

Files affected after reviewing the agent's suggestion:

- `pawpal_system.py`: added a `pet_name` field to the `Task` dataclass and later added `Scheduler.find_next_available_slot()` for the stretch scheduling feature.
- `main.py`: added CLI demos for conflict detection, recurring tasks, and the next available slot feature.
- `tests/test_pawpal.py`: added automated tests for core behavior and the next available slot algorithm.
- `README.md`: documented smarter scheduling features, sample CLI output, testing output, and UI/output formatting.
- `reflection.md`: documented the design change and why I accepted it.
- `ai_interactions.md`: documented the agent workflow and comparison process.

I also implemented a stretch scheduling feature, `Scheduler.find_next_available_slot()`, which searches for the next open time after a preferred start time while avoiding overlapping task durations.

**What did you have to verify or fix manually?**

I manually reviewed the suggestion before accepting it. I accepted the `pet_name` field because it directly supported `filter_by_pet()` and kept the design simple. I did not accept or implement extra complexity such as databases, IDs, notification systems, or advanced datetime parsing at the skeleton stage. I verified the final behavior later with `python3 main.py`, the Streamlit UI, and `python3 -m pytest`.

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | Claude in VS Code | ChatGPT |
| **Prompt** | "Review my PawPal+ class skeleton in pawpal_system.py. The system uses four main classes: Owner, Pet, Task, and Scheduler. Do you notice any missing relationships or potential logic bottlenecks before I implement the methods? Please keep the design simple and beginner-friendly." | "Check the PawPal+ rubric and help me verify whether my current implementation covers the required features and which stretch features are realistic to attempt." |
| **Response summary** | Claude focused on code structure. It identified that `Task` needed a pet relationship so flattened schedules could still support filtering by pet. It also suggested thinking carefully about time formats. | ChatGPT focused on project planning and rubric coverage. It helped organize the project into phases and identify documentation gaps and realistic stretch features. |
| **What was useful** | Claude was useful for reviewing the actual code skeleton inside VS Code and catching a structural issue before implementation. | ChatGPT was useful for step-by-step workflow, documentation wording, commit checkpoints, and checking the project against the grading rubric. |
| **Problems noticed** | Some suggestions, such as adding time parsing helpers immediately, were better saved for later algorithm work rather than the first skeleton. | Some suggestions needed to be checked against the actual starter files and project rubric before being applied. |
| **Decision** | I used Claude's `pet_name` suggestion because it improved the class design without adding too much complexity. | I used ChatGPT mainly for planning, verification, README/reflection drafting, and deciding which stretch features were worth attempting. |

**Which approach did you use in your final implementation and why?**

I used both approaches for different purposes. Claude was most helpful inside VS Code when reviewing the actual code skeleton, while ChatGPT was more helpful for breaking the project into manageable steps and checking rubric coverage. In the final implementation, I accepted the specific `pet_name` design improvement from Claude, then used step-by-step verification and testing to make sure the system worked correctly.