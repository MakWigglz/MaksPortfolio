import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Create the GeoSeries of points
s = gpd.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])

# Use the .plot() method to create a plot
s.plot()

# Add a title to the plot
plt.title("Plot of Points")

# Show the plot
plt.show()
