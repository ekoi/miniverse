"""
Metric views, returning JSON repsonses
"""
from collections import OrderedDict
import json
from os.path import splitext
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect #, Http404
from django.views.decorators.cache import cache_page
from django.views.decorators.clickjacking import xframe_options_exempt

from dv_apps.datafiles.models import Datafile, FileMetadata
from dv_apps.metrics.stats_util_datasets import StatsMakerDatasets
from dv_apps.metrics.stats_util_dataverses import StatsMakerDataverses
from dv_apps.metrics.stats_util_files import StatsMakerFiles
from dv_apps.metrics.stats_util_base import EASY_STATISTICS

from dv_apps.utils.metrics_cache_time import get_metrics_cache_time
from dv_apps.utils.date_helper import get_one_year_ago

from dv_apps.metrics.forms import Metrics
from django.http import HttpResponse, Http404

FIVE_HOURS = 60 * 60 * 5


"""
from django.core.cache import cache
cache.clear()
"""

@cache_page(FIVE_HOURS)
def view_homepage_placeholder(request):

    resp_dict = {}

    return render(request, 'metrics/index-placeholder.html', resp_dict)


@xframe_options_exempt
@cache_page(get_metrics_cache_time())
def view_public_visualizations_last12(request):
    """
    Return visualizations covering the last 11-12 months.

    e.g. If it's July 23, 2016, it will start from June 1, 2015
    e.g. If it's June 2, 2016, it will start from May 1, 2015
    """
    # one year ago
    #
    one_year_ago = get_one_year_ago(datetime.now())

    # start from the 1st day of last year's month
    #
    #filters = dict(start_date=one_year_ago.strftime('%Y-%m-01'))
    filters = dict(affiliation='DANS', start_date=one_year_ago.strftime('%Y-%m-01'))

    return view_public_visualizations(request, **filters)

@cache_page(get_metrics_cache_time())
def downloads(request, **kwargs):
    resp_dict = {}
    """
    Return HTML/D3Plus visualizations for a variety of public statistics
    """
    EASY_STATISTICS = 1
    resp_dict = {}

    if EASY_STATISTICS:
        if request.method == "POST":
            form = Metrics(request.POST)
        else:
            form = Metrics()
        kwargs["category"] = form.data.get("category", "audience")
        kwargs["start_date"] = form.data.get("start_date", "2017-01-01")
        kwargs["end_date"] = form.data.get("end_date", "2017-12-31")

    if kwargs and len(kwargs) > 0:
        # kwargs override GET parameters
        stats_datasets = StatsMakerDatasets(**kwargs)
        stats_dvs = StatsMakerDataverses(**kwargs)
        stats_files = StatsMakerFiles(**kwargs)
    else:
        stats_datasets = StatsMakerDatasets(**request.GET.dict())
        stats_dvs = StatsMakerDataverses(**request.GET.dict())
        stats_files = StatsMakerFiles(**request.GET.dict())
    return render(request, 'metrics/download.html', resp_dict)


@cache_page(get_metrics_cache_time())
def view_easy_visualizations(request, **kwargs):
    resp_dict = {}
    """
    Return HTML/D3Plus visualizations for a variety of public statistics
    """
    EASY_STATISTICS = 1
    resp_dict = {}

    if EASY_STATISTICS:
        if request.method == "POST":
            form = Metrics(request.POST)
        else:
            form = Metrics()
        kwargs["category"] = form.data.get("category", "audience")
        kwargs["start_date"] = form.data.get("start_date", "2008-01-01")
        kwargs["end_date"] = form.data.get("end_date", "2017-07-31")

    if kwargs and len(kwargs) > 0:
        # kwargs override GET parameters
        stats_datasets = StatsMakerDatasets(**kwargs)
        stats_dvs = StatsMakerDataverses(**kwargs)
        stats_files = StatsMakerFiles(**kwargs)
    else:
        stats_datasets = StatsMakerDatasets(**request.GET.dict())
        stats_dvs = StatsMakerDataverses(**request.GET.dict())
        stats_files = StatsMakerFiles(**request.GET.dict())

    # Start an OrderedDict
    resp_dict = OrderedDict()
    # -----------------------------------
    # Dataset deposits  each month - EASY
    # -----------------------------------
    if EASY_STATISTICS:
        # inclusive bulk deposits
        stats_monthly_deposit_counts = stats_datasets.get_easy_deposit_count_by_month()
        dataset_counts_by_category = stats_datasets.get_dataset_category_counts()
        files_downloads = stats_files.get_file_downloads_by_month()
        if not stats_monthly_deposit_counts.has_error():
            resp_dict['deposit_counts_by_month'] = list(stats_monthly_deposit_counts.result_data['records'])
        # exclusive bulk deposits
        stats_monthly_deposit_counts = stats_datasets.get_easy_deposit_count_by_month(True)
        if not stats_monthly_deposit_counts.has_error():
            resp_dict['deposit_counts_by_month_no_bulk'] = list(stats_monthly_deposit_counts.result_data['records'])

    if EASY_STATISTICS:
        resp_dict['out'] = str(list(stats_monthly_deposit_counts.result_data['records']))
        resp_dict['out'] = str(resp_dict['deposit_counts_by_month'])
        resp_dict['out'] = str(dataset_counts_by_category.result_data['records'])
        resp_dict['out'] = str(files_downloads.result_data['records'])
        resp_dict['file_counts_by_month'] = list(stats_monthly_deposit_counts.result_data['records'])
        resp_dict['deposit_counts_by_month'] = list(stats_monthly_deposit_counts.result_data['records'])
        resp_dict['dataverse_counts_by_month_sql'] = 'sql'
        resp_dict['dataset_counts_by_category'] = list(dataset_counts_by_category.result_data['records'])
        resp_dict['file_downloads_by_month'] = list(files_downloads.result_data['records'])
        resp_dict['form'] = form
        return render(request, 'metrics/metrics_total.html', resp_dict)
    else:
        return render(request, 'metrics/metrics_public.html', resp_dict)

@cache_page(get_metrics_cache_time())
def view_public_visualizations(request, **kwargs):
    """
    Return HTML/D3Plus visualizations for a variety of public statistics
    """
    resp_dict = {}

    if EASY_STATISTICS:
        if request.method == "POST":
            form = Metrics(request.POST)
        else:
            form = Metrics()
        kwargs["category"] = form.data.get("category", "audience")
        kwargs["start_date"] = form.data.get("start_date", "2017-01-01")
        kwargs["end_date"] = form.data.get("end_date", "2017-12-31")

    #kwargs["affiliation"] = "NIOO-KNAW"
    #kwargs["start_date"] = "2018-01-01"
    #kwargs["id"] = 686

    i = 0
    if i and kwargs and len(kwargs) > 0:
        # kwargs override GET parameters
        stats_datasets = StatsMakerDatasets(**kwargs)
        stats_dvs = StatsMakerDataverses(**kwargs)
        stats_files = StatsMakerFiles(**kwargs)
    else:
        stats_datasets = StatsMakerDatasets(**request.GET.dict())
        stats_dvs = StatsMakerDataverses(**request.GET.dict())
        stats_files = StatsMakerFiles(**request.GET.dict())

    # Start an OrderedDict
    resp_dict = OrderedDict()

    # -------------------------
    # Dataverses created each month
    # -------------------------
    # DANS count
    stats_result_dv_counts = stats_dvs.get_dataverse_counts_by_month(**request.GET.dict()) #_published()
    #return HttpResponse(stats_result_dv_counts.sql_query)
    #import ipdb; ipdb.set_trace()
    if not stats_result_dv_counts.has_error():
        resp_dict['dataverse_counts_by_month'] = list(stats_result_dv_counts.result_data['records'])
        resp_dict['dataverse_counts_by_month_sql'] = stats_result_dv_counts.sql_query

    #return HttpResponse(str(resp_dict))
    # -------------------------
    # Dataverse counts by type
    # -------------------------
    #stats_result_dv_counts_by_type =\
   #     stats_dvs.get_dataverse_counts_by_type_published(exclude_uncategorized=True)
    stats_result_dv_counts_by_type = stats_dvs.get_dataverse_counts_by_type(**request.GET.dict())
    #return HttpResponse(stats_result_dv_counts_by_type.sql_query)
    if not stats_result_dv_counts_by_type.has_error():
        resp_dict['dataverse_counts_by_type'] = stats_result_dv_counts_by_type.result_data['records']
        resp_dict['dv_counts_by_category_sql'] = stats_result_dv_counts_by_type.sql_query


    # -------------------------
    # Datasets created each month
    # -------------------------
    stats_monthly_ds_counts = stats_datasets.get_dataset_counts_by_create_date(**request.GET.dict())
    #stats_monthly_ds_counts = stats_datasets.get_dataset_counts_by_create_date(**request.GET.dict())
    #return HttpResponse(stats_monthly_ds_counts)
    if not stats_monthly_ds_counts.has_error():
        resp_dict['dataset_counts_by_month'] = list(stats_monthly_ds_counts.result_data['records'])
        resp_dict['dataset_counts_by_month_sql'] = stats_monthly_ds_counts.sql_query


    stats_ds_count_by_category = stats_datasets.get_dataset_category_counts(**request.GET.dict()) #_published()
    #stats_ds_count_by_category = stats_datasets.get_dataset_category_counts()
    #stats_ds_count_by_category = stats_datasets.get_dataverse_dataset_subject_counts(**request.GET.dict())
    #return HttpResponse(stats_ds_count_by_category)
    if not stats_ds_count_by_category.has_error():
        resp_dict['category'] = stats_datasets.get_category().capitalize()
        resp_dict['dataset_counts_by_category'] = stats_ds_count_by_category.result_data['records']
        #resp_dict['dataset_counts_by_month_sql'] = stats_monthly_ds_counts.sql_query

    # -------------------------
    # Files created, by month
    # -------------------------
    #stats_monthly_file_counts = stats_files.get_file_count_by_month_published()
    #return HttpResponse(stats_monthly_file_counts.sql_query)
    stats_monthly_file_counts = stats_files.get_file_count_by_month(**request.GET.dict())
    # DANS OK
    #return HttpResponse(stats_monthly_file_counts.query)
    #return HttpResponse(stats_monthly_file_counts.sql_query)
    if not stats_monthly_file_counts.has_error():
        resp_dict['file_counts_by_month'] = list(stats_monthly_file_counts.result_data['records'])
        resp_dict['file_counts_by_month_sql'] = stats_monthly_file_counts.sql_query

    # -------------------------
    # Files downloaded, by month
    # -------------------------
    stats_monthly_downloads = stats_files.get_file_downloads_by_month(include_pre_dv4_downloads=True, **request.GET.dict())
    #return HttpResponse(stats_monthly_downloads)
    if not stats_monthly_downloads.has_error():
        resp_dict['file_downloads_by_month'] = list(stats_monthly_downloads.result_data['records'])
        resp_dict['file_downloads_by_month_sql'] = stats_monthly_downloads.sql_query

    # -------------------------
    # File counts by content type
    # -------------------------
    # rp: removing this from current charts
    """
    stats_file_content_types = stats_files.get_datafile_content_type_counts_published()
    if not stats_file_content_types.has_error():
        resp_dict['file_content_types'] = list(stats_file_content_types.result_data)
        resp_dict['file_content_types_sql'] = stats_file_content_types.sql_query
        resp_dict['file_content_types_top_20'] = list(stats_file_content_types.result_data)[:20]
        #resp_dict['file_content_types_json'] = json.dumps(file_content_types, indent=4)
    """

    # -----------------------------------
    # Dataset deposits  each month - EASY
    # -----------------------------------
    if EASY_STATISTICS:
        # inclusive bulk deposits
        stats_monthly_deposit_counts = stats_datasets.get_easy_deposit_count_by_month()
        if not stats_monthly_deposit_counts.has_error():
            resp_dict['deposit_counts_by_month'] = list(stats_monthly_deposit_counts.result_data['records'])
        # exclusive bulk deposits
        stats_monthly_deposit_counts = stats_datasets.get_easy_deposit_count_by_month(True)
        if not stats_monthly_deposit_counts.has_error():
            resp_dict['deposit_counts_by_month_no_bulk'] = list(stats_monthly_deposit_counts.result_data['records'])

    if EASY_STATISTICS:
        resp_dict['form'] = form
        return render(request, 'metrics/metrics_easy.html', resp_dict)
    else:
        if request.GET.get('affiliation'):
	    affiliation = request.GET.get('affiliation')
            affiliation = affiliation.replace(' ', '_')
            affiliation = affiliation.replace('-', '_')
	    resp_dict[affiliation] = 'active'
        else:
            resp_dict['allaff'] = 'active'
        return render(request, 'metrics/metrics_public.html', resp_dict)

@cache_page(get_metrics_cache_time())
def view_public_visualizations_last12_dataverse_org(request):
    """
    Return visualizations covering the last 12 months+.

    e.g. If it's July 23, 2016, it will start from July 1, 2015
    e.g. If it's June 2, 2016, it will start from June 1, 2015
    """
    if not request.GET.get('iframe', None):
        return HttpResponseRedirect('http://dataverse.org')

    return view_public_visualizations_last12(request)


def view_file_extensions_within_type(request, file_type='application/octet-stream'):
    """Query as experiment.  View extensions for unidentified queries"""

    #file_type = 'data/various-formats'
    ids = Datafile.objects.filter(contenttype=file_type).values_list('dvobject__id', flat=True)

    #ids = Datafile.objects.all().values_list('dvobject__id', flat=True)
    l = FileMetadata.objects.filter(datafile__in=ids).values_list('label', flat=True)

    ext_list = [splitext(label)[-1] for label in l]

    extension_counts = {}
    for ext in ext_list:
        extension_counts[ext] = extension_counts.get(ext, 0) + 1

    ext_pairs = extension_counts.items()
    ext_pairs = sorted(ext_pairs, key=lambda k: k[1], reverse=True)

    d = dict(extension_counts=ext_pairs)

    return JsonResponse(d)


def view_files_by_type(request):

    stats_files = StatsMakerFiles(**request.GET.dict())

    # Start an OrderedDict
    resp_dict = OrderedDict()

    # -------------------------
    # Dataverses created each month
    # -------------------------
    success, file_content_types = stats_files.get_datafile_content_type_counts_published()
    if success:
        resp_dict['file_content_types'] = list(file_content_types)
        resp_dict['file_content_types_json'] = json.dumps(file_content_types, indent=4)

    return render(request, 'metrics/visualizations/file_content_types.html', resp_dict)
