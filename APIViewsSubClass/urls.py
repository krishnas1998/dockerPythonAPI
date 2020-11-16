
from django.contrib import admin
from django.urls import path
from testapp import (
    dockerview
)

urlpatterns = [
    path('ubuntu/<int:cpu_cores>/<str:memory>/<str:login_method>/', dockerview.GetProvisionID.as_view()),
    path('ubuntustatus/<str:provision_id>/', dockerview.GetProvisionStatus.as_view()),
]
