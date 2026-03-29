import pytest
from pawpal_system import Pet, Task, Scheduler


def test_mark_complete_changes_task_status():
    task = Task(name="Feed dog", duration=10, priority="high", completed=False)
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Buddy", species="Dog")
    initial_count = len(pet.tasks)

    task = Task(name="Walk dog", duration=30, priority="medium")
    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1


# ── Sorting Correctness ───────────────────────────────────────────────────────

def test_sort_by_time_returns_chronological_order():
    """Tasks should be returned in chronological order, not lexicographic."""
    pet = Pet(name="Mochi", species="Cat")
    scheduler = Scheduler(pet)
    scheduler.add_task(Task(name="Night feed",    duration=10, priority="low",    time="21:00"))
    scheduler.add_task(Task(name="Morning walk",  duration=30, priority="high",   time="08:00"))
    scheduler.add_task(Task(name="Afternoon meds",duration=5,  priority="medium", time="09:30"))

    ordered = [t.name for t in scheduler.sort_by_time()]
    assert ordered == ["Morning walk", "Afternoon meds", "Night feed"]


# ── Recurrence Logic ──────────────────────────────────────────────────────────

def test_daily_task_resets_for_next_day():
    """Completing a daily task then calling reset_for_new_day should make it active again."""
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler(pet)
    task = Task(name="Morning walk", duration=30, priority="high", recurrence="daily")
    scheduler.add_task(task)

    task.mark_complete()
    assert task.completed is True

    scheduler.reset_for_new_day()
    assert task.completed is False


def test_one_time_task_not_carried_to_next_day():
    """A task with no recurrence should be gone after reset_for_new_day."""
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler(pet)
    scheduler.add_task(Task(name="Vet visit", duration=60, priority="high", recurrence=None))

    scheduler.reset_for_new_day()

    assert all(t.name != "Vet visit" for t in scheduler.tasks)


# ── Conflict Detection ────────────────────────────────────────────────────────

def test_duplicate_start_times_flagged_as_conflict():
    """Two tasks at the exact same start time should always produce a conflict warning."""
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler(pet)
    scheduler.add_task(Task(name="Walk",    duration=30, priority="high",   time="09:00"))
    scheduler.add_task(Task(name="Feeding", duration=10, priority="medium", time="09:00"))

    warnings = scheduler.detect_time_conflicts()
    assert len(warnings) >= 1


def test_non_overlapping_tasks_produce_no_conflict():
    """Tasks that do not overlap in time should not produce any warnings."""
    pet = Pet(name="Buddy", species="Dog")
    scheduler = Scheduler(pet)
    scheduler.add_task(Task(name="Walk",    duration=30, priority="high",   time="08:00"))
    scheduler.add_task(Task(name="Feeding", duration=10, priority="medium", time="12:00"))

    assert scheduler.detect_time_conflicts() == []
