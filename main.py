from pawpal_system import Owner, Pet, Task, Scheduler

# Create owner
owner = Owner("Alex")

# Create pets and add to owner
buddy = Pet(name="Buddy", species="Dog")
whiskers = Pet(name="Whiskers", species="Cat")
owner.add_pet(buddy)
owner.add_pet(whiskers)

# Create schedulers for each pet
buddy_scheduler = Scheduler(buddy)
whiskers_scheduler = Scheduler(whiskers)

# Add tasks with different times for Buddy
buddy_scheduler.add_task(Task(title="7:00 AM - Morning Walk",      duration_minutes=30, priority="high"))
buddy_scheduler.add_task(Task(title="12:00 PM - Lunch Feeding",    duration_minutes=10, priority="medium"))
buddy_scheduler.add_task(Task(title="6:00 PM - Evening Playtime",  duration_minutes=20, priority="low"))

# Add tasks with different times for Whiskers
whiskers_scheduler.add_task(Task(title="8:00 AM - Breakfast",      duration_minutes=10, priority="high"))
whiskers_scheduler.add_task(Task(title="3:00 PM - Grooming",       duration_minutes=15, priority="medium"))
whiskers_scheduler.add_task(Task(title="9:00 PM - Night Feeding",  duration_minutes=10, priority="low"))

# Print Today's Schedule
print(f"=== Today's Schedule for {owner.name} ===\n")

for scheduler in [buddy_scheduler, whiskers_scheduler]:
    pet = scheduler.pet
    print(f"--- {pet.name} ({pet.species}) ---")
    for task in scheduler.generate_schedule():
        print(f"  [{task.priority.upper():6}] {task.title} ({task.duration_minutes} min)")
    print()
