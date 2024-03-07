from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File



class User(AbstractUser):
    phone_number = models.CharField(max_length=13,blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Employee(models.Model):
    user = models.OneToOneField(to="User", on_delete=models.CASCADE)
    profession = models.CharField(max_length=255 , blank=False)
    wages = models.PositiveIntegerField(default=10000000)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=255, null=True, blank=True)
    experience = models.IntegerField(default=1)
    work_time = models.DateTimeField()
    rating = models.FloatField(default=0)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.profession)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.address


class Cassa(models.Model):
    summa = models.PositiveIntegerField(default=1000000)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __int__(self):
        return self.summa


class Order(models.Model):
    client_name = models.CharField(max_length=55, unique=True, blank=False)
    client_phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    is_deliver = models.BooleanField(default=False)
    adress = models.CharField(max_length=255)
    car_name = models.CharField(max_length=77)
    car_number = models.CharField(max_length=255)
    master = models.ForeignKey(to=Employee, on_delete=models.PROTECT)
    problem = models.CharField(max_length=255)
    service_cost = models.PositiveIntegerField(default=1000000)
    didleni = models.DateTimeField()
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

   


class Paymet(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    paymet = models.IntegerField()
    date = models.DateTimeField()
    PAYMENT_TYPE = (
        (1,"Naqt pull"),
        (2,"Karta orqali"),
    )
    paymet_type = models.IntegerField(choices=PAYMENT_TYPE)
    admin = models.ForeignKey(to="Employee", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)


    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)



class Report(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.income)
        super().save(*args, **kwargs)



class Attends(models.Model):
    employee = models.ForeignKey(to="Employee", on_delete=models.CASCADE)
    day = models.DateField(auto_now=True)
    attent = models.BooleanField(default=False, blank=False)