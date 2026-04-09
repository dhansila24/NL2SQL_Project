from fastapi import FastAPI
import sqlite3
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
print("API KEY:", os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

# Setup Gemini
client = None

# Connect DB
conn = sqlite3.connect("clinic.db", check_same_thread=False)

@app.get("/")
def home():
    return {"message": "NL2SQL API is running"}

@app.get("/query")
def query_db(question: str):
    try:
        global client
        
        if client is None:
            client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

        prompt = f"SQL only: {question}"

        response = client.models.generate_content(
           model="gemini-2.0-flash",
            contents=prompt
        )

        sql = response.text.strip()

        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        return {
            "question": question,
            "sql": sql,
            "result": result
        }

    except Exception as e:
        return {"error": str(e)}
    print("Using model: gemini-2.0-flash")