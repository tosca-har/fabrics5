from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from decouple import config
from .models import Fabric, Site, Slide, Report, Wikisite, Volcano, SuperFabric, CeramicPeriod, ExternalLink
from .forms import SearchForm

mbsu = config('MBSU')
thsu = config('THSU')
abundances = ["None", "Minor","Few", "Common", "Frequent", "Major", "Very Dominant"]


def home(request):
    return render(request, "fabrics/home2.html")

def glossary(request):
    return render(request, "fabrics/glossary.html")

def lod(request):
    return render(request, "fabrics/lod.html")

def slide(request, slug):
    identified_slide = get_object_or_404(Slide, slug=slug)
    return render(request, "fabrics/slide.html", {
        "slide": identified_slide,
        "fabric": identified_slide.fabric,
        "slide_references": identified_slide.refs.all(),
        "site": identified_slide.site,
    })

def report(request, slug):
    identified_report = get_object_or_404(Report, slug=slug)
    id_fabrics = identified_report.fabrics.all()
    return render(request, "fabrics/report.html", {
        "report": identified_report,
        "report_slides": identified_report.slides.all(),
        "report_fabrics": id_fabrics,
        "report_sites": Site.objects.all().filter(fabrics__in=id_fabrics).distinct()
    })

def fabric(request, slug):
    identified_fabric = get_object_or_404(Fabric, slug=slug)
    id_fabrics = identified_fabric.slides.all()
    return render(request, "fabrics/fabric.html", {
        "fabric": identified_fabric,
        "fabric_slides": id_fabrics,
        "fabric_references": identified_fabric.refs.all(),
        "fabric_sites": identified_fabric.sites.all(),
        "superfabrics": identified_fabric.superfabrics.all(),
        "ceramic_periods": identified_fabric.ceramic_periods.all(),
        "mbsu": mbsu,
        "volcanoes": Volcano.objects.all(),
        "thsu":thsu
    })

def superfabric(request, slug):
    identified_superfabric = get_object_or_404(SuperFabric, slug=slug)
    fabrics = identified_superfabric.fabrics.all()
    sites = Site.objects.all().filter(fabrics__in = fabrics).distinct()
    slides = Slide.objects.all().filter(fabric__in = fabrics).distinct()
    periods = CeramicPeriod.objects.all().filter(fabrics__in = fabrics).distinct()
    query = identified_superfabric.name
    wiki = " "
    if identified_superfabric.wiki_id:
        wiki = identified_superfabric.wiki_id
    query2 = identified_superfabric.desc
    return render(request, "fabrics/results.html", {
         "fabrics": fabrics,
         "slides": slides,
        "query": query,
        "query2": query2,
        "wiki": wiki,
        "sites": sites,
        "mbsu": mbsu,
        "volcanoes": Volcano.objects.all(),
        "ceramic_periods": periods,
        "thsu":thsu
    })


def site(request, slug):
    identified_site = get_object_or_404(Site, slug=slug)
    site_slides = identified_site.slides.all()
    externallinks = identified_site.external_link.all()
    return render(request, "fabrics/site.html", {
        "site": identified_site,
        "site_slides": site_slides,
        "site_fabrics": identified_site.fabrics.all(),
        "site_references": Report.objects.all().filter(slides__in=site_slides).distinct(),
        "site_wikis": identified_site.wikisite.all(),
        "externallinks":externallinks,
        "volcanoes": Volcano.objects.all(),
        "has_volcanoes" : identified_site.volcano.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })


def wikisite(request, slug):
    identified_wikisite = get_object_or_404(Wikisite, slug=slug)
    sites = identified_wikisite.sites.all()
    fabrics = Fabric.objects.all().filter(sites__in=sites).distinct() 
    slides = Slide.objects.all().filter(site__in=sites).distinct()
    externallinks = identified_wikisite.external_link.all()
    return render(request, "fabrics/wikisite.html", {
        "wikisite": identified_wikisite,
        "sites": sites,
        "fabrics": fabrics,
        "slides": slides,       
        "references": Report.objects.all().filter(slides__in=slides).distinct(),
        "has_volcanoes" : identified_wikisite.volcano.all(),
        "volcanoes": Volcano.objects.all(), 
        "externallinks":externallinks,
        "mbsu": mbsu,
        "thsu":thsu
    })


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST) 
        fabrics = Fabric.objects.all() 
        query = "Matching fabrics for"    
        if form.is_valid():
            val = form.cleaned_data.get("calcareous")
            if val > -1:
                fabrics = fabrics.filter(calcareous_min__lte=val, calcareous_max__gte=val)
                query = query + ";  Calcareous-" + abundances[val]
            val = form.cleaned_data.get("quartz")
            if val > -1:
                fabrics = fabrics.filter(quartz_min__lte=val, quartz_max__gte=val)
                query = query + ";  Quartz-" + abundances[val]
            val = form.cleaned_data.get("feldspars")
            if val > -1:
                fabrics = fabrics.filter(feldspar_min__lte=val, feldspar_max__gte=val)
                query = query + ";  Feldspar-" + abundances[val]
            val = form.cleaned_data.get("pyroxene")
            if val > -1:
                fabrics = fabrics.filter(pyroxene_min__lte=val, pyroxene_max__gte=val)
                query = query + ";  Pyroxene-" + abundances[val]
            val = form.cleaned_data.get("amphibole")
            if val > -1:
                fabrics = fabrics.filter(amphibole_min__lte=val, amphibole_max__gte=val)
                query = query + ";  Amphibole-" + abundances[val]
            val = form.cleaned_data.get("opaque_iron_oxides")
            if val > -1:
                fabrics = fabrics.filter(opaque_min__lte=val, opaque_max__gte=val)
                query = query + ";  Opaques-" + abundances[val]
            val = form.cleaned_data.get("biotite")
            if val > -1:
                fabrics = fabrics.filter(biotite_min__lte=val, biotite_max__gte=val)
                query = query + ";  Biotite-" + abundances[val]                              
            val = form.cleaned_data.get("muscovite")
            if val > -1:
                fabrics = fabrics.filter(muscovite_min__lte=val, muscovite_max__gte=val)
                query = query + ";  Muscovite-" + abundances[val]
            val = form.cleaned_data.get("olivine")
            if val > -1:
                fabrics = fabrics.filter(olivine_min__lte=val, olivine_max__gte=val)
                query = query + ";  Olivine-" + abundances[val]                              
            val = form.cleaned_data.get("epidote")
            if val > -1:
                fabrics = fabrics.filter(epidote_min__lte=val, epidote_max__gte=val)
                query = query + ";  Epidote-" + abundances[val]  
            val = form.cleaned_data.get("garnet")
            if val > -1:
                fabrics = fabrics.filter(garnet_min__lte=val, garnet_max__gte=val)
                query = query + ";  Garnet-" + abundances[val]
            val = form.cleaned_data.get("igneous_rock_fragments")
            if val > -1:
                fabrics = fabrics.filter(igneous_rock_fragments_min__lte=val, igneous_rock_fragments_max__gte=val)
                query = query + ";  Igneous Rocks-" + abundances[val]                              
            val = form.cleaned_data.get("sedimentary_metasedimentary_rocks")
            if val > -1:
                fabrics = fabrics.filter(sedimentary_metasedimentary_min__lte=val, sedimentary_metasedimentary_max__gte=val)
                query = query + ";  Meta/Sedimentary Rocks-" + abundances[val] 
            val = form.cleaned_data.get("grog")
            if val > -1:
                fabrics = fabrics.filter(grog_min__lte=val, grog_max__gte=val)
                query = query + ";  Grog-" + abundances[val] 
            val = form.cleaned_data.get("vitric")
            if val != '':
                fabrics = fabrics.filter(vitric=val)
                query = query + ";  Vitric-" + val 
            val = form.cleaned_data.get("felsitic")
            if val != '':
                fabrics = fabrics.filter(felsitic=val)
                query = query + ";  Felsitic-" + val
            val = form.cleaned_data.get("microlitic")
            if val != '':
                fabrics = fabrics.filter(microlitic=val)
                query = query + ";  Microlitic-" + val 
            val = form.cleaned_data.get("microphaneritic")
            if val != '':
                fabrics = fabrics.filter(microphaneritic=val)
                query = query + ";  Microphaneritic-" + val 
            val = form.cleaned_data.get("lathwork")
            if val != '':
                fabrics = fabrics.filter(lathwork=val)
                query = query + ";  Lathwork-" + val
            val = form.cleaned_data.get("metavolcanic")
            if val != '':
                fabrics = fabrics.filter(metavolcanic=val)
                query = query + ";  Metavolcanic-" + val 
            val = form.cleaned_data.get("plutonite")
            if val != '':
                fabrics = fabrics.filter(plutonite=val)
                query = query + ";  Plutonite-" + val 
            val = form.cleaned_data.get("tectonite")
            if val != '':
                fabrics = fabrics.filter(tectonite=val)
                query = query + ";  Tectonite-" + val
            val = form.cleaned_data.get("argillitic")
            if val != '':
                fabrics = fabrics.filter(argillitic=val)
                query = query + ";  Argillitic-" + val     
            val = form.cleaned_data.get("chert")
            if val != '':
                fabrics = fabrics.filter(chert=val)
                query = query + ";  Chert-" + val 
            val = form.cleaned_data.get("quartzite")
            if val != '':
                fabrics = fabrics.filter(quartzite=val)
                query = query + ";  Quartzite-" + val
            val = form.cleaned_data.get("siltstone")
            if val != '':
                fabrics = fabrics.filter(siltstone=val)
                query = query + ";  Siltstone-" + val 
            val = form.cleaned_data.get("limeclast")
            if val != '':
                fabrics = fabrics.filter(limeclast=val)
                query = query + ";  Limeclast-" + val 

            val = form.cleaned_data.get("regions_to_include") 
            fabrics = fabrics.filter(region__in=val)
            query = query + "." 
            query2 = "Regions searched: " + ', '.join(val) + '.'
            wiki = " "
            sites = Site.objects.all().filter(fabrics__in = fabrics).distinct()
            slides = Slide.objects.all().filter(fabric__in = fabrics).distinct()
            periods = CeramicPeriod.objects.all().filter(fabrics__in = fabrics).distinct()
            if len(fabrics) > 0:
                return render(request, "fabrics/results.html", {
                    "fabrics": fabrics,
                    "slides": slides,
                    "query": query,
                    "query2": query2,
                    "wiki": wiki,
                    "sites": sites,
                    "mbsu": mbsu,
                    "ceramic_periods": periods,
                    "volcanoes": Volcano.objects.all(),
                    "thsu":thsu
                })
            else: return HttpResponseRedirect("no-match")
                
    else:   
        form = SearchForm()
    return render(request, "fabrics/search.html", {
        "form": form
    })

def no_match(request):
    return render(request, "fabrics/no-match.html")

def period_index(request):   
    return render(request, "fabrics/period-index.html", {
        "periods": CeramicPeriod.objects.all()
    })


def site_index(request):   
    return render(request, "fabrics/site-index.html", {
        "sites": Site.objects.all(),
        "volcanoes": Volcano.objects.all(),
        "mbsu": mbsu,
        "thsu": thsu 
    })



def period(request, slug):
    identified_period2 = CeramicPeriod.objects.filter(slug=slug)
    identified_period = get_object_or_404(CeramicPeriod, slug=slug)
    children2 = identified_period.get_all_descendants()
    pk_set = {obj.pk for obj in children2}
    children = identified_period.children.all()
    children3 = CeramicPeriod.objects.filter(pk__in=pk_set)
    periods = children3 | identified_period2
    slides = Slide.objects.all().filter(ceramic_period__in=periods).distinct()
    fabrics = Fabric.objects.all().filter(ceramic_periods__in=periods).distinct()
    wikisites = Wikisite.objects.all().filter(ceramic_periods__in=periods).distinct()
    externallinks = ExternalLink.objects.all().filter(ceramic_periods__in=periods).distinct()

    return render(request, "fabrics/period.html", {
        "period": identified_period,
        "slides": slides,
        "fabrics": fabrics,
        "wikisites":wikisites,
        "externallinks":externallinks,
        "children" : children
    })


def index(request, order, limited = 0):
    if order == 1:
        fabricsd = Fabric.objects.all().order_by("-calcareous_max", "-calcareous_min")
    elif order == 2:
        fabricsd = Fabric.objects.all().order_by("-quartz_max", "-quartz_min")
    elif order == 3:
        fabricsd = Fabric.objects.all().order_by("-feldspar_max", "-feldspar_min")
    elif order == 4:
        fabricsd = Fabric.objects.all().order_by("-pyroxene_max", "-pyroxene_min")
    elif order == 5:
        fabricsd = Fabric.objects.all().order_by("-amphibole_max", "-amphibole_min")
    elif order == 6:
        fabricsd = Fabric.objects.all().order_by("-opaque_max", "-opaque_min")
    elif order == 7:
        fabricsd = Fabric.objects.all().order_by("-olivine_max", "-olivine_min")
    elif order == 8:
        fabricsd = Fabric.objects.all().order_by("-biotite_max", "-biotite_min")
    elif order == 9:
        fabricsd = Fabric.objects.all().order_by("-muscovite_max", "-muscovite_min")
    elif order == 10:
        fabricsd = Fabric.objects.all().order_by("-epidote_max", "-epidote_min")
    elif order == 11:
        fabricsd = Fabric.objects.all().order_by("-garnet_max", "-garnet_min")
    elif order == 12:
        fabricsd = Fabric.objects.all().order_by("-igneous_rock_fragments_max", "-igneous_rock_fragments_min")
    elif order == 13:
        fabricsd = Fabric.objects.all().order_by("-sedimentary_metasedimentary_max", "-sedimentary_metasedimentary_min")
    elif order == 14:
        fabricsd = Fabric.objects.all().order_by("-grog_max", "-grog_min")
    elif order == 15:
        fabricsd = Fabric.objects.all().order_by("lithics")
    elif order == 16:
        fabricsd = Fabric.objects.all().order_by("region", "desc")              
    else:
        fabricsd = Fabric.objects.all().order_by("desc")
    return render(request, "fabrics/index.html", {
        "fabrics": fabricsd
    })

