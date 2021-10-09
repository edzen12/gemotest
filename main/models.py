from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
import qrcode.image.svg
import uuid


class Gemotest(models.Model):
    generate_number = models.IntegerField(default=int(str(uuid.uuid4().int >> 64)[0:8]))
    first_name = models.CharField(max_length=30)
    qr_code = models.ImageField(blank=True)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    number_of_phone = models.CharField(max_length=13)
    date_of_birth = models.DateField()
    email = models.EmailField()
    number_of_passport = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    date_of_give_bio = models.DateTimeField()
    date_completed = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.id}"

    def save(self, *args, **kwargs,):
        qr_code = qrcode.make(f'https://gemotest01.herokuapp.com/reference/{self.number_of_passport}')
        canvas = Image.new('RGB', (400, 400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_code)
        file_name = f"qr_code-{self.number_of_passport}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


    def get_name(self):
        first_letter = self.first_name[:1]
        rew = self.first_name[::-1]
        new_rew = rew[:-1]
        new_new = new_rew[:-1]
        last_letter = rew[:1]
        for i in new_new:
            new_new = new_new.replace(i, '*')
        new_first_name = first_letter + new_new + last_letter
        new_last_name = self.last_name[:1]
        return f"{new_first_name} {new_last_name}."
    
