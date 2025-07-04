# 📝 Job Description Generator using Groq LLaMA 3 & FastAPI

This project is an AI-powered **Job Description Generator** built using **Groq's LLaMA 3-70B model** and **FastAPI**. It generates clear, structured, and professional job descriptions based on user-provided input like role, experience, skills, job type, and location.

---

## 🚀 Features

- 🧠 Powered by **Groq's LLaMA 3-70B** via OpenAI-compatible API  
- ⚙️ Built with **FastAPI** for fast and scalable backend APIs  
- ✅ Structured input with **Pydantic** validation  
- 🧾 Clean output with basic markdown cleanup  
- 🔐 Secure API integration using `.env` for keys  

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Framework**: FastAPI  
- **LLM**: Groq LLaMA 3-70B (OpenAI-compatible)  
- **Input Validation**: Pydantic  
- **Env Management**: python-dotenv  

---

## 📁 Project Structure

Job_Description_Generator/
├── .gitignore # Ignore sensitive files (e.g., .env)
├── .env # API key (not pushed to GitHub)
├── job_description_generator.py # Main FastAPI app
└── README.md # Project overview
## ▶️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/JeevanChevula/job-description-generator.git
   cd job-description-generator
   
2.Install dependencies

   pip install fastapi uvicorn python-dotenv openai

3.Create a .env file

   GROQ_API_KEY=your_actual_groq_api_key_here

4.Run the FastAPI app

uvicorn job_description_generator:app --reload

5.Test the endpoint at
http://127.0.0.1:8000/docs

6.Output Example

POST /generate-jd

{
  "role": "AI/ML Engineer",
  "experience": "2+ years",
  "must_have_skills": ["Python", "TensorFlow", "LLMs"],
  "preferred_skills": ["LangChain", "Docker"],
  "job_type": "Full-time",
  "location": "Remote"
}
