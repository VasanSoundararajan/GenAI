import requests  # Added missing import

def get_completion(prompt):
    endpoint = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=API_KEY"
    
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{"parts": [{"text": prompt}]}]  # Corrected 'message' to 'prompt'
    }
    
    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Sorry, I couldn't process the response."
    else:
        return f"Error {response.status_code}: {response.text}"

# Example Prompt
prompt = """
Solve the problem: A farmer has 100 meters of fencing and wants to enclose the maximum area for his rectangular field. What should the dimensions be?

Let's think about this in a few ways:

1. If the field is a square, each side would be 100 / 4 = 25 meters. The area would be 25 * 25 = 625 square meters.

2. What if the field is not a square? Let's try a 2:1 ratio. The lengths would be 40 and 20 meters. The area would be 40 * 20 = 800 square meters.

3. Are there any other ratios that might give a larger area than a square or a 2:1 rectangle?

Considering these options, the best dimensions for the maximum area are:
"""

response = get_completion(prompt)
print("AI Response:")
print(response)
