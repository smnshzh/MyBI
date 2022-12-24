from django.db import models

class GoodsMainGroup(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    class Meta:
        verbose_name = "1-گروه اصلی محصول"
        verbose_name_plural = '1-گروه های اصلی'
    def __str__(self):
        return self.name    
class GoodsSubGroup(models.Model):

    code = models.IntegerField(unique = True)
    mainGroup = models.ForeignKey(to=GoodsMainGroup,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=225)

    class Meta:
        verbose_name = "2-زیر گروه محصول"
        verbose_name_plural = "2-زیر گروه محصولات"
    def __str__(self):
        return self.name     

class GoodsDivideGroup(models.Model):

    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)

    class  Meta:
        db_table = ''
        managed = True
        verbose_name = '3-گروه جدا کننده'
        verbose_name_plural = '3-جداکنندگان'
    def __str__(self):
        return self.name     
    
class Good(models.Model):

    code = models.IntegerField(unique = True)
    name = models.CharField(max_length=225)
    group = models.ForeignKey(to= GoodsSubGroup,on_delete=models.DO_NOTHING)
    dgroup = models.ForeignKey(to=GoodsDivideGroup,on_delete=models.DO_NOTHING)
    inBox = models.IntegerField()

    def mainGroup(self):
        return self.group.mainGroup.name

    class Meta:

        verbose_name = "4-نام محصول"
        verbose_name_plural = '4-نام محصولات'
    def __str__(self):
        return self.name     


# ------ اطلاعات مراکز
    
class Dc(models.Model):

    code= models.IntegerField(unique=True)  
    name = models.CharField(max_length=225)
    ggroups = models.ManyToManyField(to=GoodsMainGroup,related_name="GoodsCanSAle")
    activation = models.BooleanField(default=False)
    class Meta:
        verbose_name = "5-مرکز اصلی"
        verbose_name_plural = "5-مراکز اصلی"
    def __str__(self):
        return self.name
class Barache(models.Model):

    code = models.IntegerField()
    name = models.CharField(max_length = 225)
    mainDc = models.ForeignKey(to=Dc,on_delete=models.DO_NOTHING)
    activation = models.BooleanField(default=False)
    class Meta:
        verbose_name = "6-مرکز فروش"
        verbose_name_plural = "6-مراکز فروش"
    def __str__(self):
        return self.name


class DistrictManager(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDcs = models.ManyToManyField(Dc,related_name="MainDC")

    class Meta:
        verbose_name= "7-مدیر منطقه"
        verbose_name_plural = "7-مدیران مناطق"
    def __str__(self):
        return self.name
CHOISE = [
    (1,"مدیر"),
    (2,"رئیس")
]
class Manager(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDc = models.ForeignKey(Dc,on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=4,choices=CHOISE)
    class Meta:
        verbose_name="8-مدیر شعبه"
        verbose_name_plural = "8-مدیریت شعب"
    def __str__(self):
        return f"{self.position} {self.name}"
class Superviseur(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDc = models.ForeignKey(Dc, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name = "9-سرپرست"
        verbose_name_plural = "9-سرپرستان"

    def __str__(self):
        return self.name

class SaleLine(models.Model):

    code = models.IntegerField()
    name = models.CharField(max_length=225)
    divideGroup = models.ManyToManyField(GoodsDivideGroup)
    class Meta:
        verbose_name = "10-لاین فروش"
        verbose_name_plural = "10-لاین های فروش"
    def __str__(self):
        return self.name

class CostumersActivity(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=225)
    class Meta:
        verbose_name = "11-فعالیت مشتری"
        verbose_name_plural = f"11-فعالیتها"
    def __str__(self):
        return self.name

class SalerActivity(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=225)
    costumerActivity = models.ManyToManyField(CostumersActivity)

    class Meta:
        verbose_name = ""