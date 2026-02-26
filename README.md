🚀 AI Job Fit Evaluation Agent
This project is an Agentic AI system built using CrewAI that evaluates how well a candidate’s resume matches a job description.
It converts unstructured inputs into structured insights and generates:
•	Candidate profile
•	Job specification
•	Fit score
•	Skill gap analysis
•	Resume improvement suggestions
•	Excel-ready tracking output
________________________________________
🧠 Project Purpose
Built as part of my learning journey into:
•	AI Agents
•	LLM orchestration
•	Structured reasoning workflows
The goal was to simulate how recruiters evaluate candidate-job fit — but in a repeatable, structured and data-driven way.
________________________________________
🏗️ Agent Architecture
This system uses 3 specialized AI agents:
Agent	Role
Resume Profiler	Converts resume into structured candidate profile
Job Extractor	Converts job posting into structured job spec
Fit Scorer	Compares both and generates match insights
________________________________________
🔄 Workflow
Resume (markdown)
        ↓
Resume Profiler Agent
        ↓
Candidate JSON

Job Posting (markdown)
        ↓
Job Extractor Agent
        ↓
Job JSON

Candidate JSON + Job JSON
        ↓
Fit Scorer Agent
        ↓
Fit Score + Gap Analysis + Resume Improvements + Excel Row
________________________________________
📂 Input Files
Stored in:
knowledge/
 ├── resume.md
 └── job1.md
These are read using a custom CrewAI tool.
________________________________________
⚙️ Custom Tool Used
A custom tool (resume_job_reader) allows agents to:
•	Read markdown inputs
•	Inject structured context into reasoning
•	Keep agents file-aware
________________________________________
📊 Output Generated
The system produces:
•	Fit Rating (0–10)
•	Domain Match
•	Skills Match
•	Responsibility Alignment
•	Key Gaps
•	Resume Improvement Suggestions
•	Excel-ready tracker row
This makes it useful for:
✔ Job targeting
✔ Resume tuning
✔ Career planning
✔ Hiring analysis
________________________________________
🔐 Security
Sensitive data is protected using:
.gitignore
The following are excluded:
•	.env
•	API keys
•	Virtual environments
No secrets are committed to GitHub.
________________________________________
🛠️ Tech Stack
•	Python
•	CrewAI
•	Agentic Workflows
•	Markdown-based knowledge ingestion
•	Structured JSON reasoning
________________________________________
▶️ How to Run
Install dependencies:
uv sync
Run the agent system:
uv run crewai run
________________________________________
📈 Learning Outcome
This project helped me understand:
•	Multi-agent orchestration
•	Tool-based reasoning
•	Resume-job semantic alignment
•	Prompt-to-structured transformation
•	Real-world AI automation workflows
________________________________________
👨‍💻 Author
Kshitij Buch
Biomedical Engineer | Data Science Learner
Mumbai, India
________________________________________
🙏 Acknowledgment
Built during my learning journey with Outskill's AI Agents program.

