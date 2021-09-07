# Django-Movie-API

A simple Django REST API project that provides movie information. It retrieves the information from https://www.omdbapi.com (an OPEN RESTful API web service), stores it in the database, and displays it to the Django Admin Site. Users can also add comments to the movies.

## Description:
* **Show All Movie Information:**  
Every movie information can be retrieved using the URL: "(localhost)/api/movie-list". All the movie information presents in the database will be shown in JSON format.
* **Search Specific Movie:**  
Use the URL parameter to search a movie by title. For example: "(localhost)/api/search-movie/{MOVIE TITLE}" will search for the specified movie. First of all, the specified movie will be searched in the database. If not found, then the movie information will be retrieved from "https://www.omdbapi.com/" using public API Key and movie title. As an example, "https://www.omdbapi.com/?t=Titanic&apikey=1154146a". After movie information is retrieved from the website, it'll be saved in the local database.
* **Search All Comments:**  
All the available comments can be retrieved using the URL: "(localhost)/api/comment-list". All the comments along with the associated movie information present in the database will be shown in JSON format.
* **Create Comment:**  
Comments can be POSTED using the URL: "(localhost)/api/create-comment". Comment ID, comment description and associated movie ID need to be provided in JSON format to post a comment. 
For Example: 
{
  "id": 1,
  "description": "Great Movie!",
  "movie_id": 1 
}

## Notes:
1. You can change database info from "movie-database/settings.py" file.
2. Create a local database and run "python manage.py makemigrations" & "python manage.py migrate" commands in the terminal to migrate model into database.
3. Create a superuser to access the Django Admin Site. Run: "python manage.py createsuperuser"
4. URL patterns are mentioned in "api/urls.py"
5. Run "python manage.py runserver" commands in the terminal to run the program.

## Upcoming Developments:
1. The complete development of this project is in progress. The project will be extended into a **Movie Review Web Application**.
2. **Angular** will be as a framework from Front-End Development.
3. Users will be able to Login/Register.
4. Users will be able to view movie information and post/read comments. Also, they can write reviews about movies.
