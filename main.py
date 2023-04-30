import os
import openai
from dotenv import load_dotenv

def test_api_access() -> openai.Model:
    """
    Test whether we have access to the OpenAI api.

    :return: Some information about a model.
    """
    return openai.Model.retrieve("gpt-4")

def prompt_the_model(prompt: str) -> str:
    """
    Prompt the model with the given string as content.

    :param prompt: The prompt to use as content for the model.
    :return: The model's response.
    """
    completion = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content # type: ignore

def main():
    """
    Call other functions, run on startup.
    """
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(prompt_the_model("Hello GPT4!"))

if __name__ == "__main__":
    main()