from django.contrib import admin
from django.urls import path
from datasources import views
from datasources import api


urlpatterns = [
    path('getstateLevelData/', api.GetStateLevelCases.as_view()),
    path('getCountryLevelData/', api.GetCountryLevelCases.as_view()),
    path('getDistrictLevelData/', api.GetDistrictLevelRefreshCases.as_view()),
    path('getConsolidatedData/', api.GetConsolidatedData.as_view()),
    path('getComparisionData/', api.GetComparisionData.as_view()),
    path('getStateWiseComparisionData/', api.GetStateWiseComparisionData.as_view()),
    path('getAgeWiseData/', api.GetAgeWiseData.as_view()),
]
