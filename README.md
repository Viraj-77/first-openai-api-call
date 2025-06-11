# First OpenAI API Call

This project demonstrates a simple implementation of the OpenAI API using the GPT-3.5-turbo model. The script allows users to input prompts via the console and receive responses from the AI model, along with token usage information.

## Features

- Interactive console interface
- Fixed system prompt for consistent AI behavior
- Display of AI responses and token usage
- Environment variable support for API key security
- Error handling for API calls

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/first-openai-api-call.git
   cd first-openai-api-call
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. Make sure your virtual environment is activated
2. Run the script:
   ```bash
   python first_call.py
   ```
3. Enter your questions when prompted
4. Type 'quit' to exit the program

## Example Output

```
Welcome to the OpenAI API Demo!
Enter your question (or 'quit' to exit):

Your question: What is quantum computing?

=== Assistant's Response ===
[AI's response will appear here]

Total tokens used: [token count]
=========================
```

## Security Note

- Never commit your API key to version control
- Always use environment variables for sensitive information
- The `.env` file is included in `.gitignore` to prevent accidental commits

## Dependencies

- openai==1.3.5
- python-dotenv==1.0.0 