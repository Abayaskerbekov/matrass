from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField("Название", max_length = 100)
    visit = models.CharField("Типы", max_length = 200)
    name2 = models.CharField("месяц", max_length = 100)
    image = models.ImageField("изображение", upload_to="img_suppliers/")
    bool1 = models.BooleanField(default=True)


    verbose_name = "Товары"
    verbose_name_pluaral = "Товар"


    def __str__(self):
        return self.name



class Tovar(models.Model):
    name = models.CharField("Название", max_length = 100)
    visit = models.PositiveIntegerField("Размеры")
    name2 = models.CharField("Типы", max_length = 100)
    image = models.ImageField("Нравиться фото", upload_to="img_suppliers/")
    bool1 = models.BooleanField(default=True)


    verbose_name = "Товары"
    verbose_name_plural = "Товары"


    def __str__(self):
        return self.name



class Product_2(models.Model):
    name = models.CharField("Название", max_length=200)
    name2 = models.CharField("Одинатонные", max_length=100)
    image = models.ImageField("Изображение", upload_to="img_suppliers/")
    visit = models.JSONField("Размер")
    have = models.PositiveIntegerField("Количество")
    created_at = models.DateTimeField("Дата")
    bool1 = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    @property
    def have_label(self):
        if self.have <= 3:
            return f"Осталось {self.have} товара"


    verbose_name = "Хиты продаж"
    verbose_name_plural = "Хиты продаж"



class Card_product(models.Model):
    image = models.ImageField("Изображение", upload_to="img_suppliers/")
    visit = models.CharField("Типы", max_length = 100)
    name2 = models.CharField("Информация", max_length = 150)
    text = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    name = models.CharField("Навание", max_length = 100)
    image2 = models.ImageField("Фото нравиться", upload_to="img_suppliers/")
    favourites = models.CharField("Избранное", max_length = 100)
    basket = models.CharField("В корзину", max_length = 100)
    favourites2 = models.BooleanField(default=True)
    basket2 = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    verbose_name = "Карточка товара"
    verbose_name_plural = "Карточка товара"



class Favourites(models.Model):
    name = models.CharField("Избранное", max_length = 100)
    image = models.ImageField("Изображение", upload_to="img_suppliers/")
    name2 = models.CharField("Название", max_length = 100)
    visit = models.CharField("Типы", max_length = 100)
    img = models.ImageField("Фото нравиться", upload_to="img_suppliers/")
    bool1 = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    verbose_name = "Избранное"
    verbose_name_plural = "Избранное"



class Order(models.Model):
    name = models.CharField("Название", max_length = 100)
    organization = models.CharField("Наименование организации", max_length = 100)
    contact_person = models.CharField("Контактное лицо", max_length = 100)
    phone = models.CharField("Номер телефона", max_length = 100)
    emile = models.EmailField("Emile", blank=True)

    city = models.CharField("Город", max_length = 100)
    street = models.CharField("Улица", max_length = 100)
    house = models.CharField("Дом", max_length = 100)
    comment = models.TextField("Комментарий", blank=True)

    total_price = models.DecimalField("Итого", max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name


    verbose_name = "Оформление заказ"
    verbose_name_plural = "Оформление заказ"




class Contacts(models.Model):
    discription = models.TextField("Описание")
    phone = models.CharField("Телефон номер", max_length = 150)
    mail = models.CharField("Почта", max_length = 150)


    def __str__(self):
        return self.discription


    verbose_name = "Контакты"
    verbose_name_plural = "Контакты"



class Feedback(models.Model):
    name = models.CharField("Имя", max_length = 100)
    phone = models.CharField("Номер телефон", max_length = 100)
    emile = models.EmailField("Электронная почта", max_length = 100)
    comment = models.TextField("Комментарий")


    def __str__(self):
        return self.name


    verbose_name = "Обратная связь"
    verbose_name_plural = " Обратная связь"



class Basket(models.Model):
    product = models.CharField("Товары", max_length = 100)
    total = models.CharField("Итого", max_length = 100)
    name = models.CharField("Сумма заказ", max_length = 100)
    registration = models.CharField("Оформление", max_length = 150)
