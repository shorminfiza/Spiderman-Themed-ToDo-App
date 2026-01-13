<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spider-Todo App - README</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        h1 {
            color: #c31432;
        }
        a {
            color: #ff416c;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .video-container {
            margin: 20px 0;
        }
        iframe {
            width: 100%;
            height: 400px;
            border: none;
        }
        code {
            background: #eee;
            padding: 2px 5px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>🕷️ Spider-Todo App</h1>

    <p>This is my first web app using <strong>Flask</strong> and <strong>MySQL</strong> together.  
    It's a Spider-Man themed Todo App with priority tags, status filters, and a stylish glassy interface.</p>

    <h2>Features</h2>
    <ul>
        <li>Add tasks with priority and due date</li>
        <li>Mark tasks as completed</li>
        <li>Delete tasks</li>
        <li>Filter tasks: All / Pending / Completed</li>
        <li>Spider-Man themed background with glass effect container</li>
    </ul>

    <h2>Demo</h2>
    <div class="video-container">
        <!-- Replace the src with your demo video URL -->
        <iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID" allowfullscreen></iframe>
    </div>

    <h2>Setup</h2>
    <ol>
        <li>Clone the repository</li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the SQL file <code>todo_app.sql</code> to create the database</li>
        <li>Update <code>db.py</code> with your MySQL credentials:
            <pre>
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="todo_app"
)
            </pre>
        </li>
        <li>Start Flask: <code>python app.py</code></li>
        <li>Open <code>http://127.0.0.1:5000/</code> in your browser</li>
    </ol>

    <p>Enjoy your tasks with Spider-Man power! 🕸️</p>

</body>
</html>
