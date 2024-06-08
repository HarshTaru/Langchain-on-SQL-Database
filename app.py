
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
""" You are an expert in converting English questions to SQL queries!

The SQL database has the name chinook.db and has the following tables:

employees table stores employee data such as EmployeeId, LastName, FirstName, etc. It also has a field named ReportsTo to specify who reports to whom.
customers table stores customer data such as CustomerId, FirstName, LastName, Company, Address, etc.
invoices & invoice_items tables: these two tables store invoice data. The invoices table stores invoice header data, and the invoice_items table stores the invoice line items data.
artists table stores artist data. It is a simple table that contains ArtistId and Name.
albums table stores data about a list of tracks. Each album belongs to one artist. However, one artist may have multiple albums. It contains AlbumId, Title, and ArtistId.
media_types table stores media types such as MPEG audio and AAC audio files. It contains MediaTypeId and Name.
genres table stores music types such as rock, jazz, metal, etc. It contains GenreId and Name.
tracks table stores the data of songs. Each track belongs to one album. It contains TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, and UnitPrice.
playlists & playlist_track tables: playlists table stores data about playlists. Each playlist contains a list of tracks. Each track may belong to multiple playlists. The playlist_track table is used to reflect this relationship. The playlists table contains PlaylistId and Name. The playlist_track table contains PlaylistId and TrackId.
For example:
Example 1 - How many employees are there in the company?
The SQL command will be something like this:
SELECT COUNT(*) FROM employees;
Example 2 - List the names of all customers.
The SQL command will be something like this:
SELECT FirstName, LastName FROM customers;
Example 3 - Retrieve all albums by the artist "Queen".
The SQL command will be something like this:
SELECT Title FROM albums JOIN artists ON albums.ArtistId = artists.ArtistId WHERE artists.Name = 'Queen';
Example 4 - How many tracks are there in the Rock genre?
The SQL command will be something like this:
SELECT COUNT(*) FROM tracks JOIN genres ON tracks.GenreId = genres.GenreId WHERE genres.Name = 'Rock';
The SQL code should not have ``` in the beginning or end, and the word SQL should not be included in the output."""
]


# Streamlit App
st.set_page_config(page_title="TEXT2SQL")
st.header("TEXT2SQL")

question = st.text_input("Input your question here:", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    with st.spinner("Generating SQL query..."):
        try:
            # Generating SQL query from the question
            sql_query = get_gemini_response(question, prompt)
            st.text_area("Generated SQL Query:", sql_query)

            # Executing the SQL query and fetching results
            response = read_sql_query(sql_query, "chinook.db")

            # Displaying the results
            st.subheader("The Response is")
            for row in response:
                print(row)
                st.header(row)
        except Exception as e:
            st.error(f"An error occurred: {e}")

