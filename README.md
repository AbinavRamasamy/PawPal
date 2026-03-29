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


### Smarter Scheduling
- **Mark tasks complete** — check off tasks as you finish them throughout the day.
- **Daily time budget** — set how many minutes you have available and get a warning if your tasks add up to more than that.
- **Conflict detection** — get alerted if two tasks are scheduled at overlapping times.
- **Recurring tasks** — mark tasks as daily or weekly so they automatically come back the next day or next week.
- **Sort by time** — view your tasks in the order they happen throughout the day.
- **Filter tasks** — narrow your view by whether tasks are done or still pending, or by which pet they belong to.
- **Multiple owners and pets** — manage care plans for several pets across different owners, all in one place.

### Testing PawPal+
```bash
python -m pytest tests/test_pawpal.py -v
```

The tests cover:
- **Task completion** — verifying that marking a task done actually changes its status.
- **Pet task count** — confirming that adding a task to a pet increases its task list.
- **Sorting correctness** — ensuring tasks are returned in chronological order by start time.
- **Recurrence logic** — confirming that a completed daily task becomes active again the next day, and that one-time tasks are removed after reset.
- **Conflict detection** — verifying that tasks scheduled at the same time trigger a warning, and that well-spaced tasks do not.

**Confidence level: ★★★★☆ (4/5)**

