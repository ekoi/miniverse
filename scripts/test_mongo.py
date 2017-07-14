if __name__ == '__main__':
    import os, sys
    import django
    from os.path import realpath, dirname
    proj_path = dirname(dirname(realpath(__file__)))

    sys.path.append(proj_path)
    #sys.path.append(dirname(proj_path))
    django.setup()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miniverse.settings.local")
    EASY_STATISTICS = 'true'

import random
import numpy as np
import pandas as pd
from django.db.models import F

from dv_apps.datasets.models import *
from dv_apps.datafiles.models import FileMetadata
from dv_apps.metrics.stats_util_base import StatsMakerBase
from dv_apps.metrics.stats_view_base import StatsViewSwagger
from dv_apps.metrics.stats_util_datasets import StatsMakerDatasets
from dv_apps.metrics.stats_util_files import StatsMakerFiles
# get_easy_dataset_category_counts

miniset = StatsMakerBase() 
datasets = StatsMakerDatasets()
files = StatsMakerFiles()
print "Dataset count %s: \n" % datasets.get_easy_dataset_category_counts()
print "Datasets count by month: \n %s" % datasets.get_easy_deposit_count_by_month().get_csv_content()
print "Files by months: \n %s " % files.get_easy_file_downloads_by_month().get_csv_content()
print "EASY categories: \n %s " % datasets.get_easy_dataset_category_counts() #.get_csv_content()
