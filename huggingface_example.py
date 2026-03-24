import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()


def query_huggingface(prompt):
    """Sends a prompt to Hugging Face Inference API and returns the response."""
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        return "Error: HUGGINGFACE_API_KEY environment variable not set."

    try:
        client = InferenceClient(api_key=api_key)

        response = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=250
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Hugging Face: ")
    print("\nThinking...")
    result = query_huggingface(user_prompt)
    print("\n--- Response ---")
    print(result)