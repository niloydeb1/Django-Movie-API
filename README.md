# Django-Movie-API

1. Show All Movie Information:
Every movie information can be retrieved using the URL: "localhost/api/movie-list". All the movie information presents in the database will be shown in JSON format.
2. Search Specific Movie:
Use the URL parameter to search a movie by title. For example: "localhost/api/search-movie/{MOVIE TITLE}" will search for the specified movie. First of all, the specified movie will be search in the database. If not found, then the movie information will be retrieved from "https://www.omdbapi.com/" using public API Key and movie title. As an example, "https://www.omdbapi.com/?t=Titanic&apikey=1154146a". After movie information is retrieved from the website, it'll be saved in the local database.
3. Search All Comments:
All the available comments can be retrieved using the URL: "localhost/api/comment-list". All the comments along with the associated movie information presents in the database will be shown in JSON format.
4. Create Comment:
Comments can be POSTED using the URL: "localhost/api/create-comment". Comment ID, comment description and associated movie ID needs to be provided in JSON format to post a comment. 
For Example: 
{
  "id": 1,
  "description": "Great Movie!",
  "movie_id": 1 
}

Notes:
1. You can change database info from "movie-database/settings.py" file.
2. Create a local database and run "python manage.py makemigrations" & "python manage.py migrate" commands in the terminal to migrate model into database.
2. URL patterns are mentioned in "api/urls.py"
3. Run "python manage.py runserver" commands in the terminal to run the program.
