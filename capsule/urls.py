from django.urls import path
from capsule.views.session_view import StudySessionListCreateView, StudySessionDetailView
from capsule.views.capsule_view import capsule, ListCreateView, DetailView, CapsuleAnswerAPIView

urlpatterns = [
    # capsule
    path('', capsule, name='capsule'),

    #capsule 
    path('capsule/', capsule, name='capsule'),
    path('capsule/lcv',ListCreateView.as_view(), name='capsule-list-create'), 
    path('capsule/<int:pk>/', DetailView.as_view(), name='capsule-detail'),  # detail capsule
    path('capsule/<int:pk>/answer/', CapsuleAnswerAPIView.as_view()),
  
    #tree


    

    # api sessions
    path('sessions/', StudySessionListCreateView.as_view(), name='capsule-session-list-create'),
    path('sessions/<int:pk>/', StudySessionDetailView.as_view(), name='capsule-session-detail'),
]
