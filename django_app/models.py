from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
#
class Menu(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    age = models.IntegerField(default=25)

    def __str__(self):
        return self.name

class Item(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='Menus')
    Item_name = models.CharField(max_length=30,primary_key=True)
    calories = models.IntegerField(default=2500)
    price = models.FloatField(default=100)

    def __str__(self):
        return self.Item_name

class Drink(models.Model):
    item = models.OneToOneField(Item,on_delete=models.CASCADE,primary_key=True)
    caffeine = models.IntegerField()

    @property
    def cus_caffeine(self):
        return str(self.caffeine)


class Person(models.Model):
    person_name = models.CharField(max_length=50)
    age=models.PositiveIntegerField(default=25)
    description = models.TextField()
    email = models.EmailField(null=True)
    DOJ = models.DateField(auto_now=True)
    emp_photo = models.ImageField(null=True,upload_to='uploadsPerson/')

    def __str__(self):
        return self.person_name

class Club(models.Model):
    club_name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person)    #many to many example

    def __str__(self):
        return self.club_name


class Employee(models.Model):
    emp_id=models.IntegerField("Employee_ID",primary_key=True)

    def __str__(self):
        return str(self.emp_id)

class Details(models.Model):
    emp_unique=models.OneToOneField(Employee,on_delete=models.CASCADE,)
    emp_name=models.CharField("Employee_Name",primary_key=True,max_length=25)
    DOJ=models.DateField(auto_now=True)  #automatically adds current date, this field not shows in admin site
    email_id = str(emp_name)+'sat@com'  #need to check
    emp_photo=models.ImageField(upload_to ='uploads/')   #folder automatically creates

    def __str__(self):
        return self.emp_name

class Skill(models.Model):
    skill_choices = (('p', 'Python'), ('j', 'Java'), ('js', 'Javascript'),('DB','SQL'),('a','REST_API'))  #select one from choice
    emp_skill=models.ForeignKey(Employee,on_delete=models.CASCADE)
    skill=models.CharField("Select_skill",max_length=2,choices=skill_choices)  #drop box is automatically created for listing skills
    exp=models.PositiveIntegerField("Years of Experience")
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  #validators limit the rating should be 1-5.

    def __str__(self):
        return self.emp_skill