from django.urls import path
from .views import UserRegisterView, LoginView, LogoutView, SupplierDashboardView

from django.urls import path

from .views import (
    UserRegisterView,
    LoginView,
    LogoutView,
    SupplierDashboardView,
    BuyerDashboardView,
)

urlpatterns = [

    # =====================================
    # REGISTRATION
    # =====================================

    path(
        "suppliers/register/",
        UserRegisterView.as_view(),
        {"role": "supplier"},
        name="supplier-register"
    ),

    path(
        "buyers/register/",
        UserRegisterView.as_view(),
        {"role": "buyer"},
        name="buyer-register"
    ),

    # =====================================
    # AUTHENTICATION
    # =====================================

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),

    # =====================================
    # DASHBOARDS
    # =====================================

    path(
        "suppliers/dashboard/",
        SupplierDashboardView.as_view(),
        name="supplier-dashboard"
    ),

    path(
        "buyers/dashboard/",
        BuyerDashboardView.as_view(),
        name="buyer-dashboard"
    ),
]