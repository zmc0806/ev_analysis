#!/usr/bin/env python
# coding: utf-8

# In[1]:


import osmnx as ox
import networkx as nx
import folium
from shapely.geometry import LineString, MultiLineString
from shapely.ops import linemerge


# In[2]:


# Define the coordinates for SDG&E and EV charger
sdge_location = (32.82434409454857, -117.1429236351)
ev_charger_location = (32.831882293954735, -117.15902477363302)

# Create a road network graph around the SDG&E location
G = ox.graph_from_point(sdge_location, dist=3000, network_type='drive')

# Find the nearest nodes to the start and end locations
orig_node = ox.distance.nearest_nodes(G, sdge_location[1], sdge_location[0])
dest_node = ox.distance.nearest_nodes(G, ev_charger_location[1], ev_charger_location[0])

# Calculate the shortest path between the nodes
route = nx.shortest_path(G, orig_node, dest_node, weight='length')

# Get the route geometry and attributes
route_gdf = ox.routing.route_to_gdf(G, route, weight='length')

# Merge all route geometries into one single continuous line
if len(route_gdf.geometry) > 1:
    merged_line = linemerge(MultiLineString(route_gdf.geometry.values))
else:
    merged_line = route_gdf.geometry.iloc[0]

# Calculate the total route length
route_length = route_gdf['length'].sum()

# Estimate travel time assuming an average speed of 40 km/h
average_speed_kmh = 40
travel_time_minutes = (route_length / 1000) / (average_speed_kmh / 60)

# Print results
print(f"The driving distance from SDG&E to the selected EV charger is {route_length:.2f} meters.")
print(f"Estimated travel time is approximately {travel_time_minutes:.2f} minutes.")

# Create an interactive map
m = folium.Map(location=sdge_location, zoom_start=15)

# Add markers for the start and end locations
folium.Marker(
    location=sdge_location, popup="SDG&E (Starting Point)", icon=folium.Icon(color="green")
).add_to(m)
folium.Marker(
    location=ev_charger_location, popup="EV Charger (Destination)", icon=folium.Icon(color="red")
).add_to(m)

# Add the full route to the map
folium.PolyLine(
    [(point[1], point[0]) for point in merged_line.coords],
    color="blue",
    weight=5,
    tooltip=f"Total Route Length: {route_length:.2f} meters",
).add_to(m)

# Add each segment of the route with additional information
for i, geom in enumerate(route_gdf.geometry):
    length = route_gdf.iloc[i]["length"]
    coords = [(point[1], point[0]) for point in geom.coords]
    folium.PolyLine(
        coords,
        color="purple",
        weight=3,
        tooltip=f"Segment {i+1}: {length:.2f} meters",
    ).add_to(m)

# Display the map in Jupyter Notebook
m  # Display the map inline in the notebook

# Save the map as an HTML file
map_file = "Interactive_output/enhanced_route_map.html"
m.save(map_file)
print(f"Interactive map saved to {map_file}. Open it in a web browser to view.")


# In[5]:


m


# In[4]:


fig, ax = ox.plot_graph_route(G, route, node_size=0)


# In[ ]:




