from flask import Flask, render_template, request, redirect, url_for
from todo import get_all_tasks, add_task, complete_task, delete_task

app = Flask(__name__)

@app.route("/")
def index():
    filter_status = request.args.get("filter")
    tasks = get_all_tasks(filter_status)
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    priority = request.form["priority"]
    due_date = request.form["due_date"]

    if task.strip():
        add_task(task, priority, due_date)

    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
