# GSBG Technologies Chatbot



This repository contains the source code for a custom chatbot application developed for GSBG Technologies. The application utilizes a pre-built knowledge base to provide specific and relevant responses to user queries.

## Table of Contents

* Features
* Project Structure
* Getting Started
* Usage

## Features

* **Custom Knowledge Base:** The chatbot is driven by a localized knowledge base built from a provided PDF (`knowledge/KB.pdf`).


* **Knowledge Base Generation:** Includes a dedicated script (`build_kb.py`) for processing the PDF and creating the chatbot's knowledge base.


* **Web Application Interface:** The project features a main application script (`app.py`), likely providing a web or API interface for user interaction.



## Project Structure

The repository (`gsbgProject`) is organized as follows:

* **`chatbot-gsbg-main/`**: The core application directory.


* **`app.py`**: The primary application file (e.g., a Flask or FastAPI web server).


* **`build_kb.py`**: A utility script used to generate or update the knowledge base.


* **`knowledge/`**: A directory designated for storing the chatbot's source material and generated data.


* **`KB.pdf`**: The PDF document serving as the foundation for the chatbot's knowledge.


* **`KB2.pdf`**: A secondary PDF document, likely containing additional or supplemental information for the knowledge base.




* **`README.md`**: Project documentation.


* **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.





## Getting Started

To set up the project locally:

1. Clone the repository to your local machine.
2. Navigate to the `chatbot-gsbg-main` directory.
3. *(Note: specific dependency installation instructions (e.g., `requirements.txt`) are not available in the provided structure, but you will likely need to install the necessary Python packages for the web framework and NLP tools used.)*

## Usage

1. **Build the Knowledge Base:** Before running the application, you may need to generate the knowledge base from the provided PDFs. Run the build script:
```bash
python build_kb.py
```
2.  **Run the Application:** Start the main chatbot application:
```bash
python app.py
```
