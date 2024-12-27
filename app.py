from huggingface_hub import InferenceClient
import sqlite3
import os

# try:
#     with sqlite3.connect("my.db") as conn:
#         print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

# except sqlite3.OperationalError as e:
#     print("Failed to open database:", e)


client = InferenceClient(api_key="note")

def llm_request(messages, model="microsoft/Phi-3.5-mini-instruct", maxtokens=500):
    completion = client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=maxtokens
    )
    print(completion.choices[0].message)
    return completion, completion.choices[0].message

def prompt(subject, audi_level, description):
    prompt = [
        {
            "role": "system",
            "content": f"You are a teacher with hands-on experience in {subject}. Your tasks is to a create table of contents of course base on user small description. Be careful user need this course for a specific {audi_level} level of audience."
        },
        {
            "role": "user",
            "content": description
        }
    ]
    return prompt


try:
    # user inputs
    subject = input("Enter your subject: ")
    if not subject:
        raise ValueError("Subject cannot be empty.")
    audi_level = input("Enter your Audience level (Beginner | Intermediate | Advance): ")
    if not audi_level:
        raise ValueError(f"Audience cannot be empty.")
    desc = input("Provide a clear explanation about your course: ")
    if not desc:
        raise ValueError("Course description cannot be empty.")
    
    # prompt for llm.
    llm_prompt = prompt(subject, audi_level, desc)
    print(llm_prompt)

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")
