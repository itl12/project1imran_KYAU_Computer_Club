from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from dateutil.relativedelta import relativedelta  # install it using pip
import uuid 

# Create your models here.

class Notice(models.Model):
    heading = models.CharField(max_length=300)
    date = models.DateField(verbose_name='Will be held on or from today')
    body = models.TextField(blank=True, null=True) 
    pdf = models.FileField(blank=True, null=True, upload_to='notice_file')
    slug = models.SlugField(max_length=300, unique=True)

    class Meta():
        ordering = ['-id']

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        return super().save(**kwargs)


    def days_left(self):
        today = timezone.now().date()
        days_left = (self.date - today).days

        if days_left > 0:
            return f'{days_left} day{"s" if days_left != 1 else ""} left'
        elif days_left == 0:
            return 'Today'
        else:
            # Calculate how far in the past
            delta = today - self.date

            if delta.days < 30:
                return f'{delta.days} day{"s" if delta.days != 1 else ""} past'
            elif delta.days < 365:
                months_past = relativedelta(today, self.date).months
                return f'{months_past} month{"s" if months_past != 1 else ""} past'
            else:
                years_past = relativedelta(today, self.date).years
                return f'{years_past} year{"s" if years_past != 1 else ""} past'
    
    def __str__(self):
        return f"{self.heading[:40]}"+ '...' if len(self.heading) > 40 else self.heading + f" | {self.date}"


class Notice_images(models.Model):
    notice = models.ForeignKey(Notice, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notice_image')

    def __str__(self):
        return f'{self.notice.heading}'
    class Meta():
        ordering = ['notice', 'pk']

class RoutineModel(models.Model):
    routine_pdf = models.FileField(upload_to='notice_file', verbose_name='Routine pdf')
    routine_photo = models.ImageField(upload_to='routine_photo', verbose_name='Routine photo',  help_text="To convert the pdf into jpg visit https://smallpdf.com/pdf-converter or <a href='https://smallpdf.com/pdf-converter' target='_blank'><span style='color:green;font-size:20px;'>click here</span></a>")
    date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta():
        verbose_name = 'Update previous routine'

    def __str__(self):
        return f'last updated {self.update_date} {self.routine_pdf}'
