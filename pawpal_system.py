from dataclasses import dataclass


@dataclass
class Pet:
    name: str
    species: str

    def __post_init__(self):
        """Initialize an empty task list for the pet."""
        self.tasks: list = []

    def add_task(self, task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

class Task:
    def __init__(self, name: str, duration: int, priority: str, time: str = "00:00", completed: bool = False, recurrence: str = None):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.time = time
        self.completed = completed
        self.recurrence = recurrence

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

class Scheduler:
    def __init__(self, pet, time_budget: int = 120):
        self.pet = pet
        self.tasks = []
        self.time_budget = time_budget
        self.day_count = 0

    def add_task(self, task):
        """Add a task to this scheduler's task list."""
        self.tasks.append(task)

    def check_conflicts(self):
        """Return a warning string if pending task durations exceed the time budget, else None."""
        total = sum(t.duration for t in self.tasks if not t.completed)
        if self.time_budget > 0 and total > self.time_budget:
            return f"Total pending duration ({total} min) exceeds daily budget ({self.time_budget} min)."
        return None

    def detect_time_conflicts(self):
        """Return a list of warning strings for any tasks whose time windows overlap."""
        def to_minutes(t):
            h, m = t.time.split(":")
            return int(h) * 60 + int(m)

        warnings = []
        pending = [t for t in self.tasks if not t.completed]
        for i in range(len(pending)):
            for j in range(i + 1, len(pending)):
                a, b = pending[i], pending[j]
                a_start, b_start = to_minutes(a), to_minutes(b)
                a_end = a_start + a.duration
                b_end = b_start + b.duration
                if a_start < b_end and b_start < a_end:
                    warnings.append(
                        f"'{a.name}' ({a.time}, {a.duration} min) overlaps with '{b.name}' ({b.time}, {b.duration} min)."
                    )
        return warnings

    def reset_for_new_day(self):
        """Advance one day: reset daily tasks each day, weekly tasks only every 7 days."""
        self.day_count += 1
        self.tasks = [t for t in self.tasks if t.recurrence is not None]
        for t in self.tasks:
            if t.recurrence == "daily":
                t.completed = False
            elif t.recurrence == "weekly" and self.day_count % 7 == 0:
                t.completed = False

    def sort_by_time(self):
        """Return tasks sorted by scheduled start time in HH:MM format."""
        return sorted(self.tasks, key=lambda t: tuple(int(part) for part in t.time.split(":")))

    def filter_tasks(self, completed: bool = None, pet_name: str = None):
        """Return tasks filtered by completion status and/or pet name."""
        result = self.tasks
        if completed is not None:
            result = [t for t in result if t.completed == completed]
        if pet_name is not None:
            result = [t for t in result if self.pet.name.lower() == pet_name.lower()]
        return result

    def generate_schedule(self):
        """Return incomplete tasks sorted by priority (high → medium → low)."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        pending = [t for t in self.tasks if not t.completed]
        return sorted(pending, key=lambda t: priority_order.get(t.priority, 99))
