from django.db import models


class PrizeDraw(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.name} - {self.created_at}'


class Winner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prize_draw = models.ForeignKey(PrizeDraw, related_name='winner_prize_draw', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.name} - {self.prize_draw} - {self.created_at}'