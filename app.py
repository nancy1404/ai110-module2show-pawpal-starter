import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
PawPal+ helps a pet owner plan daily care tasks for their pets.
Add an owner, add a pet, schedule tasks, and generate a sorted daily plan.
"""
)

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

st.divider()

st.subheader("Owner and Pet")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    new_pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name} the {species}.")

if st.session_state.owner.pets:
    st.write("Current pets:")
    st.table(
        [
            {"name": pet.name, "species": pet.species}
            for pet in st.session_state.owner.pets
        ]
    )
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Add Care Task")

if st.session_state.owner.pets:
    selected_pet_name = st.selectbox(
        "Choose pet",
        [pet.name for pet in st.session_state.owner.pets],
    )

    task_title = st.text_input("Task title", value="Morning walk")
    task_time = st.text_input("Time (HH:MM)", value="08:00")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add task"):
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet_name:
                pet.add_task(
                    Task(
                        task_title,
                        task_time,
                        int(duration),
                        priority,
                        frequency,
                    )
                )
                st.success(f"Added task for {selected_pet_name}.")
else:
    st.info("Add a pet before creating tasks.")

st.divider()

st.subheader("Build Schedule")

scheduler = Scheduler(st.session_state.owner)

if st.button("Generate schedule"):
    schedule = scheduler.get_daily_schedule()

    if schedule:
        st.write("Today's Schedule")
        st.table(
            [
                {
                    "time": task.time,
                    "pet": task.pet_name,
                    "task": task.description,
                    "duration": task.duration,
                    "priority": task.priority,
                    "frequency": task.frequency,
                    "completed": task.completed,
                }
                for task in schedule
            ]
        )

        conflicts = scheduler.detect_conflicts(schedule)
        if conflicts:
            for conflict in conflicts:
                st.warning(conflict)
    else:
        st.info("No tasks scheduled yet.")