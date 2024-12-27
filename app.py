from huggingface_hub import InferenceClient
import sqlite3

# set llm   
def llm_request(messages, model="microsoft/Phi-3.5-mini-instruct", maxtokens=1000):
    client = InferenceClient(api_key="your_api_key")
    completion = client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=maxtokens
    )
    return completion, completion.choices[0].message.content

# llm prompt
def prompt(subject, audi_level, description):
    prompt = [
        {
            "role": "system",
            "content": f"You are a teacher with hands-on experience in {subject}. Your tasks is to a create table of contents of course base on user course description. Be careful user need this course for a specific {audi_level} level of audience."
        },
        {
            "role": "user",
            "content": description
        }
    ]
    return prompt

# create database
def database():
    connection = sqlite3.connect("chat_hist.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            level TEXT,
            prompt TEXT,
            output TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)    
    connection.commit()
    return cursor, connection

# save values in db
def save_response(sub, level, prompt, output, cursor, conn):
    cursor.execute("""
            INSERT INTO course (subject, level, prompt, output)
            VALUES (?, ?, ?, ?)
        """, (sub, level, prompt, output))
    conn.commit()
    conn.close()

# print response
def show_response(response):
    print(response)

# user input
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

    # course generation
    withHeader, response = llm_request(llm_prompt)

    # table creation
    cursor, conn = database()

    # store in db
    save_response(subject, audi_level, desc, response, cursor, conn)

    # show output
    show_response(response)

# show input error
except ValueError as ve:
    print(f"Input Error: {ve}")
# show other error
except Exception as e:
    print(f"Unexpected error: {e}")
