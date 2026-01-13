<h1>🕷️ Spider-Todo App – Flask & MySQL</h1>

<p>
A <strong>Spider-Man themed Todo Web Application</strong> built using 
<strong>Flask</strong> and <strong>MySQL</strong>.  
This is my <strong>first full-stack web app</strong> combining backend logic,
database integration, and a modern glassmorphism-inspired UI.
</p>

<p>
The app lets users manage daily tasks with priority levels, due dates, 
and task status filtering — all with a stylish Spider-Man inspired design.
</p>

<hr>

<h2>🎥 Demo Video</h2>
<p>
Watch the app in action:<br>
<a href="https://youtu.be/qI3THKc6b_c" target="_blank">▶ Watch Demo Video</a>
</p>

<hr>

<h2>🕸️ Project Overview</h2>

<p>
<strong>Spider-Todo App</strong> is a functional task management system where users can:
</p>

<ul>
  <li>Create tasks with a title, priority, and due date</li>
  <li>Mark tasks as completed</li>
  <li>Delete tasks</li>
  <li>Filter tasks by status (All / Pending / Completed)</li>
</ul>

<p>
The UI features a <strong>glass-effect container</strong> layered over a 
<strong>Spider-Man themed background</strong>.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
  <li>➕ Add new tasks</li>
  <li>🏷️ Priority tags: Low / Medium / High</li>
  <li>📅 Due date support</li>
  <li>✅ Mark tasks as completed</li>
  <li>🗑️ Delete tasks</li>
  <li>🔍 Filter tasks by status</li>
  <li>🕷️ Spider-Man themed UI with glass-effect styling</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li><strong>Frontend:</strong> HTML, CSS</li>
  <li><strong>Backend:</strong> Flask (Python)</li>
  <li><strong>Database:</strong> MySQL</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Spiderman-Themed-ToDo-App/
│
├── app.py              # Main Flask application
├── db.py               # MySQL database connection
├── todo.py             # Task management logic
├── todo_app.sql        # Database schema
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
│
├── templates/
│   └── index.html      # Main HTML template
│
└── static/
    ├── style.css       # CSS styling
    └── images/
        └── zo.jpg      # Spider-Man themed background
</pre>

<hr>

<h2>💾 Database Setup</h2>

<p>
Create the database and table by running <code>todo_app.sql</code>.  
Then update <code>db.py</code> with your MySQL credentials:
</p>

<pre>
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="todo_app"
)
</pre>

<hr>

<h2>▶️ How to Run</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/shorminfiza/Spiderman-Themed-ToDo-App.git</code></pre>
  </li>

  <li>Navigate to the project folder:
    <pre><code>cd Spiderman-Themed-ToDo-App</code></pre>
  </li>

  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li>Run <code>todo_app.sql</code> to create the database</li>

  <li>Update <code>db.py</code> with your MySQL credentials</li>

  <li>Run the Flask application:
    <pre><code>python app.py</code></pre>
  </li>

  <li>Open your browser and visit:
    <pre><code>http://127.0.0.1:5000/</code></pre>
  </li>
</ol>

<hr>

<h2>🧠 Learning Outcomes</h2>

<ul>
  <li>Flask backend development</li>
  <li>MySQL database integration</li>
  <li>CRUD operations (Create, Read, Update, Delete)</li>
  <li>Connecting frontend and backend using templates</li>
  <li>Basic UI/UX design with CSS and glass-effect styling</li>
</ul>

<hr>

<h2>🌟 Final Note</h2>

<p>
This project helped me understand real-world web applications by connecting
frontend, backend, and database in one functional system.
</p>

<p><strong>With great power comes great productivity 🕸️</strong></p>

<hr>

<p><em>Developed as a learning project using Flask & MySQL</em></p>
