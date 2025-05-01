🤖 BSIS AI Assistant – ZDSPGC Aurora
The BSIS AI Assistant is an intelligent web-based chatbot system designed specifically to help freshmen students and prospective enrollees at Zamboanga del Sur Provincial Government College – Aurora. The assistant focuses solely on answering relevant and frequently asked questions related to the Bachelor of Science in Information Systems (BSIS) course.

🎯 Purpose
This project aims to:

Provide quick and accurate responses to common BSIS-related inquiries.

Assist incoming BSIS freshmen with course requirements, enrollment steps, subjects, and expectations.

Reduce the workload on staff by automating repetitive informational tasks.

🧠 Features
✅ AI-powered question answering system.

✅ Answers only BSIS-related questions (rejects off-topic queries).

✅ Simple web interface with chat functionality.

✅ Works offline with a local knowledge base (JSON).



🚀 Tech Stack
Backend: Python / Flask

Frontend: HTML, TailwindCSS (via CDN)

AI Logic: Custom logic using keyword matching or simple NLP

Database: JSON

📁 Folder Structure

school_ai/
│
├── static/
│   ├── images/          # Image assets
│   ├── JS/              # JavaScript files
│   │   └── main.js
│   └── styles.css       # CSS stylesheet
│
├── templates/           # HTML templates
│   └── app.py           # (Note: Typically app.py would be in root)
│
├── data.json            # Data storage
├── Q&A.txt              # Documentation
└── README.md            # Project documentation

📌 Example Questions It Can Answer
"What is BSIS?"

"What are the first year subjects in BSIS?"

"How many years does BSIS take?"

"What are the requirements to enroll in BSIS at ZDSPGC?"

"Who is the professor for Programming II?"

⛔ What It Will Reject
Questions not related to BSIS (e.g., "What is the weather today?") will be responded with:

"Beyond the scope of BSIS Assistant."

🛠️ How to Run
Clone the repository:


git clone https://github.com/jhunamae/BSIS---AI-Assistant.git
cd BSIS---AI-Assistant/school_ai

Install dependencies:

pip install -r requirements.txt

Run app.py

Open your browser and paste this:
http://127.0.0.1:8000/


🧑‍💻 Developer
Developed by: Jhunamae Buoc
Course: BSIS, ZDSPGC - Aurora
Instructor: Prof. John Bon Juvi Jumarito (Programming II)
