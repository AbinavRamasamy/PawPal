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
    def __init__(self, name: str, completed: bool = False):
        self.name = name
        self.completed = completed

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

class Scheduler:
    def __init__(self, pet):
        self.pet = pet
        self.tasks = []

    def add_task(self, task):
        """Add a task to this scheduler's task list."""
        self.tasks.append(task)

    def generate_schedule(self):
        """Return tasks sorted by priority (high → medium → low)."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 99))
