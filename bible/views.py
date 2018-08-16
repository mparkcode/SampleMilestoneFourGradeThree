from django.shortcuts import render
import requests
from igdb_api_python.igdb import igdb
import os
from datetime import datetime
from .forms import IgdbSearchForm


# Create your views here.
def get_games(request):
    form = IgdbSearchForm()
    r = igdb(os.environ.get("IGDB_API_KEY"))
    games=[]
    igdb_search = request.GET.get("igdb_search")
    if igdb_search:
        result = r.games({
        'search': igdb_search,
        'fields' : ['name','summary', 'rating', 'url', 'screenshots', 'cover', 'first_release_date']
    })
        for game in result.body:
            if 'first_release_date' in game:
                game['first_release_date'] = datetime.utcfromtimestamp(int(game['first_release_date'] / 1000)).strftime('%Y/%m/%d')
            games.append(game)
        return render(request, "bible/search_bible.html", {'games':games, 'form':form})    
    return render(request, "bible/search_bible.html", {'games':games, 'form':form})
    
def game_detail(request):
    game_id = int(request.GET.get("game_id"))
    r = igdb(os.environ.get("IGDB_API_KEY"))
    result = r.games(game_id)
    for g in result.body:
        game = g
    if 'cover' in game:
        game['cover']['url']=game['cover']['url'].replace("t_thumb","t_cover_big")
    if 'first_release_date' in game:
        game['first_release_date'] = datetime.utcfromtimestamp(int(game['first_release_date'] / 1000)).strftime('%Y/%m/%d')
    return render(request, "bible/game_detail.html", {'game':game})