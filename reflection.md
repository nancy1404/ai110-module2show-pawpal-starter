# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Before writing code, I identified three core actions a user should be able to perform in PawPal+:

1. Add basic owner and pet information so the system knows who is managing care and which pets need support.
2. Add care tasks for each pet, such as feeding, walks, medication, grooming, or appointments.
3. Generate and view a daily schedule that organizes tasks by time, priority, and completion status.

My initial UML design includes four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. The `Owner` class manages one or more pets. The `Pet` class stores details about an individual pet and keeps a list of that pet's tasks. The `Task` class represents one care activity with information such as description, time, duration, priority, frequency, pet name, and completion status. The `Scheduler` class acts as the system's organizing layer by collecting tasks from the owner's pets and preparing daily schedules.

**b. Design changes**

After asking my AI coding assistant to review the initial skeleton, I made one small design change. The AI pointed out that once tasks are collected into one flat schedule, each `Task` should still know which pet it belongs to. Without that relationship, methods like `filter_by_pet()` would be harder to implement.

I accepted this suggestion and added a `pet_name` field to the `Task` class. I did not add extra classes, databases, IDs, or notification features because those would make the design more complex than necessary for the project scope.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
