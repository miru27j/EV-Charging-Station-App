from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
import requests

class ChargingStationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a MapView centered at a default location (San Francisco)
        self.mapview = MapView(zoom=10, lat=37.7749, lon=-122.4194)

        # Button to fetch charging station locations
        fetch_button = Button(text="Find Charging Stations", size_hint=(1, 0.1))
        fetch_button.bind(on_press=self.fetch_charging_stations)

        # Add the map and button to the layout
        layout.add_widget(self.mapview)
        layout.add_widget(fetch_button)
        
        return layout

    def fetch_charging_stations(self, instance):
        """ Fetch real-time charging station data (Mock API) """
        try:
            response = requests.get("https://api.openchargemap.io/v3/poi/?output=json&countrycode=US&maxresults=5")
            stations = response.json()
            
            # Loop through the stations and add markers
            for station in stations[:5]:  # Limit to 5 stations for demo
                lat = station["AddressInfo"]["Latitude"]
                lon = station["AddressInfo"]["Longitude"]
                marker = MapMarker(lat=lat, lon=lon)
                self.mapview.add_widget(marker)

        except Exception as e:
            print("Error fetching stations:", e)

# Run the App
ChargingStationApp().run()
