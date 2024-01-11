import random
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import TableWithResultsCoinToss


logger = logging.getLogger(__name__)


def heads_or_tails(request):

    coin: list = ["heads", "tails"]
    resalt: str = random.choice(coin)

    logger.info(f'heads_or_tails page accessed, get message: {resalt}')

    results_coin_toss = \
        TableWithResultsCoinToss(result_coin_toss=resalt)
    results_coin_toss.save()

    return HttpResponse(resalt)


def heads_or_tails_statistics(request, number_throws: int):

    resalt: dict = \
        TableWithResultsCoinToss().get_statistics(number_throws=
                                                  number_throws)

    return HttpResponse(str(resalt))
