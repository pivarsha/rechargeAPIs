from django.urls import re_path,path
from .views import *


urlpatterns = [
    # re_path(r'^list_plan/$',list_plan, name='list_plan'),
    # re_path(r'^initiate_recharge/$',initiate_recharge, name='initiate_recharge'),

    # function Based

    # path('list_plan/', list_plan, name="list_plan"),
    # path('initiate_recharge/', initiate_recharge, name="initiate_recharge"),

    path('list-plans',ListPlans.as_view(),name='list-plans'),
    path('list-plans/<int:pk>',DetailListPlans.as_view(),name='detailplans'),
    path('initiate-recharge/',ListInitiatePlan.as_view(),name='initiate-recharge'),
    path('initiate-recharge/<int:pk>/',DetailInitiatePlan.as_view(),name='detailrecharge'),
]




