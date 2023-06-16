document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("taskForm");
    const taskList = document.getElementById("taskList");

    taskForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;
        const completed = document.getElementById("completed").checked;
        const task = {
            title: title,
            description: description,
            completed: completed
        };

        fetch("http://localhost:8000/tasks", {
            method: "POST"
            Headers: {
                "content-Type": "aplication/json"
            },
            body: JSON.stringify(task)
        })
        .then(Response => Response.json())
        .then(data =>{
            displayTask(data);
            taskForm.reset();
        })
        .catch(error => console.log(error));
    });


    

})