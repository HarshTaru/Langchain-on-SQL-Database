# Langchain-on-SQL-Database
# TEXT2SQL Streamlit App

This Streamlit application allows users to convert natural language questions into SQL queries using the Google Gemini model. The generated SQL queries are then executed against the Chinook database, and the results are displayed in the app.

## Features

- Convert natural language questions to SQL queries using Google Gemini.
- Execute the generated SQL queries against a SQLite database.
- Display the results of the SQL queries in the app.

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- SQLite3
- Google Generative AI SDK

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/text2sql.git
    cd text2sql
    ```

2. Install the required packages:
    ```bash
    pip install streamlit sqlite3 google-generativeai
    ```

3. Set up your Google API key:
    - Obtain your API key from Google Cloud Console.
    - Set the `GOOGLE_API_KEY` environment variable:
      ```bash
      export GOOGLE_API_KEY='your_google_api_key'
      ```

4. Ensure you have the `chinook.db` SQLite database in the project directory. You can download it from [here](https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite).

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter your question in natural language into the text input field and click the "Ask the question" button.

4. The app will generate a SQL query based on your question, execute it against the `chinook.db` database, and display the results.

## Code Overview

### Import Dependencies

```python
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
