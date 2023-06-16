document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const completed = document.getElementById('completed').checked;

        const task = {
            title: title,
            description: description,
            completed: completed
        };

        fetch('http://localhost:8000/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(task)
        })
        .then(response => response.json())
        .then(data => {
            displayTask(data);
            taskForm.reset();
        })
        .catch(error => console.log(error));
    });

    function displayTask(task) {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${task.title}</strong>
            <p>${task.description}</p>
            <p>Completed: ${task.completed ? 'Yes' : 'No'}</p>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    }

    function deleteTask(taskId) {
        fetch(`http://localhost:8000/tasks/${taskId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                const li = document.querySelector(`li[data-task-id="${taskId}"]`);
                li.remove();
            }
        })
        .catch(error => console.log(error));
    }

    fetch('http://localhost:8000/tasks')
        .then(response => response.json())
        .then(data => {
            data.forEach(task => displayTask(task));
        })
        .catch(error => console.log(error));
});



})