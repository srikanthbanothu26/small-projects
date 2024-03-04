"""Create a GUI application which is used to search for movie information by the 
name of the movie or name of director.
1. To build the GUI, you can use any GUI library such as Tkinter, PyQt, etc.
2. You need to use the Movie API's to get the movie information. (use free API's)
3. When user searches for a movie, the application should display the movie information 
such as movie name, director, release date, etc.
4. We also need to store the movies history of the movie in a database.
(use SQLite database or mysql database)
5. When user searches for a movie, the application should check if the movie is 
already present in the database. If yes, then it should display the movie information 
from the database. If not, then it should get the movie information from the API and 
store it in the database and display it to the user.
6. If no movie is found, then display a message to the user saying "No movie found".

"""
from tkinter import *
import sqlite3
import requests
from PIL import Image, ImageTk
from io import BytesIO

win = Tk()
movie_search = StringVar()
conn = sqlite3.connect("movie3.db")
cursor = conn.cursor()
create_table = """
CREATE TABLE IF NOT EXISTS movie_data (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,year1 TEXT,directo TEXT,Actors TEXT,Rated TEXT,Released TEXT,Runtime TEXT,Genre TEXT,Boxoffice VARCHAR(300),Poster TEXT)
"""
search_query = """SELECT id, title, Poster FROM movie_data WHERE title LIKE ?"""
insert_data_query = """INSERT INTO movie_data (title, year1, directo, Actors, Rated, Released, Runtime, Genre, Boxoffice, Poster) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

cursor.execute(create_table)


def api_search(movie_name):
    movie_data.delete(1.0, "end")
    api_key = "your api key"
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    resp = requests.get(url)
    data = resp.json()
    if not data.get("Error", False):
        moviedata = f"\nTitle: '{data['Title']}',\nYear: '{data['Year']}',\nDirector: '{data['Director']}',\nActors:'{data['Actors']}',\nRated: '{data['Rated']}'',\nReleased: '{data['Released']}',\nRuntime: '{data['Runtime']}'',\nGenre: '{data['Genre']}',\nBoxOffice: '{data['BoxOffice']}' "
        movie_data.insert(INSERT, moviedata)

        # Fetch poster image
        poster_url = data.get("Poster")
        if poster_url and poster_url != "N/A":
            poster_image = fetch_and_display_poster(poster_url)
            display_poster(poster_image)
        return (
            data["Title"].lower(),
            data["Year"],
            data["Director"],
            data["Actors"],
            data["Rated"],
            data["Released"],
            data["Runtime"],
            data["Genre"],
            data["BoxOffice"],
            poster_url,
        )
    else:
        moviedata = f"\nTitle for '{movie_name}' not found!\nKindly enter a valid movie name!!"
        movie_data.insert(INSERT, moviedata)


def fetch_and_display_poster(poster_url):
    img_data = requests.get(poster_url)
    poster_image = Image.open(BytesIO(img_data.content))
    return poster_image


def display_poster(poster_image):
    aspect_ratio = poster_image.width / poster_image.height
    new_width = win.winfo_width()
    new_height = int(new_width / aspect_ratio)
    poster_image = poster_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    poster_image = ImageTk.PhotoImage(poster_image)
    bg_label.config(image=poster_image)
    bg_label.image = poster_image  # Keep a reference to avoid garbage collection


def db_search(movie_name):
    cursor.execute(search_query, ("%" + movie_name + "%",))
    result = cursor.fetchall()
    return result  # [(), (), ()] or []


def insert_into_movie_data(movie_id, title, poster_url):
    if movie_id:
        movie_data.delete(1.0, "end")
        message = f"\nMovie ID: {movie_id}, Title: {title}\n"
        movie_data.insert(INSERT, message)

        # Fetch and display poster
        if poster_url and poster_url != "N/A":
            poster_image = fetch_and_display_poster(poster_url)
            display_poster(poster_image)
    else:
        movie_data.delete(1.0, "end")
        message = f"\nNo matching movie found.\n"
        movie_data.insert(INSERT, message)


def search():
    movie_name = movie_search.get()
    result = db_search(movie_name)
    print("Db result:", result)
    if result:
        for row in result:
            movie_id, movie_title, poster_url = row[0], row[1], row[2]
            message = f"\nMovie ID: {movie_id}, Title: {movie_title}\n"
            movie_data.insert(INSERT, message)
            # Fetch and display poster
            if poster_url and poster_url != "N/A":
                poster_image = fetch_and_display_poster(poster_url)
                display_poster(poster_image)
    else:
        print("Searching in API")
        result =api_search(movie_name)
        if result:
            existing_movie = db_search(result[0])
            if existing_movie:
                existing_movie_data = existing_movie[0]
                movie_id = existing_movie_data[0]
                message = f"\nTitle '{movie_name}' already exists in the database.\nMovie ID: {movie_id}\n"
                movie_data.insert(INSERT, message)
            else:
                print("Inserting in DB")
                cursor.execute(insert_data_query, result)
                conn.commit()
                print("Inserted")

bg_label = Label(win)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame1 = Frame(win, borderwidth=2)
frame1.pack()

entry = Entry(frame1, width=50, fg="black", textvariable=movie_search)
entry.pack(pady=10)
btn = Button(
    win,
    text="Search Movie",
    command=search,
)
btn.pack(pady=10)
movie_data = Text(win, width=30, height=13, fg="red")
movie_data.pack()

mainloop()
