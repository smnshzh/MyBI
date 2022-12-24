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
    groups = models.ManyToManyField(to=GoodsMainGroup)
    lines = models.ManyToManyField(to=GoodsDivideGroup)
    class Meta:
        verbose_name = "مرکز اصلی"
        verbose_name_plural = "مراکز اصلی"
