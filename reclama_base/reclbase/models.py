from django.db import models
from django.contrib.auth.models import AbstractUser



# Модель ресположения изделий
class Location(models.Model):
    vch_no = models.IntegerField(verbose_name='Номер войсковой части')
    address = models.TextField(verbose_name='Адрес расположения')

    class Meta:
        verbose_name_plural = 'Расположение'
        verbose_name = 'Расположение'
        ordering = ['vch_no']


# Модель контрактов гарантийного обслуживания 
class Project(models.Model):
    project_no = models.CharField(max_length=50, verbose_name='Номер проекта')
    with_npo = models.CharField(max_length=100, verbose_name='Номер контракта/договора с НПО машиностроения', unique=True)
    with_mzkt = models.CharField(max_length=100, verbose_name='Контракт с ОАО "МЗКТ"', unique=True)

    class Meta:
        verbose_name_plural = 'Договора'
        verbose_name = 'Договор'
        ordering = ['project_no']

        
# Модель данных по изделиям
class Item(models.Model):
    ITEM_TYPE = (
        ('TZA', '3Т55-ТЗА'),
        ('TPA', '3С55-ТПА'),
    )
    item_type = models.CharField(max_length=3, choices=ITEM_TYPE, verbose_name='Тип изделия')
    item_no = models.IntegerField(verbose_name='Заводской номер изделия')
    item_frame = models.CharField(max_length=17, unique=True, verbose_name='Заводской номер шасси')
    item_engine = models.CharField(max_length=10, unique=True, verbose_name='Заводской номер двигателя')
    item_tn_to = models.CharField(max_length=50, verbose_name='ТН отправки на НПО машиностроения')
    item_tn_from = models.CharField(max_length=50, verbose_name='ТН получения шасси с ОАО "МЗКТ"')

    class Meta:
        verbose_name_plural = 'Изделия'
        verbose_name = 'Изделие'
        ordering = ['item_no', 'item_type']


# Модель записей рекламационныз актов
class Reclamacia(models.Model):
    mileage = models.IntegerField(verbose_name='Пробег шасси км')
    operating_time_frame = models.IntegerField(verbose_name='Наработка шасси м/ч')
    operating_time_dg1 = models.IntegerField(verbose_name='Наработка малого дизель-генератора м/ч')
    operating_time_dg2 = models.IntegerField(verbose_name='Наработка большого дизель-генератора м/ч')
    description = models.TextField(verbose_name='Описание обнаруженного дефекта')
    notice_from = models.CharField(max_length=50, verbose_name='Уведомление от НПО машиностроения')
    notice_to = models.CharField(max_length=50, verbose_name='Уведомление на ОАО "МЗКТ"')
    recl_akt_from = models.CharField(max_length=50, verbose_name='Рекламационный акт от НПО машиностроения')
    recl_akt_to = models.CharField(max_length=50, verbose_name=' Рекламационный акт на ОАО "МЗКТ"')
    ai_to = models.CharField(max_length=50, verbose_name='Акт исследования на НПО машиностроения')
    ai_from = models.CharField(max_length=50, verbose_name='Акт исследования от ОАО "МЗКТ"')
    aur_from = models.CharField(max_length=50, verbose_name='Акт удовлетворения рекламации от НПО машиностроения')
    aur_to = models.CharField(max_length=50, verbose_name='Акт удовлетворения рекламации на ОАО "МЗКТ"')

    class Meta:
        verbose_name_plural = 'Рекламационные акты'
        verbose_name = 'Рекламационная работа'
        ordering = ['notice_from']


class ReclUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Пользователь активирован')
    send_messages = models.BooleanField(default=False, verbose_name='Слать оповещения')

    class Meta(AbstractUser.Meta):
        pass