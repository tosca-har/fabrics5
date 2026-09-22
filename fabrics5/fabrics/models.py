from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class ExternalLink(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 50, blank=True)
    org = models.CharField(max_length= 200, blank=True)
    first = models.CharField(max_length= 200, blank=True)
    last = models.CharField(max_length= 200, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.org} ({self.name})" 


class Report(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20, blank=True)
    fullname = models.CharField(max_length= 100, blank=True)
    author_list = models.CharField(max_length= 500, null=True)
    details = models.TextField(max_length= 1000, null=True, blank=True)
    link = models.CharField(max_length= 100, blank=True, null=True)
    summary = models.TextField(max_length= 1000, null=True, blank=True)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.fullname})" 



class SuperFabric(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 50)
    desc = models.CharField(null=True, max_length= 200, blank=True)
    comments = models.TextField(null=True, blank=True)
    wiki_id = models.CharField(null=True, max_length= 100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.desc})"

class Fabric(models.Model):
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    name = models.CharField(default="tpr", max_length=20)
    desc = models.CharField(null=True, max_length=100)
    region = models.CharField(null=True, max_length=100)
    superfabrics = models.ManyToManyField(SuperFabric, related_name="fabrics", blank=True)
    calcareous_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    calcareous_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet_min = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet_max = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    lithics = models.CharField(null=True, max_length=100)
    vitric = models.BooleanField(default=False)
    felsitic = models.BooleanField(default=False)
    microlitic = models.BooleanField(default=False)
    microphaneritic = models.BooleanField(default=False)
    lathwork = models.BooleanField(default=False)
    metavolcanic = models.BooleanField(default=False)
    plutonite = models.BooleanField(default=False)
    amphibolite = models.BooleanField(default=False)
    tectonite = models.BooleanField(default=False)
    argillitic = models.BooleanField(default=False)
    chert = models.BooleanField(default=False)
    quartzite = models.BooleanField(default=False)
    siltstone = models.BooleanField(default=False)
    limeclast = models.BooleanField(default=False)
    comments = models.CharField(null=True, max_length=500)
    refs = models.ManyToManyField(Report, related_name="fabrics", blank=True)
    has_full = models.BooleanField(default=False) 
    has_image = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug} ({self.desc})"

    
class CeramicPeriod(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 50)
    desc = models.CharField(null=True, max_length= 100, blank=True)
    comments = models.TextField(null=True, blank=True)
    time_start = models.IntegerField(null=True, blank =True)
    time_start_ref = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, related_name="vg_time_start", blank=True)
    time_end = models.IntegerField(null=True, blank =True)
    time_end_ref = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, related_name="vg_time_end", blank=True)
    wikidata = models.CharField(null=True, max_length= 100, blank=True)
    periodo = models.CharField(null=True, max_length= 100, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    fabrics = models.ManyToManyField(Fabric, related_name="ceramic_periods", blank=True)
    image_name = models.CharField(null=True, max_length=200, blank=True)
    image_link = models.CharField(null=True, max_length=200, blank=True)
    image_attribution = models.CharField(null=True, max_length=500, blank=True)
    external_link = models.ManyToManyField(ExternalLink, related_name="ceramic_periods", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_all_descendants(self):
        descendants = set()
        children = self.children.all()
        for child in children:
            descendants.add(child)
            descendants.update(child.get_all_descendants())
        return descendants

    def __str__(self):
        return f"{self.name} ({self.time_start} - {self.time_end} BP)"

class Volcano(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20)
    number = models.CharField(max_length= 20)
    region = models.CharField(null=True, max_length=100)
    wiki_id = models.CharField(null=True, max_length= 100, blank=True)
    type = models.CharField(null=True, max_length= 100, blank=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    volcanic_region = models.CharField(null=True, blank=True, max_length=200)
    volcano_landform = models.CharField(null=True, blank=True, max_length=200)
    rock_type = models.CharField(null=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.region})"
    
class Site(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20)
    island = models.CharField(max_length= 20, null=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    geonames_id = models.IntegerField(null=True, blank=True)
    open_location_code = models.CharField(null=True, blank=True, max_length=100)
    wikidata_id = models.CharField(null=True, blank=True, max_length=100)
    gettyname = models.CharField(null=True, max_length= 100, blank=True)
    fabrics = models.ManyToManyField(Fabric, related_name="sites", blank=True)
    has_full = models.BooleanField(default=False) 
    has_image = models.BooleanField(default=False)
    island_type = models.CharField(null=True, blank=True, max_length=100)
    macrostrat = models.CharField(null=True, blank=True, max_length=200)
    mindatname = models.CharField(null=True, max_length= 100, blank=True)
    dickinson_lithology = models.CharField(null=True, blank=True, max_length=200)
    comments = models.TextField(null=True, blank=True)
    volcano = models.ManyToManyField(Volcano, related_name="site", blank=True)
    external_link = models.ManyToManyField(ExternalLink, related_name="sites", blank=True)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.island})"

    def thename(self):
        return f"{self.name}" 
    
    @property
    def fabric_string(self):
        fabs = self.fabrics.all()
        fabstring = ''
        for fab in fabs:
            fabstring = fabstring + " (" + fab.name + " " + fab.desc + ")"
        return fabstring
    
class Slide(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20, db_index=True, unique=True)
    fabric = models.ForeignKey(Fabric, on_delete=models.SET_NULL, null=True, related_name="slides")
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True, blank=True, related_name="slides")
    sherd = models.CharField(null=True, blank=True, max_length=50)
    sherd_origin_site = models.CharField(null=True, max_length=50)
    calcareous = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    feldspar = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    quartz = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    pyroxene = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    amphibole = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    opaque = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    olivine = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    biotite = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    muscovite = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    epidote = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    igneous_rock_fragments = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    sedimentary_metasedimentary = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    grog = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)])
    garnet = models.IntegerField(default="0", validators=[MinValueValidator(0), MaxValueValidator(6)]) 
    lithics = models.CharField(null=True, max_length=100, blank=True)
    vitric = models.BooleanField(default=False)
    felsitic = models.BooleanField(default=False)
    microlitic = models.BooleanField(default=False)
    microphaneritic = models.BooleanField(default=False)
    lathwork = models.BooleanField(default=False)
    metavolcanic = models.BooleanField(default=False)
    plutonite = models.BooleanField(default=False)
    tectonite = models.BooleanField(default=False)
    argillitic = models.BooleanField(default=False)
    chert = models.BooleanField(default=False)
    quartzite = models.BooleanField(default=False)
    siltstone = models.BooleanField(default=False)
    limeclast = models.BooleanField(default=False)
    desc = models.CharField(null=True, max_length=500, blank=True)
    image_name = models.CharField(null=True, max_length=100, blank=True)
    image_omero_id = models.IntegerField(null=True, blank=True)
    full_image_name = models.CharField(null=True, max_length=100, blank=True)
    full_image_omero_id = models.IntegerField(null=True, blank=True)
    full_image_oe_omero_id = models.IntegerField(null=True, blank=True)
    source = models.CharField(default="Dickinson Collection, Bishop Museum", null=True, blank=True, max_length=100)
    refs = models.ManyToManyField(Report, related_name="slides", blank=True)
    ceramic_period = models.ForeignKey(CeramicPeriod, on_delete=models.SET_NULL, null=True, blank=True, related_name="slides")
    sherd_image = models.CharField(null=True, max_length=100, blank=True)
    sherd_geochem = models.CharField(null=True, max_length=100, blank=True)
    sherd_microct = models.CharField(null=True, max_length=100, blank=True)
    sherd_desc = models.CharField(null=True, max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} ({self.sherd})" 


class Wikisite(models.Model):
    slug = models.SlugField(default="", blank= True, null = False, db_index=True)
    name = models.CharField(max_length= 20)
    desc = models.CharField(null=True, max_length= 100, blank=True)
    geoname = models.CharField(null=True, max_length= 100, blank=True)
    gettyname = models.CharField(null=True, max_length= 100, blank=True)
    mindatname = models.CharField(null=True, max_length= 100, blank=True)
    sites = models.ManyToManyField(Site, related_name="wikisite", blank=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6) 
    lng = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    macrostrat = models.CharField(null=True, blank=True, max_length=200)
    comments = models.TextField(null=True, blank=True)
    volcano = models.ManyToManyField(Volcano, related_name="wikisite", blank=True)
    ceramic_periods = models.ManyToManyField(CeramicPeriod, related_name="wikisites", blank=True)
    dickinson_lithology = models.CharField(null=True, blank=True, max_length=300)
    external_link = models.ManyToManyField(ExternalLink, related_name="wikisites", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.desc})"# Create your models here.
