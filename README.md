# bookswaplibrary
[Model](/bookswaplibrary/docs/images/community-library-model.png)
# bookswap-reboot
features: bookclub - organsises the same book. if enough of the same book are in the database it can suggest bookclub

from django.db import models
from django.contrib.auth.models import User as AuthUser

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"

class User(models.Model):
    # If you want Django's built-in auth, use OneToOne with AuthUser
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True)
    join_date = models.DateField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=50, unique=True, blank=True, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    condition = models.CharField(max_length=50, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    review_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} on {self.book}"

class BookClub(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    is_bookswap = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'club')

    def __str__(self):
        return f"{self.user} in {self.club}"

class BookClubDiscussion(models.Model):
    club = models.ForeignKey(BookClub, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    discussion_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Discussion in {self.club} about {self.book}"

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Loan of {self.book} to {self.borrower}"

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserver = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Reservation of {self.book} by {self.reserver}"
