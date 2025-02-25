from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here.


class Member(models.Model):

    member = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profileimages', blank=True, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.member} {self.member.first_name} {self.member.last_name} {self.address.suburb} {self.image}'


class Address(models.Model):
    
    LOCATIONS = (
        ('h', 'Home'),
        ('b', 'Business'),
        ('l', 'Library'),
    )
    
    location_type = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        blank=True,
        default='e',
    ) 
    street_no = models.CharField(max_length=9)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postcode = models.CharField(max_length=9)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.street_no} {self.street} {self.suburb} {self.state} {self.postcode}'


class Author(models.Model):

    name = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
    

class Genre(models.Model):

    genre = models.CharField(max_length=200)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.genre
        

class Publisher(models.Model):

    publisher = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.publisher}'


class Book(models.Model):

    """Model representing a book (but not a specific copy of a book)."""
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    summary = models.TextField(max_length=500, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField(Genre)
    publisher = models.ManyToManyField(Publisher)
    image = models.ImageField(upload_to='images/bookimages', blank=True, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title}'
    
class BookImage(models.Model):

    image = models.ImageField(upload_to='images/bookimages', blank=True, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.image}'
    

class BookInstance(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    
    BOOK_CONDITION = (
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('bad', 'Bad'),
        ('dog_eared', 'Dog Eared'),
        ('water_damaged', 'Water Damaged'),
        ('missing_pages', 'Missing Pages'),
    )    
    condition = models.CharField(max_length=20, choices=BOOK_CONDITION)
    condition_notes = models.CharField(max_length=500, null=True)
    
    LOAN_STATUS = (
        ('on_loan', 'On loan'),
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('reserved', 'Reserved'),
    )
    status = models.CharField(max_length=20, choices=LOAN_STATUS)
    
    EXCHANGE_PREFERENCE = (
        ('swap', 'Swap'),
        ('loan', 'Loan'),
        ('gift', 'Gift'),
    ) 
    exchange_preference = models.CharField(max_length=20, choices=EXCHANGE_PREFERENCE, null=True)
     
    images = models.ManyToManyField('BookInstanceImage')
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.book.title}'
    
class BookInstanceImage(models.Model):

    image = models.ImageField(upload_to='images/bookinstanceimages', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        return f'{self.image} {self.description}'

class Swap(models.Model):

    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    request = models.BooleanField()
    accept = models.BooleanField()    

class Exchange(models.Model):

    date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="owner")
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrower")
    books = models.ManyToManyField('BookInstance')
    exchange_location = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_exchanged = models.DateField(null=True, blank=True)
    
