import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


class FoundryClient:

    def __init__(self):

        self.endpoint = os.getenv("FOUNDRY_ENDPOINT")
        self.api_key = os.getenv("FOUNDRY_API_KEY")
        self.deployment = os.getenv("FOUNDRY_DEPLOYMENT")

        self.client = AzureOpenAI(
            api_key=self.api_key,
            api_version="2024-02-15-preview",
            azure_endpoint=self.endpoint
        )

    def ask(self, system_prompt, user_prompt):

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1,
            max_tokens=500
        )

        return response.choices[0].message.content