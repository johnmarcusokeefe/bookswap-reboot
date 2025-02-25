from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('members', views.members, name='members'),
    path('member_titles/<int:member_id>', views.member_titles, name='member_titles'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('author', views.author, name='author'),
    path('publisher', views.publisher, name='publisher'),
    path('register', views.register, name='register'),
    path('book/<int:book_id>', views.book, name='book'),
    path('book_instance/<int:book_id>', views.book_instance, name='book_instance'),
    path('edit_book', views.edit_book, name='edit_book'),
    path('edit_book/<int:id>', views.edit_book, name='edit_book'),
    path('edit_book_instance', views.edit_book_instance, name='edit_book_instance'),
    path('edit_book_instance/<int:id>', views.edit_book_instance, name='edit_book_instance'),
    path('swap/<int:book_id>/<int:book_instance_id>', views.swap),
] 