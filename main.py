import streamlit as st

# Initialize the session state for tasks if not already present
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ''

# Function to remove a task
def remove_task(index):
    del st.session_state.tasks[index]

# App title
st.title('To-Do List App')

# Input field for new tasks
st.text_input('Enter a new task', key='new_task', on_change=add_task)

# Display current tasks
if st.session_state.tasks:
    st.write('### Current Tasks:')
    for idx, task in enumerate(st.session_state.tasks):
        st.write(f"{idx + 1}. {task} [Delete]")
        if st.button(f'Delete {idx + 1}', key=f'delete_{idx}'):
            remove_task(idx)
            st.rerun()  # Replace experimental_rerun with rerun
else:
    st.write('No tasks added yet.')
