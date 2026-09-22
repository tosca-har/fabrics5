from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("index<int:order>", views.index, name="index"),
    # path("sites", views.site_index, name="site-index"),
    # path("periods", views.period_index, name="period-index"),
    # path("search", views.search, name="search"),
    # path("<int:tpr>", views.fabric_by_number),
    path("glossary", views.glossary, name="glossary"),
    # path("vocab", views.lod, name="vocab"),
    # path("period_<slug:slug>", views.period, name="period"),
    # path("no-match", views.no_match, name="no-match"),
    # path("site_<slug:slug>", views.site, name="site-type"),
    # path("superfabric_<slug:slug>", views.superfabric, name="superfabric-type"),
    # path("wikisite_<slug:slug>", views.wikisite, name="wikisite-type"),
    # path("report_<slug:slug>", views.report, name="report-type"),
    # path("slide_<slug:slug>", views.slide, name="slide-type"),
    # path("<slug:slug>", views.fabric, name="fabric-type"),
    
]
