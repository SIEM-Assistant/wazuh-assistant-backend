import os
import openai

def raw_send_prompt_one_off(system_prompt: str, user_prompt: str) -> str:
    client = openai.OpenAI(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
    )

    response = client.chat.completions.create(
        model=os.environ["OPENAI_MODEL"],
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content
