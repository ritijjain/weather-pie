from django.apps import AppConfig


class WeatherHomeConfig(AppConfig):
    name = 'weather_home'

    def ready(self):
        import weather_home.signals
