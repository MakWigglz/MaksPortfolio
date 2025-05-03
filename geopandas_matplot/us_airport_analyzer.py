import csv
import matplotlib.pyplot as plt
import geopandas as gpd  # using alias gpd throughout
from shapely.geometry import Point

# Module-level variables
DATA_FILE = 'airports.csv'
COUNTRY_TO_PLOT = 'United States'

# Class to represent an Airport
class Airport:
    def __init__(self, iata, name, city, state, country, longitude, latitude):
        self.iata = iata
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        try:
            self.longitude = float(longitude)
            self.latitude = float(latitude)
        except ValueError:
            print(f"Warning: Could not convert longitude/latitude to float for {name} ({iata}).")
            self.longitude = None
            self.latitude = None

    def __str__(self):
        return (f"IATA: {self.iata}, Name: {self.name}, City: {self.city}, "
                f"State: {self.state}, Country: {self.country}, Lon: {self.longitude}, Lat: {self.latitude}")

# Function to load airport data from CSV
def load_airport_data(filename):
    airports = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airports.append(Airport(
                    row['iata'], row['name'], row['city'], row['state'],
                    row['country'], row['longitude'], row['latitude']
                ))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return airports

# Function to filter airports by country
def filter_by_country(airports, country):
    return [airport for airport in airports if airport.country == country and airport.longitude is not None and airport.latitude is not None]

# Class to visualize US airport locations on a map
class USAirportMapVisualizer:
    def __init__(self, airports):
        self.airports = airports

    def plot_us_airports(self, title="USA Airport Locations"):
        # Create a GeoDataFrame from the airport data
        geometry = [Point(airport.longitude, airport.latitude) for airport in self.airports]
        gdf = gpd.GeoDataFrame(self.airports, geometry=geometry, crs="EPSG:4326")

        # Load U.S. states shapefile using a direct URL (since datasets.get_path is deprecated)
        us_states = gpd.read_file("https://github.com/nvkelso/natural-earth-vector/raw/master/110m_cultural/ne_110m_admin_0_countries.shp")
        us_states = us_states[us_states["ADMIN"] == "United States of America"]

        # Create the plot
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        us_states.plot(ax=ax, color='lightgray', edgecolor='black')
        gdf.plot(ax=ax, marker='o', color='blue', markersize=20, label='Airports')

        # Add labels for a few prominent airports
        for i, row in gdf.head(15).iterrows():
            ax.annotate(row['iata'], xy=(row.geometry.x, row.geometry.y), xytext=(3, 3),
                        textcoords="offset points", fontsize=8, color='black')

        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_title(title)
        ax.legend(loc='upper left')
        # Adjust plot bounds based on the U.S. states geometry bounds
        ax.set_xlim(us_states.total_bounds[0] - 5, us_states.total_bounds[2] + 5)
        ax.set_ylim(us_states.total_bounds[1] - 2, us_states.total_bounds[3] + 2)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Main execution block
if __name__ == "__main__":
    all_airports = load_airport_data(DATA_FILE)
    if all_airports:
        us_airports = filter_by_country(all_airports, COUNTRY_TO_PLOT)
        visualizer = USAirportMapVisualizer(us_airports)
        visualizer.plot_us_airports(title="USA Airport Locations")
    else:
        print("No airport data loaded. Check the CSV file.")
