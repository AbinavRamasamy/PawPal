from dataclasses import dataclass


@dataclass
class Pet:
    name: str
    species: str

@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

class Scheduler:
    def __init__(self, pet):
        self.pet = pet
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def generate_schedule(self):
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 99))
