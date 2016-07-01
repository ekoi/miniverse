from django.db import models
from apps.dvobjects.models import DvObject
from apps.terms_of_use.models import TermsOfUseAndAccess

class Dataverse(models.Model):

    id = models.OneToOneField(DvObject, db_column='id', primary_key=True)

    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    affiliation = models.CharField(max_length=255, blank=True, null=True)
    dataversetype = models.CharField(max_length=255)

    #displaybytype = models.NullBooleanField()

    facetroot = models.BooleanField()
    guestbookroot = models.BooleanField()

    metadatablockroot = models.BooleanField()

    permissionroot = models.BooleanField(default=True)
    templateroot = models.BooleanField()
    themeroot = models.BooleanField()

    defaultcontributorrole = models.ForeignKey('Dataverserole')
    defaulttemplate = models.ForeignKey('Template', blank=True, null=True, related_name='dv_default_template')
    citation_redirect_url = models.CharField(db_column='citationredirecturl', max_length=255, blank=True, null=True)

    """
        defaultcontributorrole = models.ForeignKey('Dataverserole')
        defaulttemplate = models.ForeignKey('Template', blank=True, null=True)
        citationredirecturl = models.CharField(max_length=255, blank=True, null=True)
    """

    def __str__(self):
        return self.name
    #defaultcontributorrole = models.ForeignKey('Dataverserole')
    #defaulttemplate = models.ForeignKey('Template', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataverse'

class Dataverserole(models.Model):
    alias = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    permissionbits = models.BigIntegerField(blank=True, null=True)
    owner = models.ForeignKey(DvObject, blank=True, null=True)

    def __str__(self):
        return self.alias

    class Meta:
        managed = False
        db_table = 'dataverserole'

class DataverseTheme(models.Model):
    """
    No id, created, modified
    """
    backgroundcolor = models.CharField(max_length=255, blank=True, null=True)
    linkcolor = models.CharField(max_length=255, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    logoalignment = models.CharField(max_length=255, blank=True, null=True)
    logobackgroundcolor = models.CharField(max_length=255, blank=True, null=True)
    logoformat = models.CharField(max_length=255, blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    textcolor = models.CharField(max_length=255, blank=True, null=True)
    dataverse = models.ForeignKey(Dataverse, blank=True, null=True)

    def __str__(self):
        return '%s' % self.dataverse.name

    class Meta:
        managed = False
        db_table = 'dataversetheme'


class Template(models.Model):
    name = models.CharField(max_length=255)
    dataverse = models.ForeignKey(DvObject, blank=True, null=True)

    usagecount = models.BigIntegerField(blank=True, null=True)

    createtime = models.DateTimeField()

    def __str__(self):
        return '%s (%s)' % (self.dataverse, self.dataverse)

    class Meta:
        managed = False
        db_table = 'template'

class CitationPageCheck(models.Model):
    dataverse = models.ForeignKey(Dataverse)
    citation_url = models.URLField()
    widget_link = models.TextField(blank=True)
    citation_found = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.dataverse

    class Meta:
        ordering = ('-created', 'dataverse')