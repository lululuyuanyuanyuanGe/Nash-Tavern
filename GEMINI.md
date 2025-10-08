# GEMINI.md

## Project Overview

This project, "nash-tavern," is a Python-based job application automation tool. It is designed to automate the process of finding and applying for jobs. The tool uses a browser automation library to navigate job websites, and leverages the Google Gemini Pro language model to extract and process job information. The project also includes functionality for parsing and tailoring resumes to specific job postings.

## Key Files

*   `main.py`: The main entry point for the application. It kicks off the job search process.
*   `jobFetcher.py`: Contains the logic for scraping job postings from a list of URLs. It uses a browser agent to extract job details and structure them using the `JobPosting` schema.
*   `schema.py`: Defines the Pydantic `JobPosting` model, which specifies the data structure for job postings (title, company, location, description, requirements, and application URL).
*   `resume.py`: Includes functions for parsing resumes from a URL and tailoring them to specific job descriptions. It also has a placeholder for generating a new resume in PDF format.
*   `pyproject.toml`: The project configuration file, specifying the project name and Python version.

## Building and Running

### Dependencies

The project requires the following Python libraries:

*   `pydantic`
*   `python-dotenv`
*   `browser_use` (This appears to be a local or custom library and is not listed in `pyproject.toml`)

You can install the dependencies from `requirements.txt` if it exists, or install them manually:

```bash
pip install pydantic python-dotenv
```

### Environment Variables

The project uses a `.env` file to manage API keys for the Google AI services. Create a `.env` file in the root directory with the following content:

```
GOOGLE_API_KEY="your_google_api_key"
```

### Running the Application

You can run the different parts of the application using the following commands:

*   To start the main job search:
    ```bash
    python main.py
    ```
*   To fetch job details from a list of URLs:
    ```bash
    python jobFetcher.py
    ```

## Development Conventions

*   **Asynchronous Operations:** The project uses `asyncio` for concurrent web scraping tasks.
*   **Data Modeling:** Pydantic is used for data validation and modeling (see `schema.py`).
*   **Environment Management:** `python-dotenv` is used to load environment variables from a `.env` file.
*   **Modular Structure:** The code is organized into modules with distinct responsibilities (e.g., `jobFetcher.py`, `resume.py`).
