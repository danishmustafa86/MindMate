from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import traceback

app = FastAPI()

# CORS setup to allow your React frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to your frontend domain if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

# AIML API Configuration
API_KEY = "236adec514ee40babc9f56aef0443185"
BASE_URL = "https://api.aimlapi.com/v1"
MODEL = "deepseek/deepseek-chat"

# OpenAI-compatible AIML client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

@app.post("/analyze")
async def analyze(request: Request):
    try:
        # Get data from the frontend (mood and journal entry)
        data = await request.json()
        mood = data.get("mood", "")
        entry = data.get("entry", "")

        if not mood and not entry:
            return JSONResponse(status_code=400, content={"error": "Mood and/or entry required"})

        # Construct the message for AI
        message = f"The user feels: {mood}. Their journal entry is: {entry}. Provide helpful feedback or suggestions."

        # Make the API call using OpenAI client to AIML API with the specified model
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an AI assistant who knows everything."},
                {"role": "user", "content": message}
            ]
        )

        # Extract and return the AI response
        analysis = response.choices[0].message.content

        return {"analysis": analysis}

    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
