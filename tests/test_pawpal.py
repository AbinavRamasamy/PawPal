import pytest
from pawpal_system import Pet, Task

def test_mark_complete_changes_task_status():
    task = Task(name="Feed dog", completed=False)
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Buddy", species="Dog")
    initial_count = len(pet.tasks)
    
    task = Task(name="Walk dog")
    pet.add_task(task)
    
    assert len(pet.tasks) == initial_count + 1
