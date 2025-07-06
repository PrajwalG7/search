#!/usr/bin/env python

import sys
import time
import os
import google.generativeai as genai

# 🔐 Load API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Error: GEMINI_API_KEY environment variable not set.")
    print("👉 Run `export GEMINI_API_KEY=your-api-key` in your shell config.")
    sys.exit(1)

# ✅ Configure Gemini
genai.configure(
    api_key=API_KEY,
    transport="rest"
)

def ask_gemini(query):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
        prompt = f"What does this command do: {query}? Explain in 1 line with example usage."

        start_time = time.time()
        response = model.generate_content(prompt)
        end_time = time.time()

        duration_ms = int((end_time - start_time) * 1000)
        answer = response.text.strip()

        return f"{answer}\n\n✨ Time taken: {duration_ms} ms"

    except Exception as e:
        return f"❌ Error while querying Gemini: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search <your-command>")
        sys.exit(1)

    command_query = " ".join(sys.argv[1:])
    result = ask_gemini(command_query)
    print(result)
