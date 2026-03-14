from foundry.model_client import FoundryClient

client = FoundryClient()

system_prompt = "You are a test assistant."

user_prompt = "Say 'Foundry connection successful' if you can read this."

response = client.ask(system_prompt, user_prompt)

print("\nLLM RESPONSE:\n")
print(response)