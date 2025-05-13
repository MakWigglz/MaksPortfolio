import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

# 1. Create Shapely geometry objects
point1 = Point(0, 0)
point2 = Point(1, 1)
line = LineString([(2, 2), (3, 3), (4, 2)])
polygon = Polygon([(0, 0), (0, 2), (2, 2), (2, 0)])

# 2. Create a GeoSeries
geometry = [point1, point2, line, polygon]
geo_series = gpd.GeoSeries(geometry, crs="EPSG:4326")  # Set CRS to WGS 84

print("--- GeoSeries ---")
print(geo_series)
print(f"\nGeoSeries CRS: {geo_series.crs}")

# 3. Create a Pandas Series for attributes
data = {'name': ['Point A', 'Point B', 'Line AB', 'Square']}
attribute_series = gpd.GeoSeries(data) # Note: This will be a Series of strings, not geometries

# 4. Create a GeoDataFrame
geo_df = gpd.GeoDataFrame(attribute_series, geometry=geo_series, crs="EPSG:4326")

print("\n--- GeoDataFrame ---")
print(geo_df)
print(f"\nGeoDataFrame CRS: {geo_df.crs}")

# 5. Perform a basic spatial operation: buffer
buffered_points = geo_df[geo_df.geometry.type == 'Point'].geometry.buffer(0.5)

print("\n--- Buffered Points (GeoSeries) ---")
print(buffered_points)

# 6. Perform a spatial predicate: intersects
# Create a test polygon
test_polygon = Polygon([(0.5, 0.5), (0.5, 1.5), (1.5, 1.5), (1.5, 0.5)])
test_geo_series = gpd.GeoSeries([test_polygon], crs="EPSG:4326")

# Check which geometries in our GeoDataFrame intersect with the test polygon
intersections = geo_df.intersects(test_geo_series[0])

print("\n--- Intersections with Test Polygon ---")
print(intersections)

# You can also filter the GeoDataFrame based on the intersection
intersecting_geometries = geo_df[intersections]
print("\n--- Intersecting Geometries ---")
print(intersecting_geometries)
