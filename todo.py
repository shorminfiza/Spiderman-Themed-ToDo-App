from db import get_connection

def get_all_tasks(filter_status=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if filter_status == "completed":
        cursor.execute("SELECT * FROM todos WHERE status=TRUE ORDER BY due_date")
    elif filter_status == "pending":
        cursor.execute("SELECT * FROM todos WHERE status=FALSE ORDER BY due_date")
    else:
        cursor.execute("SELECT * FROM todos ORDER BY due_date")

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task(task, priority, due_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (task, priority, due_date) VALUES (%s, %s, %s)",
        (task, priority, due_date)
    )
    conn.commit()
    conn.close()


def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET status=TRUE WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
