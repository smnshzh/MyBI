from django.db import models

class GoodsMainGroup(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    class Meta:
        verbose_name = "گروه اصلی محصول"
        verbose_name_plural = 'گروه های اصلی'
    def __str__(self):
        return self.name    
class GoodsSubGroup(models.Model):

    code = models.IntegerField(unique = True)
    mainGroup = models.ForeignKey(to=GoodsMainGroup,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=225)

    class Meta:
        verbose_name = "زیر گروه محصول"
        verbose_name_plural = "زیر گروه محصولات"
    def __str__(self):
        return self.name     

class GoodsDivideGroup(models.Model):

    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)

    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'گروه جدا کننده'
        verbose_name_plural = 'جداکنندگان'
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

        verbose_name = "نام محصول"
        verbose_name_plural = 'نام محصولات'
    def __str__(self):
        return self.name     


# ------ اطلاعات مراکز
    
class Dc(models.Model):

    code= models.IntegerField(unique=True)  
    name = models.CharField(max_length=225)
    ggroups = models.ManyToManyField(to=GoodsMainGroup,related_name="GoodsCanSAle")
    activation = models.BooleanField(default=False)
    class Meta:
        verbose_name = "مرکز اصلی"
        verbose_name_plural = "مراکز اصلی"
    def __str__(self):
        return self.name
class Barache(models.Model):

    code = models.IntegerField(unique=True)
    name = models.CharField(max_length = 225)
    mainDc = models.ForeignKey(to=Dc,on_delete=models.DO_NOTHING)
    activation = models.BooleanField(default=False)
    class Meta:
        verbose_name = "مرکز فروش"
        verbose_name_plural = "مراکز فروش"
    def __str__(self):
        return self.name


class DistrictManager(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDcs = models.ManyToManyField(Dc,related_name="MainDC")

    class Meta:
        verbose_name= "مدیر منطقه"
        verbose_name_plural = "مدیران مناطق"
    def __str__(self):
        return self.name
CHOISE = [
    (1,"مدیر"),
    (2,"رئیس")
]
class Manager(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDc = models.ForeignKey(Dc,on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=4,choices=CHOISE)
    class Meta:
        verbose_name="مدیر شعبه"
        verbose_name_plural = "مدیریت شعب"
    def __str__(self):
        return f"{self.position} {self.name}"
class Superviseur(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    activation = models.BooleanField(default=False)
    MainDc = models.ForeignKey(Barache, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name = "سرپرست"
        verbose_name_plural = "سرپرستان"

    def __str__(self):
        return self.name

class SaleLine(models.Model):

    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    divideGroup = models.ManyToManyField(GoodsDivideGroup)
    class Meta:
        verbose_name = "لاین فروش"
        verbose_name_plural = "لاین های فروش"
    def __str__(self):
        return self.name

class CostumersActivity(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    class Meta:
        verbose_name = "فعالیت مشتری"
        verbose_name_plural = f"فعالیتها"
    def __str__(self):
        return self.name

class SalerActivity(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=225)
    costumerActivity = models.ManyToManyField(CostumersActivity)

    class Meta:
        verbose_name = "فعالیت فروشنده"
        verbose_name_plural = "فعالیت فروشندگان"

    def __str__(self):
        return self.name

class Saler(models.Model):
    scode = models.IntegerField(unique=True)
    pcode = models.IntegerField()
    name = models.CharField(max_length=225)
    branch = models.ForeignKey(Barache,on_delete=models.DO_NOTHING)
    superviseur = models.ForeignKey(Superviseur,on_delete=models.DO_NOTHING)
    activity = models.ForeignKey(SalerActivity,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "فروشنده"
        verbose_name_plural = "فروشندگان"






