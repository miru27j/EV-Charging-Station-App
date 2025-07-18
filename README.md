# 🚗 Smart Real-Time EV Charging Station Navigation App

This Kivy-based app helps electric vehicle (EV) users locate nearby charging stations on an interactive map. It fetches real-time station data using the OpenChargeMap API and displays markers on the map for quick navigation.

---

## Features

- Interactive map using `kivy_garden.mapview`
- Fetches charging station data dynamically via OpenChargeMap API
- Displays charging stations as map markers
- Simple and user-friendly interface with a “Find Charging Stations” button

---

## How It Works

When you tap the **Find Charging Stations** button, the app requests charging station data (limited to 5 stations for demo) and adds map markers for each location.

---

## Code Snippet

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
import requests

class ChargingStationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a MapView centered at San Francisco
        self.mapview = MapView(zoom=10, lat=37.7749, lon=-122.4194)

        # Button to fetch charging station locations
        fetch_button = Button(text="Find Charging Stations", size_hint=(1, 0.1))
        fetch_button.bind(on_press=self.fetch_charging_stations)

        # Add the map and button to the layout
        layout.add_widget(self.mapview)
        layout.add_widget(fetch_button)
        
        return layout

    def fetch_charging_stations(self, instance):
        try:
            response = requests.get("https://api.openchargemap.io/v3/poi/?output=json&countrycode=US&maxresults=5")
            stations = response.json()
            
            for station in stations[:5]:
                lat = station["AddressInfo"]["Latitude"]
                lon = station["AddressInfo"]["Longitude"]
                marker = MapMarker(lat=lat, lon=lon)
                self.mapview.add_widget(marker)

        except Exception as e:
            print("Error fetching stations:", e)

if __name__ == "__main__":
    ChargingStationApp().run()
