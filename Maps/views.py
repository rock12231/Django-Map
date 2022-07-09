from django.shortcuts import render, redirect
from .models import Coordenadas
from .forms import *
import folium

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
    
       
    coordenadas = list(Coordenadas.objects.values_list('lat','lon'))[-1]
    map = folium.Map(coordenadas)
    folium.Marker(coordenadas).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    
 
    
    folium.LayerControl().add_to(map)
    map = map._repr_html_()
    context = {'map': map }
    return render(request, 'Maps/maps.html', context)
