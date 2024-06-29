# GameFolio

**Overview**

GameFolio is a web application that allows users to write a review of their game of choice and post it online for other users to see. Users can also search for games using several parameters such as name and genre and leave a review. The game page will show information about the game, its average rating and its reviews. The user will also have their own user page in which posts they have written will be displayed as well as the total number of likes they’ve received on their reviews and their own list of favourite games. The home page will be the hub where the most trending games and reviews will be put on display. 

<!--
```sh
python3 manage.py makemigrations \
&& python3 manage.py migrate \
&& python3 populate_gamefolio.py
```
-->

**Required to Run**
- Python 3.10
- Django 5.0.6
- Pillow
- django-registration-redux 2.13
- NumPy
- Requests