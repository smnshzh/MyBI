from django.db import models
from basicData.models import *

MONTHCHOISE = [
    ("1", "فروردین"),
    ("2","اردیبهشت"),
    ("3", "خرداد"),
    ("4", "تیر"),
    ("5", "مرداد"),
    ("6", "شهریور"),
    ("7", "مهر"),
    ("8", "آبان"),
    ("9", "آذر"),
    ("10", "دی"),
    ("11", "بهمن"),
    ("12", "اسفند")
]


class PorsatnGroup(models.Model):
    month = models.CharField(max_length=20, choices=MONTHCHOISE)
    year = models.IntegerField()
    center = models.ForeignKey(Barache, on_delete=models.DO_NOTHING)
    tgroups = models.ManyToManyField(GoodsSubGroup, related_name="targetgroups")
    qnty = models.IntegerField()
    def groupList(self):
        blanky = ""
        for item in self.tgroups.values_list("name"):
            blanky.join(item)
        return blanky

    class Meta:

        verbose_name = "تعریف تارگت شعبه"
        verbose_name_plural = "تعریف تارگت های شعب"

    def __str__(self):
        return f"تارگت {self.month}/{self.year} شعبه {self.center} گروه {self.groupList()}"

class SalerTargets(models.Model):

    saler = models.ForeignKey(Saler,on_delete=models.DO_NOTHING)
    month = models.CharField(max_length=20, choices=MONTHCHOISE)
    year = models.IntegerField()
    tgroups = models.ManyToManyField(GoodsSubGroup)
    qnty = models.IntegerField()
    accept = models.BooleanField()

    class Meta:
        verbose_name = "تارگت فروشنده"
        verbose_name_plural = "تارگت فروشندگان"


