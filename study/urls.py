from django.urls import path
from study.views.math_view import persegi, segitiga, geometri, Ppanjang, Lingkaran, Bketupat, kubus, math, stat, akarpangkat, akar, study
from study.views.session_view import StudySessionListCreateView, StudySessionDetailView
from study.views.capsule_view import capsule, ListCreateView, DetailView

urlpatterns = [
    # study
    path('', study, name='study'),

    #capsule 
    path('capsule/', capsule, name='capsule'),
    path('capsule/lcv',ListCreateView.as_view(), name='capsule-list-create'), 
    path('capsule/<int:pk>/', DetailView.as_view(), name='capsule-detail'),  # detail capsule

    #tree


    # math
    path('math/', math, name='math'),
    path('geometri/', geometri, name='geometri'),
    path('persegi/', persegi, name='persegi'),
    path('segitiga/', segitiga, name='segitiga'),
    path('Ppanjang/', Ppanjang, name='Ppanjang'),
    path('Lingkaran/', Lingkaran, name='Lingkaran'),
    path('Bketupat/', Bketupat, name='Bketupat'),
    path('kubus/', kubus, name='kubus'),
    path('stat/', stat, name='stat'),
    path('akarpangkat/', akarpangkat, name='akarpangkat'),
    path('akar/', akar, name='akar'),

    # api sessions
    path('sessions/', StudySessionListCreateView.as_view(), name='study-session-list-create'),
    path('sessions/<int:pk>/', StudySessionDetailView.as_view(), name='study-session-detail'),
]
