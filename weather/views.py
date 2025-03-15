from django.shortcuts import render
import requests

# Create your views here.
def home(request):
  return render(request, "index.html")

def weather(request):
  if request.method == "POST":
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")

    data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")

    data = data.json()
    
    return render(request, 'weather.html', {'data': data})
  else:
      return render(request, "index.html")