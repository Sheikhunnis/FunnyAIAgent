import google.genai as genai

# --- Initialize Gemini ---
client = genai.Client(api_key=" API_KEY")

# --- Set your name here ---
your_name = "Unnis"  # change to your name

def funny_agent(user_input):
    prompt = f"""
    You are FunnyBot 🤖 — a witty, sarcastic AI friend.
    Always greet or include the user's name ({your_name}) in your reply.
    Keep it friendly, humorous, and positive.
    Use short replies with emojis and jokes when possible.
    
    User ({your_name}): {user_input}
    FunnyBot:
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text.strip()

# --- Chat loop ---
print(f"😂 Welcome {your_name}! FunnyBot is ready to make you laugh. Type 'exit' to quit.")
while True:
    user_text = input(f"{your_name}: ")
    if user_text.lower() == "exit":
        print(f"FunnyBot: Bye {your_name}, don’t forget to laugh today! 😜")
        break
    reply = funny_agent(user_text)
    print("FunnyBot:", reply)

