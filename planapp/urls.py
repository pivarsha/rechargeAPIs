from django.urls import re_path,path
from .views import *

urlpatterns = [
    # re_path(r'^list_plan/$',list_plan, name='list_plan'),
    # re_path(r'^initiate_recharge/$',initiate_recharge, name='initiate_recharge'),
    # function Based
    # path('list_plan/', list_plan, name="list_plan"),
    # path('initiate_recharge/', initiate_recharge, name="initiate_recharge"),
    # for class based
    re_path(r'^list-plans/$', ListPlans.as_view(), name='list_plans'),
    path('initiate-recharge/<int:pk>/', InitiatePlan.as_view(), name='initiate_recharge'),



    

]




