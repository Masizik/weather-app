# Weather App
## Web application with Python Django Framework + RESTful APIs,  It supports the following operation for searching: 
- search by city
- search by weather description
## Details
### The app is based on Django Framework, Javascript, HTML, CSS, Bootstrap and JQuery.
## The app uses two RESTful APIs:
### https://api.openweathermap.org/ - Weather API for forecast
- GET https://api.openweathermap.org/data/2.5/weather?q=' + {name_of_the_city} + '&units=metric&appid=' - get current weather by city
- GET https://api.openweathermap.org/data/2.5/forecast?q=' + {name_of_the_city} + '&units=metric&appid= - get 3-hour weather forecast 5 days
### https://pixabay.com/api/ - Picture API for generating random pictures. With this API app gets background and card picture
- GET https://pixabay.com/api/?key={API_KEY} + {name_of_the_city} - get random picture for background image by city name
- GET https://pixabay.com/api/?key={API_KEY} + {weather_description} - get random picture for card image by weather description
## Scrennshot
![Снимка от 2023-05-04 14-55-54](https://user-images.githubusercontent.com/59261346/236196915-d59f636f-4c3e-4f8d-a036-0448041061e8.png)
