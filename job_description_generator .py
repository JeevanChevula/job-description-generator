from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI
import re

# Load .env for Groq API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Groq client using OpenAI-compatible SDK
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

app = FastAPI()

# Enhanced input model
class JDRequest(BaseModel):
    role: str
    experience: str
    must_have_skills: list[str]
    preferred_skills: list[str]
    job_type: str | None = None
    location: str | None = None

@app.post("/generate-jd")
def generate_jd(request: JDRequest):
    try:
        # Build dynamic prompt
        prompt = (
            f"Write a clear and professional job description for the role of '{request.role}'.\n"
            f"Experience required: {request.experience}.\n"
            f"Must-have skills: {', '.join(request.must_have_skills)}.\n"
            f"Preferred skills: {', '.join(request.preferred_skills)}.\n"
        )
        if request.job_type:
            prompt += f"This is a {request.job_type} role.\n"
        if request.location:
            prompt += f"The job is based in {request.location}.\n"
        prompt += "Include responsibilities, requirements, and a short 'What We Offer' section."

        # Call Groq LLaMA 3
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are an expert HR assistant who creates clear, attractive job descriptions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )

        # Clean markdown (remove **)
        raw_output = response.choices[0].message.content.strip()
        cleaned_output = re.sub(r"\*\*", "", raw_output)

        return {"job_description": cleaned_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
