import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

# ── Session state defaults ────────────────────────────────────────────────────
if "owners" not in st.session_state:
    st.session_state.owners = []       # list[Owner]
if "schedulers" not in st.session_state:
    st.session_state.schedulers = {}   # pet_name → Scheduler

# ── Sidebar: filter by owner and pet ─────────────────────────────────────────
with st.sidebar:
    st.header("Filter")
    owners = st.session_state.owners

    if owners:
        owner_names = [o.name for o in owners]
        selected_owner_name = st.selectbox("Owner", owner_names)
        selected_owner = next(o for o in owners if o.name == selected_owner_name)

        pet_names = [p.name for p in selected_owner.pets]
        if pet_names:
            selected_pet_name = st.selectbox("Pet", pet_names)
            selected_pet      = next(p for p in selected_owner.pets if p.name == selected_pet_name)
            active_scheduler  = st.session_state.schedulers.get(selected_pet_name)
        else:
            selected_pet_name, selected_pet, active_scheduler = None, None, None
            st.info("No pets for this owner yet.")
    else:
        selected_owner_name, selected_pet, active_scheduler = None, None, None
        st.info("No owners yet. Create one below.")

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner & Pet")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name   = st.text_input("Pet name",   value="Mochi")
species    = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Create Owner & Pet"):
    existing = next((o for o in st.session_state.owners if o.name == owner_name), None)
    if existing is None:
        existing = Owner(name=owner_name)
        st.session_state.owners.append(existing)
    pet = Pet(name=pet_name, species=species)
    existing.add_pet(pet)
    st.session_state.schedulers[pet_name] = Scheduler(pet=pet)
    st.success(f"Added {pet_name} ({species}) under owner {owner_name}.")
    st.rerun()

st.markdown("### Tasks" + (f" — {selected_pet_name}" if active_scheduler else ""))

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    recurrence = st.selectbox("Recurrence", ["none", "daily", "weekly"])

if st.button("Add task"):
    if active_scheduler is None:
        st.warning("Select an owner and pet from the sidebar first.")
    else:
        task = Task(
            name=task_title,
            duration=int(duration),
            priority=priority,
            recurrence=None if recurrence == "none" else recurrence,
        )
        selected_pet.add_task(task)
        active_scheduler.add_task(task)

if active_scheduler and active_scheduler.tasks:
    st.write("Current tasks:")
    for i, t in enumerate(active_scheduler.tasks):
        col_a, col_b, col_c, col_d, col_e = st.columns([3, 2, 2, 2, 2])
        col_a.write(t.name)
        col_b.write(f"{t.duration} min")
        col_c.write(t.priority)
        col_d.write(t.recurrence or "—")
        if t.completed:
            col_e.write("✓ done")
        elif col_e.button("Complete", key=f"complete_{selected_pet_name}_{i}"):
            t.mark_complete()
            st.rerun()
elif active_scheduler:
    st.info("No tasks yet. Add one above.")
else:
    st.info("Select an owner and pet from the sidebar to manage tasks.")

st.divider()

st.subheader("Build Schedule")

time_budget = st.number_input("Daily time budget (minutes)", min_value=0, max_value=1440, value=120)
if active_scheduler:
    active_scheduler.time_budget = time_budget

col_gen, col_day = st.columns(2)

with col_gen:
    if st.button("Generate schedule"):
        if active_scheduler is None:
            st.warning("Select an owner and pet from the sidebar first.")
        else:
            budget_warn = active_scheduler.check_conflicts()
            if budget_warn:
                st.warning(budget_warn)
            for w in active_scheduler.detect_time_conflicts():
                st.warning(w)
            schedule = active_scheduler.generate_schedule()
            if not schedule:
                st.info("No pending tasks to schedule.")
            else:
                st.success("Schedule (sorted by priority):")
                st.table([
                    {"name": t.name, "duration (min)": t.duration, "priority": t.priority, "recurrence": t.recurrence or "—"}
                    for t in schedule
                ])

with col_day:
    if st.button("Start New Day"):
        if active_scheduler is None:
            st.warning("Select an owner and pet from the sidebar first.")
        else:
            active_scheduler.reset_for_new_day()
            selected_pet.tasks = list(active_scheduler.tasks)
            st.success("New day started. Recurring tasks reset, one-time tasks cleared.")
            st.rerun()
