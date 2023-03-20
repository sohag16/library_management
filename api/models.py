from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(to='Author')
    summary = models.TextField(max_length=1000)
    genre = models.ManyToManyField(to='Genre')
    language = models.OneToOneField(to='Language', on_delete=models.SET_NULL, null=True)
    no_of_copy = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    student = models.OneToOneField(to='auth.User', on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=12, unique=True)
    branch = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"

class Borrower(models.Model):
    student = models.ForeignKey(to='student', on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(to='book', on_delete=models.SET_NULL, null=True)
    issued_date = models.DateTimeField(null=False, blank=False)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} borrowed {self.book}"

class Review(models.Model):
    choices = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    reviewer = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=1, choices=choices, default="0")

    def __str__(self):
        return f"{self.reviewer} rated {self.rating} for {self.book}"