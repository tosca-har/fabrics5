from django.contrib import admin
from .models import Fabric, Slide, Site, Report, Wikisite, CeramicPeriod, SuperFabric, Volcano, ExternalLink

class FabricAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("region",)
    ordering = ('name',)

admin.site.register(Fabric, FabricAdmin)

class SlideAdmin(admin.ModelAdmin):
    list_filter = ("fabric",)
    list_display = ("name", "fabric", "site", "image_name", "full_image_name",)
    ordering = ('name',)

admin.site.register(Slide, SlideAdmin)

class ExternalLinkAdmin(admin.ModelAdmin):
    list_filter = ("org",)
    list_display = ("name", "org",)
    ordering = ('org','name',)

admin.site.register(ExternalLink, ExternalLinkAdmin)

class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Site, SiteAdmin)

class WikisiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('desc',)
    
admin.site.register(Wikisite, WikisiteAdmin)

class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Report, ReportAdmin)

class SuperFabricAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('desc',)
    
admin.site.register(SuperFabric, SuperFabricAdmin)

class CeramicPeriodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(CeramicPeriod, CeramicPeriodAdmin)

class VolcanoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('region', 'name',)
    
admin.site.register(Volcano, VolcanoAdmin)
# Register your models here.
