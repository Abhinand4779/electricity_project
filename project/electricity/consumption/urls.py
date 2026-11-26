from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Dashboard (Overview & Analytics)
    path('', views.dashboard, name='dashboard'),

    # Data Collection & Management
    path('add/', views.add_consumption, name='add_consumption'),
    path('history/', views.history, name='history'),
    path('edit/<int:pk>/', views.edit_consumption, name='edit_consumption'),
    path('delete/<int:pk>/', views.delete_consumption, name='delete_consumption'),
    path('import-data/', views.import_data_view, name='import_data'),

    # ML Consumption Prediction & Forecasting
    path('predictions/', views.predictions_view, name='predictions'),

    # Anomaly Detection
    path('anomaly-detection/', views.anomaly_detection_view, name='anomaly_detection'),
    path('anomaly-detection/<int:pk>/toggle/', views.toggle_anomaly_resolved, name='toggle_anomaly_resolved'),

    # Energy Waste Analysis
    path('waste-analysis/', views.waste_analysis_view, name='waste_analysis'),

    # Energy-Saving Recommendations & Self-Learning Feedback (Feature 04)
    path('recommendations/', views.recommendations_view, name='recommendations'),
    path('recommendations/<int:pk>/toggle/', views.toggle_recommendation_completed, name='toggle_recommendation_completed'),
    path('recommendations/<int:pk>/feedback/', views.recommendation_feedback_view, name='recommendation_feedback'),

    # Advanced AI Features (Features 01, 02, 03, 05, 06, 07)
    path('digital-twin/', views.digital_twin_view, name='digital_twin'),
    path('waste-detective/', views.waste_detective_view, name='waste_detective'),
    path('energy-fingerprint/', views.energy_fingerprint_view, name='energy_fingerprint'),

    # Smart Meter Dataset Explorer
    path('dataset/', views.dataset_view, name='dataset'),

    # Grid Administrator & Multi-User Analytics Dashboard
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),

    # Viva Demonstration Instant Persona Switcher
    path('switch-role/<str:role>/', views.switch_role_view, name='switch_role'),

    # Authentication Portals (Dedicated Consumer & Admin Logins)
    path('login/', views.consumer_login_view, name='login'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
