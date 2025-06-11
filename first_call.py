import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Fixed system prompt
SYSTEM_PROMPT = "You are a helpful assistant."

print("Welcome! Type 'quit' to exit.")

while True:
    # Get user input from console
    user_input = input("\nYour question: ").strip()
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    if not user_input:
        print("Please enter a question.")
        continue
    
    # Make API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    # Extract and print response
    answer = response["choices"][0]["message"]["content"]
    tokens = response["usage"]["total_tokens"]
    
    print("\n=== Assistant's Response ===")
    print(answer)
    print(f"\nTokens used: {tokens}")
    print("=" * 25) 