from huggingface_hub import InferenceClient

client = InferenceClient(api_key="note")

messages = [
	{
		"role": "user",
		"content": "What is the capital of Bharat?"
	}
]

completion = client.chat.completions.create(
    model="microsoft/Phi-3.5-mini-instruct", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)