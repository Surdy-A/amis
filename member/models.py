from distutils.command.upload import upload
import email
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.text import slugify
import datetime
from django.utils import timezone

LGA_CHOICES = (
     ('OS01', 'Atakunmosa East Central LCDA'),
     ('OS02', 'Atakunmosa West'),
     ('OS03', 'Atakunmosa West Central'),
     ('OS04', 'Ayedaade'),
     ('OS05', 'Ayedaade South LCDA'),
     ('OS06', 'Ayedire'),
     ('OS07', 'Ayedire South LCDA'),
     ('OS08', 'Boluwaduro'),
     ('OS09', 'Boluwaduro East LCDA'),
     ('OS10', 'Boripe'),
     ('OS11', 'Boripe North LCDA'),
     ('OS12', 'Ede East LCDA'),
     ('OS13', 'Ede North'),
     ('OS14', 'Ede North Area Council'),
     ('OS15', 'Ede South'),
     ('OS16', 'Egbedore'),
     ('OS17', 'Egbedore Area Council'),
     ('OS18', 'Egbedore South LCDA'),
     ('OS19', 'Ejigbo'),
     ('OS20', 'Ejigbo South LCDA'),
     ('OS21', 'Ejigbo West LCDA'),
     ('OS22', 'Ife Central'),
     ('OS23', 'Ife Central West LCDA'),
     ('OS24', 'Ife East'),
     ('OS25', 'Ife North'),
     ('OS26', 'Ife North Area Council'),
     ('OS27', 'Ife North Central LCDA'),
     ('OS28', 'Ife North West LCDA'),
     ('OS29', 'Ife Ooye LCDA'),
     ('OS30', 'Ife South'),
     ('OS31', 'Ife South West'),
     ('OS32', 'Ifedayo'),
     ('OS33', 'Ifedayo Area Council'),
     ('OS34', 'Ifelodun'),
     ('OS35', 'Ifelodun North Area Council'),
     ('OS36', 'Ifelodun North LCDA'),
     ('OS37', 'Ila'),
     ('OS38', 'Ila Central LCDA'),
     ('OS39', 'Ilesa East'),
     ('OS40', 'Ilesa North East LCDA'),
     ('OS41', 'Ilesa West'),
     ('OS42', 'Ilesa West Central LCDA'),
     ('OS43', 'Irepodun'),
     ('OS44', 'Irepodun South LCDA'),
     ('OS45', "Irewole"),
     ('OS46', 'Irewole North East LCDA'),
     ('OS47', 'Isokan'),
     ('OS48', 'Isokan South LCDA'),
     ('OS49', 'Iwo'),
     ('OS50', 'Iwo East LCDA'),
     ('OS51', 'Iwo West LCDA'),
     ('OS52', 'Obokun'),
     ('OS53', 'Obokun East LCDA'),
     ('OS54', 'Odo Otin'),
     ('OS55', 'Odo Otin North LCDA'),
     ('OS56', 'Odo Otin South LCDA'),
     ('OS57', 'Ola Oluwa'),
     ('OS58', 'Ola Oluwa South East LCDA'),
     ('OS59', 'Olorunda'),
     ('OS60', 'Olorunda Area Council'),
     ('OS61', 'Olorunda North LCDA'),
     ('OS62', 'Oriade'),
     ('OS63', 'Oriade South LCDA'),
     ('OS64', 'Orolu'),
     ('OS65', 'Orolu Area Council'),
     ('OS66', 'Osogbo'),
     ('OS67', 'Osogbo South LCDA'),
     ('OS68', 'Osogbo West LCDA'),
)

SCHOOL_TYPE_CHOICES = (
     ('Nursery', 'Nursery'),
     ('Primary', 'Primary'),
     ('Secondary', 'Secondary'),
     ('Islamiyyah', 'Islamiyyah'),
     ('Nursery+primary+secondary', 'Nursery+primary+secondary'),
     ('Nursery+primary+secondary+islamiyyah', 'Nursery+Primary+Secondary+Islamiyyah'),
     ('secondary+islamiyyah', 'Secondary + Islamiyyah'),
)

SCHOOL_OPERATING_TYPE_CHOICES = (
     ('Day', 'Day'),
     ('Boarding', 'Boarding'),
     ('Secondary', 'Secondary'),
     ('Day & Boarding', 'Day & Boarding'),
     ('Boarding Only', 'Boarding Only'),
)

STATE_GOV_STATUS_CHOICES = (
     ('Approved', 'Approved'),
     ('Under', 'Under Processing'),
     ('No', 'Not Yet Applied'),
)

FEDERAL_GOV_STATUS_CHOICES = (
     ('Registered', 'Registered'),
     ('Not Registered', 'Not Registered'),
)

BELONG_CHOICES = (
     ('Y', 'Yes'),
     ('N', 'No'),
)

OWNERSHIP_CHOICES = (
     ('S', 'Sole Proprietor'),
     ('P', 'NoPartnership'),
)

SEX = (
     ('M', 'Male'),
     ('F', 'Female'),
)

#School Name and Code Choice
SCHOOL_NAME__AND_CODE = (
     ('51241', 'ISLAMIC MODEL SCHOOL. IGANGAN - 51241'),
     ('61321', 'THE LIGHT NUR & PRY SCHOOL, ORILE- OWU - 61321'),
     ('61322', 'EPITOME MONTESSORI N/P SCH. ODE-OMU - 61322'),
     ('42501', 'FOMWAN N /P SCHOOL IREE - 42501'),
)

LG_NAME__AND_CODE = (
     ('51', 'ATAKUNMOSA WEST - 51'),
     ('61', 'AYEDAADE - 61'),
     ('42', 'BORIPE - 42'),
     ('11', 'EDE NORTH - 11'),
)

CLASS = (
     ('3', 'Grade 3'),
     ('4', 'Grade 4'),
     ('5', 'Grade 5'),
     ('6', 'Grade 6'),
)

class Member(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    slug = models.SlugField(max_length=200, db_index=True, default='')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(403, 482)],
                                     format='PNG',
                                     options={'quality': 95})

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Proprietor(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

#School
class School(models.Model):
    school_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    about = models.CharField(max_length=200, blank=True)
    school_type = models.CharField(max_length=200, blank=True, choices=SCHOOL_TYPE_CHOICES)
    state_government_status = models.CharField(max_length=200, blank=True, choices=STATE_GOV_STATUS_CHOICES)
    federal_government_status = models.CharField(max_length=200, blank=True, choices=FEDERAL_GOV_STATUS_CHOICES)
    cac_reg_number = models.CharField(max_length=200, blank=True)
    other_association = models.CharField(max_length=200, blank=True, choices=BELONG_CHOICES)
    association_details = models.CharField(max_length=200, blank=True)
    school_code = models.CharField(max_length=200, blank=True)
    lga_code = models.CharField(max_length=200, blank=True)
    proprietor = models.ForeignKey(Proprietor, on_delete=models.CASCADE)
    ownership = models.CharField(max_length=200, choices=OWNERSHIP_CHOICES)
    local_government = models.CharField(max_length=200, blank=True, choices=LGA_CHOICES)
    contact_person = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, default='')
    logo = models.ImageField(upload_to='img')
    logo_thumbnail = ImageSpecField(source='logo',
                                     processors=[ResizeToFill(884, 868)],
                                     format='PNG',
                                     options={'quality': 95})

    class Meta:
        ordering = ['school_name']
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):
       value = self.school_name
       self.slug = slugify(value, allow_unicode=True)
       super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('member:school_detail', args={self.slug})

#Workshop/Conference
class Delegate(models.Model):
    name = models.CharField(max_length=200)
    status_in_school = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    workshop_name = models.CharField(max_length=200, default='', blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    delegate = models.ForeignKey(Delegate, on_delete=models.CASCADE)
    year = models.CharField(max_length=200, default='')
    date = models.CharField(max_length=200, default='')
    venue = models.CharField(max_length=200, default='')
    amount = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['workshop_name']
        verbose_name_plural = "Workshops"

    def __str__(self):
        return self.workshop_name

class CalenderRegistration(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-year']

    def date(self):
        self.year = datetime.datetime.now()

    def __str__(self):
        return self.school.school_name

#Workshop/Conference


class Quiz(models.Model):
    candidate_name = models.CharField(max_length=200)
    candidate_class = models.CharField(max_length=200)
    candidate_image = models.ImageField(upload_to='img', default="")

    def __str__(self):
        return self.candidate_name

class Debate(models.Model):
    candidate_name = models.CharField(max_length=200)
    candidate_class = models.CharField(max_length=200)

    def __str__(self):
        return self.candidate_name

class Exhibition2(models.Model):
    candidate_name = models.CharField(max_length=200)
    candidate_class = models.CharField(max_length=200)

    def __str__(self):
        return self.candidate_name


class Exhibition(models.Model):
    candidate_name = models.CharField(max_length=200)
    candidate_class = models.CharField(max_length=200)

    def __str__(self):
        return self.candidate_name + self.candidate_class

#Academic Competition for Primary Category
class PrimaryCompetition(models.Model):
    competition_name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    quran = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    teacher_phone = models.CharField(max_length=200)
    principal_name = models.CharField(max_length=200)
    quiz = models.ManyToManyField(Quiz)
    khutbah = models.CharField(max_length=200)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    class Meta:
        ordering = ['school']

    def __str__(self):
        return self.competition_name

    def save(self, *args, **kwargs):
       value = self.competition_name
       self.slug = slugify(value, allow_unicode=True)
       super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('member:competition_detail', args={self.competition_name})


#Academic Category for JSS
class JSSCompetition(models.Model):
    competition_name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    quran = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    teacher_phone = models.CharField(max_length=200)
    principal_name = models.CharField(max_length=200)
    quiz = models.ManyToManyField(Quiz)
    pick_and_talk = models.CharField(max_length=200)
    ceative_writing = models.CharField(max_length=200)
    caligraphy = models.CharField(max_length=200)

    class Meta:
        ordering = ['school']

    def __str__(self):
        return self.competition_name

    def save(self, *args, **kwargs):
       value = self.competition_name
       self.slug = slugify(value, allow_unicode=True)
       super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('member:competition_detail', args={self.competition_name})

#Academic Category for SSS
class SSSCompetition(models.Model):
    competition_name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    quran = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    teacher_phone = models.CharField(max_length=200)
    principal_name = models.CharField(max_length=200)
    quiz = models.ManyToManyField(Quiz)
    essay_writing = models.CharField(max_length=200)
    debate = models.ManyToManyField(Debate)
    exhibition = models.ManyToManyField(Exhibition2)

    class Meta:
        ordering = ['school']

    def __str__(self):
        return self.competition_name

    def save(self, *args, **kwargs):
       value = self.competition_name
       self.slug = slugify(value, allow_unicode=True)
       super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('member:competition_detail', args={self.competition_name})

#Grading Exam Model
class Exam(models.Model):
    surname = models.CharField(max_length=200, default='')
    other_names = models.CharField(max_length=200, default='')
    student_class = models.CharField(max_length=200, blank=True, choices=CLASS)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default='')
    gender = models.CharField(max_length=200, default='', choices=SEX)
    date_of_birth = models.DateTimeField()

    class Meta:
        ordering = ['surname']
        verbose_name_plural = "Examination"

    def __str__(self):
        return self.surname

