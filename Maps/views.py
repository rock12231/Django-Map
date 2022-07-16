from django.shortcuts import render, redirect
from django.views import View
from .models import Coordenadas, Crimes2001
from .forms import *
import folium
from folium.plugins import MousePosition
import pandas as pd

df = pd.read_csv("Maps/data/Crimes2001.csv")

def coordinates_form(request):
    coordinates = Coordenadas.objects.all()
    form = CoordinatesForm()

    if request.method == 'POST':
        form = CoordinatesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("maps")
    context = {
                'coordinates': coordinates,
                'form' : form,
            }
    return render(request, 'Maps/maps_form.html', context)


def maps(request): 
   
    coordenadas = list(Coordenadas.objects.values_list('lat','lon'))[-1]
    map = folium.Map(coordenadas)
    folium.Marker(coordenadas).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    
    folium.Circle(
        radius=100,
        location=[26.463437, 80.296537],
        popup="The Waterfront",
        color="crimson",
        fill=False,
    ).add_to(map)
    # data = folium.LatLngPopup().add_to(map)
    map.add_child(folium.LatLngPopup())
  
    
    # folium.Marker(popup = f'<input type="text" id="myInput"><button onclick="myFunction()">Copy location</button>').add_to(map)
    # location_center = [45.5236, -122.6750]
    # locations = [[45.5012, -122.6655],[45.5132, -122.6708],[45.5275, -122.6692],[45.5318, -122.6745]]

    # map = folium.Map(location_center, zoom_start=13)
    # for location in locations:
        # folium.Marker(
            # location=location,
            # popup = f'<input type="text" value="{location[0]}, {location[1]}" id="myInput"><button onclick="myFunction()">Copy location</button>').add_to(map)
        
    # folium.GeoJson(
    #     states[['STATE_NAME', 'geometry']].to_json(),
    #     name='States',
    #     show=True,
    #     style_function=lambda x: {
    #         'fillColor': 'lightblue',
    #         'color': 'black',
    #         'weight': 1,
    #         'fillOpacity':0.7
    #     },
    #     highlight_function=lambda x: {
    #         'fillOpacity':1
    #     },
    #     tooltip=folium.features.GeoJsonTooltip(
    #         fields=['STATE_NAME'],
    #         aliases=['State name:'],
    #     ),
    # ).add_to(map)
    
    # pp= folium.Html('<a href="'+ 'give your url here'+'"target="_blank">'+ 'popup text' + '</a>', script=True)
    # popup = folium.Popup(pp, max_width=2650)
    # current = folium.LatLngPopup()
    # folium.Marker(location=[26.420491, 80.314232], popup=popup).add_to(map)
    
    # folium.Marker(
    #     popup = f'<input type="text" value="{location[0]}, {location[1]}" id="myInput"><button onclick="myFunction()">Copy location</button>'
    # ).add_to(map)

    # map.add_child(folium.LatLngPopup())
    
    # formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

    # MousePosition(
    #     position="topright",
    #     separator=" | ",
    #     empty_string="NaN",
    #     lng_first=True,
    #     num_digits=20,
    #     prefix="Coordinates:",
    #     lat_formatter=formatter,
    #     lng_formatter=formatter,
    # ).add_to(map)

    
    folium.LayerControl().add_to(map)
    map = map._repr_html_()
    context = {'map': map }
    return render(request, 'Maps/maps.html', context)


class CrimeDetials(View):
    
    def get(self, request):
        tempDF = df.copy() 
        # tempDF = tempDF.head()
        # tempDF = tempDF.dropna()
        for i in range (len(tempDF)):
            tempDF.unique[i]
            
        
            data = {
                'caseno' : tempDF['caseno'][i],	
                'block' : tempDF['block'][i],
                'Type' : tempDF['Type'][i],
                'Type_desc' : tempDF['Type_desc'][i],
                'Where' : tempDF['Where'][i],
                'Arrest' : tempDF['Arrest'][i],
                'Domestic' : tempDF['Domestic'][i],
                'District' : tempDF['District'][i],
                'Community_area' : tempDF['Community_area'][i],
                'Year' : tempDF['Year'][i],
                'Latitude' : tempDF['Latitude'][i],
                'Longitude' : tempDF['Longitude'][i],
            }
            print(data,".......................")
            Crimes2001.objects.create(**data)
        return render(request, 'Maps/crime.html', { "dataT":tempDF.values.tolist()}) 
    
    def post(self, request):
        tempDF = df.copy() 
        for i in range (len(tempDF)):
            tempDF.unique[i]
            data = {
                    'caseno' : tempDF['caseno'][i],	
                    'block' : tempDF['block'][i],
                    'Type' : tempDF['Type'][i],
                    'Type_desc' : tempDF['Type_desc'][i],
                    'Where' : tempDF['Where'][i],
                    'Arrest' : tempDF['Arrest'][i],
                    'Domestic' : tempDF['Domestic'][i],
                    'District' : tempDF['District'][i],
                    'Community_area' : tempDF['Community_area'][i],
                    'Year' : tempDF['Year'][i],
                    'Latitude' : tempDF['Latitude'][i],
                    'Longitude' : tempDF['Longitude'][i],
                    }
            print(data,".......................")
        # Crimes2001.objects.create(**data) 
        context = Crimes2001.objects.all()
        return render(request, 'Maps/crime.html', {'context': context})