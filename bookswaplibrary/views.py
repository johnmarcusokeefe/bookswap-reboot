from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from bookswaplibrary.models import Book, BookInstance, BookImage, BookInstanceImage, Member, User, Author, Address, Publisher, Author
from .forms import NewBookForm, MembershipForm, NewBookInstanceForm, AuthorForm, PublisherForm, RegistrationForm, BookInstanceImageForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core import mail

# Create your views here.
def index(request):
    """View function for home page of site."""

    member_count = Member.objects.all().count()
    title_count = Book.objects.all().count()
    book_instance_count = BookInstance.objects.all().count()
    
    user = request.user
    context = {
        'user': user,
        'member_count': member_count,
        'title_count': title_count,
        'book_instance_count': book_instance_count,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#
def author(request):
    
    if request.method == 'POST':
    
        authorform = AuthorForm(request.POST)
   
        # file is saved
        if authorform.is_valid():
            authorform.save()
    
    authorform = AuthorForm()
    
    
    authors = Author.objects.all()
    
    message = "none"
    context = {
        'message': message,
        'authorform': authorform,
        'authors': authors,
        }

    return render(request, 'author.html', context=context)
       

# Create your views here.
def book(request, book_id):
    """View function for home page of site."""

    owner_flag = False
    book = ""
    user = request.user
    member = user.groups.filter(name='Member').exists()
    book_detail = Book.objects.get(pk=book_id)
    book = Book.objects.filter(pk=book_id).values('id','isbn','title','author__name','summary','genre__genre','publisher__publisher')
        
    book_copies = BookInstance.objects.select_related('owner').filter(book=book_detail).values('id','book__title','owner__member__email','owner__address__suburb','condition','status','exchange_preference')
    
    print('owner flag', owner_flag)
    context = {
        'user': user,
        'member': member,
        'book': book,
        'book_copies': book_copies,       
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'book.html', context=context)
    

# image saves through book instance
def book_instance(request, book_id):
    """View function for home page of site."""
    status = ""
    condition = ""

    user = request.user
    member = user.groups.filter(name='Member').exists()
    book_instance = BookInstance.objects.get(pk=book_id)
    
    
    image_id = None
    if request.method == 'POST': # If the form has been submitted...
        image_id = request.POST['image_id']
        if image_id == None:
            book_instance_image = BookInstanceImage.objects.create(image=request.FILES['image'],description=request.POST['description'])
            book_instance_image.save()
            book_instance.images.add(book_instance_image)
            book_instance.save()
        else:
            print("delete image")


    book_data =  BookInstance.objects.all().filter(pk=book_id).values('id','book__title','book__id','condition','status')    
    #
    condition = book_data[0]['condition']
    status = book_data[0]['status']
    title_id = book_data[0]['book__id']
    
    context = {
        'user': user,
        'member': member,
        'book_instance': book_instance,
        'status': status,
        'condition': condition,
        'title_id': title_id,
        'book_instance_image_form': BookInstanceImageForm(),
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'book_instance.html', context=context)
# holds all book titles

def catalogue(request):

    # add book
    if request.method == 'POST': # If the form has been submitted...
    
        bookform = NewBookForm(request.POST,request.FILES)
        print(bookform.errors.as_data())
        if bookform.is_valid():
            # file is saved
            bookform.save()
            
        else:
            print("book not saved")
        
        
    user = request.user
    # members can add books 
    member = user.groups.filter(name='Member').exists()

    books = Book.objects.all()
#     for b in books:
#         images = BookImage.objects.filter(book=b)
#         for i in images:
#             print(i)
   
    print(books)
    # author_id = books.values('author')
#     for a in author_id:
#         print(Author.objects.filter(id=a['author']))
        
    context = {
        'book_list': books,
        'member': member,
        'new_book_form': NewBookForm(), 
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalogue.html', context=context)

# detail of book
def edit_book(request, id=-1):

    user = request.user
    # members can add books 
    member = user.groups.filter(name='Member').exists()
    
    if request.method == 'POST':
    
        if id == -1:
        
            pk = request.POST['book_id']
            book_instance = get_object_or_404(Book, pk=pk)
            edit_book_form = NewBookForm(instance=book_instance) 
        
        else:
            # update form
            book_instance = get_object_or_404(Book, pk=id)
            editform = NewBookForm(request.POST, request.FILES, instance=book_instance)
            editform.save()
            print("print save after edit", request.FILES)
            return redirect("/catalogue")
            
         # Check if the form is valid:
        
    
    context = {
        'member': member,
        'book_id': pk,
        'edit_book_form': edit_book_form,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'edit_book.html', context=context)
    
# detail of book
def edit_book_instance(request, id=-1):

    user = request.user
    # members can add books 
    member = user.groups.filter(name='Member').exists()
    
    if request.method == 'POST':
    
        if id == -1:
        
            pk = request.POST['book_id']
            book_instance = get_object_or_404(BookInstance, pk=pk)
            edit_book_instance_form = NewBookInstanceForm(instance=book_instance) 
        
        else:
            # update form
            book_instance = get_object_or_404(BookInstance, pk=id)
            editform = NewBookInstanceForm(request.POST, instance=book_instance)
            editform.save()
            print("print save after edit")
            return redirect("/profile")
            
         # Check if the form is valid:
        
    
    context = {
        'member': member,
        'book_id': pk,
        'edit_book_instance_form': edit_book_instance_form,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'edit_book_instance.html', context=context)

   
# member will list the book instances owned
def profile(request):

    user = request.user
    book_data = ""
    message = "none"
    bookform = ""
    member_details = ""
    member_exists = False
    memberform = MembershipForm()
    member_object = Member.objects.filter(member=user)
    print("member object", member_object)
    member_details = User.objects.filter(username=user).values()
    member = user.groups.filter(name='Member').exists()

    if request.method == 'POST':
    
        # add membership details
        memberform = MembershipForm(request.POST)
        
        if memberform.is_valid():

            saved_member = memberform.save()
            print(saved_member)
            
            user_id = User.objects.filter(username=user).values('id')
            user_instance = User.objects.get(pk=user_id[0]['id'])  
            
            # this saves the address
            member_instance = Member.objects.create(member=user_instance, address=saved_member, image=request.FILES['image'])
            member_instance.save()
            
            # have to create member first using admin
            user_instance.groups.add(Group.objects.get(name='Member'))
            user_instance.save()
        
    print("member object",member_object.values())
    member_exists = member_object.exists()
       
    if member_exists == True:
        print("member exists")
        bookform = NewBookInstanceForm()
    else:   
        form = MembershipForm()
        message = "please complete membership details to activate the ability to swap"
        
        # add address from member details form
    
    # adding book from form
    try:        
        id = Member.objects.all().filter(member=user).values('id')
        pk = id[0]['id']
        bookform = NewBookInstanceForm(request.POST, request.FILES)
        # file is saved
        if bookform.is_valid():
                
            newbook = bookform.save(commit=False)
            newbook.owner = Member.objects.get(pk=pk)
            newbook.save()
            print(newbook)                
    except Exception as err:   
        print("book not added", err)
        
    user_id = User.objects.filter(username=user).values('id')
    user_instance = User.objects.get(pk=user_id[0]['id'])
        
    #    
    # retrieves titles in members library
    #
    try:    
        id = Member.objects.all().filter(member=user).values('id')
        pk = id[0]['id']
        user_instance = Member.objects.get(pk=pk)
        # if no member create
        book_data =  BookInstance.objects.select_related('owner').filter(owner=user_instance).values('id','book__title','book__image',
           'condition','status','exchange_preference')
        #print(book_data)
        #
    except Exception as e:
            # 
        print(e)
               
    # membership completed on first login
    context = {
        'message': message,
        'member_details': member_details[0],
        'member_object': member_object,
        'member_book_list': book_data,
        'membership_form': memberform,
        'member_exists': member_exists,
        'new_book_instance_form': bookform,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profile.html', context=context)



def publisher(request):

    if request.method == 'POST':
    
        publisherform = PublisherForm(request.POST)
        
        # file is saved
        if publisherform.is_valid():
            publisherform.save()

    publisherform = PublisherForm()
    publishers = Publisher.objects.all()
    message = "none"
    context = {
        'message': message,
        'publisherform': publisherform,
        'publishers': publishers,
        }

    return render(request, 'publisher.html', context=context)
    
def swap(request, book_id, book_instance_id):
    
    # on select swap send email with details to book owner, the owner will see a confirm or 
    # reject button or link with such in email and on this action an email will be sent back to the requester
    
    borrower_email = request.user.username
    system_email = "admin@okka.au"
    print("user", borrower_email)
    print("swap", book_instance_id)
    # set book available to pending
    
    # send request to book owner
    book_instance = BookInstance.objects.filter(id=book_instance_id).values('book__title','owner__member__username')
    # send message to requestor
    print("owner book instance", book_instance)
    book_owner_email = book_instance[0]['owner__member__username']
    book_to_borrow = book_instance[0]['book__title']
    
    #
    connection = mail.get_connection()

# Manually open the connection
    connection.open()

    email_text = "A request for book title: " + book_to_borrow + " from " + borrower_email
   
# Construct an email message that uses the connection
    owner_email = mail.EmailMessage(
        "Book Request",
        email_text,
        book_owner_email,
        [system_email],
        connection=connection,
    )

    owner_email.send()  # Send the email
    connection.close()
    
    context = {
        'book_instance_id': book_instance_id,
        'book_instance': book_instance,
        }
    # Redirect to a success page.
    return render(request, 'swap.html', context=context)


# after registration a membership form will be offered on profile page
def register(request):
    
    message = "New User Created"
    
    context = {
        'message': message,
    }
    
    if request.method == 'POST': # If the form has been submitted...

        email = request.POST['email']
        password = request.POST['password']
            
        if not User.objects.filter(username=email):
    
            # Create user and save to the database
        
            user = User.objects.create_user(email, email, password)
            # Update fields and then save again
        
            user.save()

            user = authenticate(request, username=email, password=password)
            login(request, user)
            
        else:
            print("user exists", email)
            message = "User Exists. Please login or change username"
        
        
    return render(request, 'index.html', context=context)
    
    
def login_view(request):

    username = request.POST['username']
    password = request.POST['password']
    print(password)
    
    user = authenticate(request, username=username, password=password)
    
    print("user in login view",user)
    
    context = {
    'registration_form': RegistrationForm()
    }
    
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'index.html')
    else:
        # Return an 'invalid login' error message.
        print("login error")
        return render(request, 'register.html', context=context)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'index.html')
  
    
def members(request):
    
    members = Member.objects.all().values('id','image','member__first_name','member__last_name','address__suburb','member__username')
    #print(members)
    
    context = {
        'members': members,
        }
    
    return render(request, 'members.html', context=context)
    
def member_titles(request, member_id):
    
    member_data =  Member.objects.filter(id=member_id).values('member__first_name','member__last_name')
    member = Member.objects.get(pk=member_id)
    print('member', member_data)
    member_titles = BookInstance.objects.filter(owner=member).values('id','book__title','book__image',
           'condition','status','exchange_preference')
    print(member_titles)
    
    context = {
        'member_data': member_data[0],
        'member_titles': member_titles,
        }
    
    return render(request, 'member_titles.html', context=context)
    