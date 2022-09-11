from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from applicant.models import Artist as ArtistModel
# Create your models here.

class Art(models.Model):
    class Meta:
        db_table = 'art'
    def __str__(self):
        return f'{self.name}'

    name = models.CharField("작품명",max_length=64)
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE)
    number = models.IntegerField("호수", validators=[MinValueValidator(1), MaxValueValidator(500)])
    price = models.IntegerField("가격", default=0, validators=[MinValueValidator(0)])
    create_date = models.DateTimeField(auto_now_add=True)