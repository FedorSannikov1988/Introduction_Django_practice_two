from django.db import models


class TableWithResultsCoinToss(models.Model):
    result_coin_toss = models.CharField(max_length=5)
    time_throw = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ResultsCoinToss: {self.result_coin_toss}, ' \
               f'data_and_time_throw: {self.time_throw}'

    @staticmethod
    def get_statistics(number_throws: int) -> dict:

        all_coin_toss = \
            TableWithResultsCoinToss.objects.order_by('-id')[:number_throws]

        heads: int = 0
        tails: int = 0
        heads_and_tails: int = 0

        for one_coin_toss in all_coin_toss:
            if one_coin_toss.result_coin_toss == "heads":
                heads += 1
            else:
                tails += 1
            heads_and_tails += 1

        return {"heads": heads/heads_and_tails, "tails": tails/heads_and_tails}
