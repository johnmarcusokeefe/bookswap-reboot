from django import forms
from .models import Address, Genre, BookInstance, Book, Author, Publisher, BookInstanceImage, Member, User

    
# class RegistrationForm(forms.Form):
#     
#     first_name =
#     last_name = 
#     email = forms.CharField(label='Email', max_length=100)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

class NewBookForm(forms.ModelForm):  
    class Meta:
        model = Book
        fields = ('isbn','title','author','summary','genre','publisher','image')

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('location_type', 'street_no', 'street', 'suburb', 'state', 'postcode', 'country')
        
class NewBookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ('book', 'status', 'condition', 'images', 'exchange_preference')
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name','external_link')

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('publisher','external_link')
        
class BookInstanceImageForm(forms.ModelForm):
    class Meta:
        model = BookInstanceImage
        fields = ('image','description')        
