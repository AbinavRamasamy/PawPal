from pawpal_system import Owner, Pet, Task, Scheduler

# ── Setup ────────────────────────────────────────────────────────────────────
owner = Owner("Alex")

buddy    = Pet(name="Buddy",    species="Dog")
whiskers = Pet(name="Whiskers", species="Cat")
owner.add_pet(buddy)
owner.add_pet(whiskers)

buddy_scheduler    = Scheduler(buddy,    time_budget=60)
whiskers_scheduler = Scheduler(whiskers, time_budget=60)

# ── Buddy's tasks (intentional overlap at 08:00) ─────────────────────────────
buddy_scheduler.add_task(Task(name="Morning Walk",  duration=30, priority="high",   time="08:00", recurrence="daily"))
buddy_scheduler.add_task(Task(name="Vet Checkup",   duration=60, priority="high",   time="08:15"))   # overlaps Morning Walk
buddy_scheduler.add_task(Task(name="Lunch Feeding", duration=10, priority="medium", time="12:00", recurrence="daily"))
buddy_scheduler.add_task(Task(name="Bath Time",     duration=20, priority="low",    time="17:00", recurrence="weekly"))

# ── Whiskers's tasks ──────────────────────────────────────────────────────────
whiskers_scheduler.add_task(Task(name="Breakfast",   duration=10, priority="high",   time="08:00", recurrence="daily"))
whiskers_scheduler.add_task(Task(name="Grooming",    duration=15, priority="medium", time="15:00", recurrence="weekly"))
whiskers_scheduler.add_task(Task(name="Night Feeding",duration=10, priority="low",   time="21:00", recurrence="daily"))

# ── 1. generate_schedule (priority order, skips completed) ───────────────────
print("=== generate_schedule (priority order) ===")
for scheduler in [buddy_scheduler, whiskers_scheduler]:
    print(f"\n  {scheduler.pet.name}:")
    for t in scheduler.generate_schedule():
        print(f"    [{t.priority.upper():6}] {t.name} @ {t.time} ({t.duration} min)")

# ── 2. sort_by_time ───────────────────────────────────────────────────────────
print("\n=== sort_by_time ===")
for t in buddy_scheduler.sort_by_time():
    print(f"  {t.time}  {t.name}")

# ── 3. check_conflicts (budget) ───────────────────────────────────────────────
print("\n=== check_conflicts (time budget) ===")
for scheduler in [buddy_scheduler, whiskers_scheduler]:
    result = scheduler.check_conflicts()
    label  = scheduler.pet.name
    print(f"  {label}: {result if result else 'no budget conflict'}")

# ── 4. detect_time_conflicts ──────────────────────────────────────────────────
print("\n=== detect_time_conflicts ===")
for scheduler in [buddy_scheduler, whiskers_scheduler]:
    warnings = scheduler.detect_time_conflicts()
    print(f"\n  {scheduler.pet.name}:")
    if warnings:
        for w in warnings:
            print(f"    WARNING: {w}")
    else:
        print("    no time conflicts")

# ── 5. filter_tasks ───────────────────────────────────────────────────────────
print("\n=== filter_tasks ===")
buddy_scheduler.tasks[0].mark_complete()   # mark Morning Walk done
pending   = buddy_scheduler.filter_tasks(completed=False)
completed = buddy_scheduler.filter_tasks(completed=True)
print(f"  Buddy pending:   {[t.name for t in pending]}")
print(f"  Buddy completed: {[t.name for t in completed]}")

# ── 6. reset_for_new_day (day 1 — weekly tasks should NOT reset) ──────────────
print("\n=== reset_for_new_day ===")
buddy_scheduler.reset_for_new_day()   # day_count → 1
print(f"  After day 1 — tasks kept: {[t.name for t in buddy_scheduler.tasks]}")
print(f"  Bath Time completed: {buddy_scheduler.tasks[-1].completed}")  # weekly, should still be False (never marked)

# advance to day 7 so weekly tasks reset
for _ in range(6):
    buddy_scheduler.reset_for_new_day()
print(f"  After day 7 — Bath Time completed reset to: {buddy_scheduler.tasks[-1].completed}")
