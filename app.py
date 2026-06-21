import os
from google import genai
from dotenv import load_dotenv

# 1. Load the secret API key from your hidden .env file
load_dotenv()

def test_ai_connection():
    print("Connecting to the Gemini cluster... please wait...")
    
    try:
        # 2. Initialize the official Google GenAI client
        client = genai.Client()
        
        # 3. Request a response using the ultra-fast gemini-2.5-flash model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Say 'System online! Your environment is completely ready for your project!'",
        )
        
        # 4. Print the result out to your screen
        print("\n--- SUCCESS! ---")
        print(response.text)
        print("----------------\n")
        
    except Exception as error:
        print("\n--- CONNECTION FAILED ---")
        print(f"Error details: {error}")
        print("💡 Double-check that your API key inside the .env file is correct.")
        print("--------------------------\n")

if __name__ == "__main__":
    test_ai_connection()