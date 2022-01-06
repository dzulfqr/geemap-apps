import streamlit as st
import geemap
import json
import os
import requests
from geemap import geojson_to_ee, ee_to_geojson
from ipyleaflet import GeoJSON, Marker, MarkerCluster

def app():
    st.title("Membuat Marker Cluster")
    
    keys = list(geemap.basemaps.keys())[1:]

    basemap = st.selectbox("Pilih Peta Dasar", keys)
    m = geemap.Map(center=(40, -100), zoom=4, width=700, height=500)
    
    url = 'https://github.com/giswqs/geemap/raw/master/examples/data/us-cities.json'
    r = requests.get(url)

    json_data = json.loads(r.content.decode("utf-8"))
        
    maker_cluster = MarkerCluster(markers=[Marker(location=feature['geometry']['coordinates'][::-1]) for feature in json_data['features']], name = 'Markers')
    
    m.add_layer(maker_cluster)
    m.add_basemap(basemap)
    m.to_streamlit()
