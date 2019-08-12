from django.db import models

# Create your models here.
class person_news(models.Model):
    person_height = models.IntegerField(verbose_name='身高(/cm)',unique=False)
    person_weight = models.IntegerField(verbose_name='体重(/kg)',unique=False)
    person_bmi = models.FloatField(verbose_name='BIM计算器',unique=False,max_length=4)
    time = models.DateTimeField(verbose_name='时间',auto_now_add=True)
    # def __str__(self):
    #     return self.person_height