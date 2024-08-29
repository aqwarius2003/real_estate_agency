from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', db_index=True, null=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField(verbose_name='New_building',
                                       null=True, blank=True)
    likes = models.ManyToManyField(User, through='Like', blank=True, related_name='liked_flates',
                                   verbose_name='Кто лайкнул', )

    @property
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался', related_name='complaints')
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира, на которую пожаловались',
                             related_name='complaints')
    text = models.TextField('Текст жалобы')

    class Meta:
        verbose_name = 'жалобу'
        verbose_name_plural = 'жалобы'

    def __str__(self):
        return f'Жалоба от {self.user.username} \nна квартиру {self.flat}'


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name='user_likes')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flat_likes')

    class Meta:
        unique_together = ('user', 'flat')

    def __str__(self):
        return f'{self.user.username} лайкнул {self.flat.address}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True, db_column='owner')
    phonenumber = models.CharField('Номер владельца', max_length=20, db_index=True)
    pure_phone = PhoneNumberField('Нормализованный номер владельца', region="RU", blank=True)
    flats = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры в собственности'
    )

    def __str__(self) -> str:
        return self.owner'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
