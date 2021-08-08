import random

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import PrizeDrawForm

from .models import PrizeDraw, Winner

def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PrizeDrawForm(request.POST)
        if form.is_valid():
            participants = form.cleaned_data["participants"].splitlines()
            quantity = form.cleaned_data["quantity"]
            winners = random.sample(participants, k=quantity)
            prize_draw = PrizeDraw.objects.create(name=form.cleaned_data['draw_name'])
            winners_db = []
            for i in winners:
                winners_db.append(Winner(name=i, prize_draw=prize_draw))
            Winner.objects.bulk_create(winners_db)
            return render(
                request,
                "app_draw/winners.html",
                {"form": form, "winners": winners},
            )
    else:
        form = PrizeDrawForm()
    last_winners = Winner.objects.all().order_by('-created_at')[:5]
    return render(request, "app_draw/index.html", {"form": form, "last_winners": last_winners})
