from django.shortcuts import render, redirect
from .models import Coordenadas
from .forms import *
import folium
from folium.plugins import MousePosition

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

    folium.CircleMarker(
        location=[26.420491, 80.314232],
        radius=50,
        popup="Laurelhurst Park",
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(map)


    folium.GeoJson(
        states[['STATE_NAME', 'geometry']].to_json(),
        name='States',
        show=True,
        style_function=lambda x: {
            'fillColor': 'lightblue',
            'color': 'black',
            'weight': 1,
            'fillOpacity':0.7
        },
        highlight_function=lambda x: {
            'fillOpacity':1
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['STATE_NAME'],
            aliases=['State name:'],
        ),
    ).add_to(map)
    
    # pp= folium.Html('<a href="'+ 'give your url here'+'"target="_blank">'+ 'popup text' + '</a>', script=True)
    # popup = folium.Popup(pp, max_width=2650)
    # current = folium.LatLngPopup()
    # folium.Marker(location=[26.420491, 80.314232], popup=popup).add_to(map)
    
    # folium.Marker(
    #     popup = f'<input type="text" value="{location[0]}, {location[1]}" id="myInput"><button onclick="myFunction()">Copy location</button>'
    # ).add_to(map)
    
    # folium.LatLngPopup().add_to(map)
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
