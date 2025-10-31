Topics Covered: 
- Python basics
- OOP (classes, inheritance)
- Data visualization (Matplotlib)
- Files, Exceptions, API. 

Skills Developed: 
Python Programming
- Python syntax and fundamentals
- Working with modules and imports
- Reading/writing files

Object-Oriented Programming (OOP)
- Creating classes and objects,  Inheritance. 
-  Method overriding

Data Visualization
- Matplotlib library
- Creating line charts, bar charts
- Plotting data points
- Customizing plots (labels, titles, colors)
- Visualizing trends and patterns

API Integration
- Making HTTP requests
- Working with JSON data
  
Mini Project: Weather Dashboard
Django: User can save favorite cities
API: OpenWeatherMap API for real-time data
Matplotlib: Temperature trends, precipitation graphs
OOP: Weather, City, Forecast classes
Features: 7-day forecast, compare cities. 
Goal: To Display weather data.


## **Project Structure**
```
weather_dashboard/
├── weather/
│   ├── models.py (City, WeatherData, UserSettings)
│   ├── views.py (dashboard, city_detail, search)
│   ├── forms.py (CitySearchForm, SettingsForm)
│   ├── utils.py (API calls, chart generation)
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── city_detail.html
│   │   └── search.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── charts/
├── manage.py
└── requirements.txt
```

## **Stack Summary**
### Backend:
- Django 5.2
- OpenWeatherMap API
- Requests library

### Frontend:
- Bootstrap 4/5
- Weather icons 
- Responsive design

### Visualization:
- Matplotlib (temperature, humidity charts)

### Database:
- SQLite (development)
- PostgreSQL (production)
