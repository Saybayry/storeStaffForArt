

from django.db import models


class productForArt(models.Model):
    price = models.IntegerField(verbose_name="цена", default=0)
    title = models.CharField(max_length=300, verbose_name="название товара", null=True)
    description = models.CharField( max_length=1000,verbose_name="Описание товара", null=True)
    type = models.ForeignKey('typeProductForArt', on_delete=models.PROTECT)
    pictureProductForArt = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return str(self.title) + ' по цене' + str(self.price) + ' шт'
    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

class albomForArt(productForArt):

   product_for_art = models.OneToOneField(productForArt , on_delete=models.DO_NOTHING, related_name="albom",blank=True, null=True)
   numberOfPages = models.IntegerField(default=10,verbose_name="количество станиц" )
   def __str__(self):
       if str(self.product_for_art) == "None":
           self.product_for_art = self.productforart_ptr
           self.save()
       return str(self.title)

   class Meta:
       verbose_name = u'альбомы и скечбуки'
       verbose_name_plural = u'альбомы и скечбуки'


class paintForArt(productForArt):
   product_for_art = models.OneToOneField(productForArt , on_delete=models.DO_NOTHING, related_name="paint",blank=True, null=True)
   colors = models.IntegerField(default=10,verbose_name="количество станиц" )
   volumePaint = models.IntegerField(default=250 )
   TYPES_OF_PAINT =[
       ('oil_paint', 'масляная'),
       ('water_collor', 'акварель'),
       ('gouache_paint', 'гуаш'),
       ('acrylic_paint', 'акрил'),
       ('tempera_paint', 'темпер'),
   ]
   typePaint = models.CharField(max_length=30, choices=TYPES_OF_PAINT,
                                default="oil_paint",verbose_name="тип краски" )
   class Meta:
       verbose_name = u'краски'
       verbose_name_plural = u'краски'
   def __str__(self):
       if str(self.product_for_art) == "None":
           self.product_for_art = self.productforart_ptr
           self.save()
       return str(self.title)



class typeProductForArt(models.Model):
    class Meta:
        verbose_name = u'вид продукции'
        verbose_name_plural = u'виды продукции'
    title = models.CharField(max_length=200, default="none")
    def __str__(self):
        return self.title
