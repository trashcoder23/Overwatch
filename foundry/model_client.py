from azure.ai.inference import ChatCompletionsClient
from azure.identity import DefaultAzureCredential


class FoundryClient:

    def __init__(self, endpoint, model):

        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=DefaultAzureCredential(),
        )

        self.model = model

    def ask(self, prompt):

        response = self.client.complete(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model
        )

        return response.choices[0].message.content