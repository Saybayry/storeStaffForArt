
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




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

## вопрос поиска и связи таблиц товаров и их подвидов я решил реализовать через мультитэйб наследование
## возникла проблема в поиске из родителя свойств доступных в дочерних моделях
## это проблему я решил черех связь OneToOneField
## по умолчанию это поле пустое, и в админке не отображается
## для заполнения я использую сигнал @receiver(post_save, sender=albomForArt) с методом post_save
## т.е. дествия происходят после сохранеия модели, я ее повторно вызываю и незначаю в OneToOneField родительскую модель
## все дочернии модели я решил делать по данному образцу
## уточнение создание дочерней модели создается на оснр=ове таблицы родительсой, и в род модели отображаются своства которые были унасл
class albomForArt(productForArt):
   product_for_art = models.OneToOneField(productForArt , on_delete=models.DO_NOTHING, related_name="albom",blank=True, null=True,editable = False)
   numberOfPages = models.IntegerField(default=10,verbose_name="количество станиц" )
   class Meta:
       verbose_name = u'альбомы и скечбуки'
       verbose_name_plural = u'альбомы и скечбуки'
   def __str__(self):
       return str(self.title)
## перехват сигнала и перезаполнения занчения OneToOneField
@receiver(post_save, sender=albomForArt)
def calc_ac_total(sender, instance, **kwargs):
    if str(instance.product_for_art) == "None":
        instance.product_for_art = instance.productforart_ptr
        instance.save()


class paintForArt(productForArt):
   product_for_art = models.OneToOneField(productForArt , on_delete=models.DO_NOTHING, related_name="paint",blank=True, null=True,editable = False)
   colors = models.IntegerField(default=10,verbose_name="просто поле, что докопался то?" )
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
       return str(self.title)
@receiver(post_save, sender=paintForArt)
def calc_ac_total(sender, instance, **kwargs):
    if str(instance.product_for_art) == "None":
        instance.product_for_art = instance.productforart_ptr
        instance.save()


class albomForArt(productForArt):
   product_for_art = models.OneToOneField(productForArt , on_delete=models.DO_NOTHING, related_name="albom",blank=True, null=True,editable = False)
   numberOfPages = models.IntegerField(default=10,verbose_name="количество станиц" )
   class Meta:
       verbose_name = u'альбомы и скечбуки'
       verbose_name_plural = u'альбомы и скечбуки'
@receiver(post_save, sender=albomForArt)
def calc_ac_total(sender, instance, **kwargs):
    if str(instance.product_for_art) == "None":
        instance.product_for_art = instance.productforart_ptr
        instance.save()

class typeProductForArt(models.Model):
    class Meta:
        verbose_name = u'вид продукции'
        verbose_name_plural = u'виды продукции'
    title = models.CharField(max_length=200, default="none")
    def __str__(self):
        return self.title
