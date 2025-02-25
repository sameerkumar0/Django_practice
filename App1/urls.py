from django.urls import path
from App1 import views
urlpatterns = [

    path('books_create/', views.book_create, name='book-create'),
    path('books_list/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('book_update/<int:pk>/', views.book_update, name='book-update'),
    path('books_delete/<int:pk>/', views.book_delete, name='book-delete'),
    # User Authentication URLs
    path('register_user/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name='logout')
]
