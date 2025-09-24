# import google.generativeai as genai
# import user_config  # This should contain: special_key = "YOUR_API_KEY"

# def send_request(query: str) -> str:
#     # Configure Gemini with your API key
#     genai.configure(api_key=user_config.special_key)

#     # Choose Gemini model
#     model = genai.GenerativeModel("gemini-1.5-flash")

#     # Send the query
#     response = model.generate_content(query)

#     # Return the text content
#     return response.text.strip()


import google.generativeai as genai
import user_config

# Setup Gemini API once
genai.configure(api_key=user_config.special_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def send_request(query: str) -> str:
    try:
        response = model.generate_content(query)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"
