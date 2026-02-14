from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Home
    path('', views.home, name='home'),

    # Teach & Learn Pages
    path('tech/', views.tech_page, name='tech'),

    # Learn List & Skill Detail (Learner view)
    path('learn/', views.learn_page, name='learn'),
    path('learn/<int:skill_id>/', views.skill_detail, name='skill_detail'),

    # Teacher Views (view & edit)
    path('skill/<int:pk>/view/', views.skill_detail_teacher, name='skill_detail_teacher'),
    path('skill/<int:pk>/edit/', views.edit_skill, name='edit_skill'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
