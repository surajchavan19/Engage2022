# VIBING 








## Introduction
 VIBING is a simulated prototype that uses facial recognition to authenticate users inside cars, retrieves their Spotify playlists using Spotify API and sets the temperature of the car to their preferred temperature 

## Technologies Used
HTML, CSS, Bootstrap, JavaScript,Django, Python, SQLite, OpenCV, Spotify-API(Spotipy), face-recognition and Django HTTP

## Set-up
1) Download the zip-file or clone the repository.
2) Open the file in a code editor.
3) In the terminal open the directory in which the file is present
4) Download the dependencies 
   ```python
   pip3 install Django face-recognition cmake spotipy opencv-python
   ```
5) python3 manage.py makemigrations
6) python3 manage.py migrate
7) python3 manage.py runserver 0.0.0.0:8000
8) To open the web application
### On mobile
  To run the application the laptop and the phone should be connected to the same network
   ```python
   http://(Laptop's IP address):/face/signupform
   ```
   example: http://192.169.0.102:8000/face/signupform
### On laptop
      ```python
   http://0.0.0.0:8000/face/signupform 
   ```



