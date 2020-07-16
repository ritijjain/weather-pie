# WeatherPie v1.0

[weatherpie.herokuapp.com](https://weatherpie.herokuapp.com/)

WeatherPie gives you the current weather and suggests you what to wear based on the forecast.

## Prerequisites
* [Python 3.8](https://www.python.org/downloads/) or greater
* [Pipenv](https://pypi.org/project/pipenv/)
* [OpenWeatherMap API](https://openweathermap.org/api) key

## Quick Start
Initialize pipenv:

```
pipenv install -r requirements.txt
pipenv shell
```
Generate secret key:

```
python
>>> import secrets
>>> secrets.token_hex(24)
>>> exit()
```

Set environment variables:

`SECRET_KEY` = generated hex key

`OPEN_WEATHER_API_KEY` = OpenWeatherMap API key

Run Django migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Start localhost server:
```
python manage.py runserver
```
Navigate to http://localhost:8000/

## Future Feature Update

Planned features to be added in future updates.

* Ability for the user to set temperature threshold for summer and winter clothing suggestions.
* Display clothing suggestions for the next week based on the daily forecast data.
* Display icons for clothing suggestions.
* Email notification support.
* Optimizations for the mobile version of the site.
* More accurate UVI data.
* Updated UI.