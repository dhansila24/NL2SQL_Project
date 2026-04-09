# NL2SQL Project

## Description
This project converts natural language queries into SQL using FastAPI and Gemini.

## How to Run
pip install -r requirements.txt
uvicorn main:app --port 8001

## Example
Input: show all patients  
Output: SELECT * FROM patients;

## LLM Used
Google Gemini (gemini-1.5-flash)

## Limitations
- API quota issues may occur
- Not using Vanna 2.0 (basic implementation)
