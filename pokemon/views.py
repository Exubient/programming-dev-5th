from django.shortcuts import render
from pokemon.models import pokemon,user,location,capture


def pokemon_list(request):
      qs=pokemon.objects.all()
      return render(request, 'pokemon/pokemon_list.html', {
            'pokemon_list':qs,
            })


def user_list(request):
      qs=user.objects.all()
      return render(request, 'pokemon/user_list.html', {
            'user_list':qs,
            })

def capture_list(request):
      qs=capture.objects.all()
      return render(request, 'pokemon/capture_list.html', {
            'capture_list':qs,
            })

def location_list(request):
      qs=location.objects.all()
      return render(request, 'pokemon/location_list.html', {
            'location_list':qs,
            })

def pokemon_rank(request):
      qs=location.objects.all()
      return render(request, 'pokemon/rank_list.html', {
            'location_list':qs,
            })
