
# Course Content Generator using Hugging Face API and SQLite

This repository contains a Python-based application to generate course content dynamically using the **Hugging Face Phi-3.5-mini-instruct** model. Users can input a subject, audience level, and a course description. The app generates a detailed table of contents and stores the results in a SQLite database.

---

## Features
- Generate a course outline based on user-provided input.
- Save course details, prompts, and output in a SQLite database.
- Retrieve and view the course content directly after generating it.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/course-content-generator.git
   cd course-content-generator
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Instructions

### Create a Hugging Face API Token
1. Go to the [Hugging Face website](https://huggingface.co/).
2. Log in to your account or create one if you don’t already have an account.
3. Navigate to **Settings > Access Tokens**.
4. Create a new token:
   - Token type: **Write**
   - Name your token for identification.
5. Copy the generated token and replace `your_api_key` in the code:
   ```python
   client = InferenceClient(api_key="your_api_key")
   ```

### Run the Application
1. Start the program:
   ```bash
   python main.py
   ```

2. Enter the required inputs when prompted:
   - Subject (e.g., "Artificial Intelligence").
   - Audience Level (e.g., "Intermediate").
   - Course Description (e.g., "A beginner's course on AI basics, applications, and challenges.").

3. The program will:
   - Generate a detailed table of contents using Hugging Face's model.
   - Store the details in a SQLite database named `chat_hist.db`.

4. View the output in the console.

---

## File Descriptions

### Main Code
- **`main.py`**: The main entry point for the application.
- **`requirements.txt`**: Lists the Python dependencies for the project.

### Database
- **`chat_hist.db`**: The SQLite database file where course data is stored (automatically created if not present).

---

## How It Works

1. **Input:** The user provides the course subject, audience level, and description.
2. **Processing:** 
   - A prompt is constructed using this input and sent to Hugging Face's inference API.
   - The model generates a course outline based on the input description and audience level.
3. **Storage:** 
   - The inputs and generated content are saved to the SQLite database for future reference.
4. **Output:** The generated course content is displayed in the console.

---

## Notes

- **Database:** The database schema is automatically created if it doesn't exist.
- **API Token Security:** Never commit your API key to a public repository. Use environment variables or a `.env` file instead.

---

## Future Enhancements
- Add a feature to query and retrieve previously saved courses.
- Implement a user-friendly web interface using Flask or Gradio.
- Support for multiple models and user customization for prompt parameters.

---

## Dependencies
- [Hugging Face Hub](https://huggingface.co/docs/huggingface_hub)
- SQLite3 (built-in with Python)
- Python 3.7 or higher

---

## License
This project is licensed under the [MIT License](LICENSE).
