from __future__ import unicode_literals

from django.db import models

CATEGORY_CHOICES = (
    ('audience', 'Audience'),
    ('rights', 'Rights'),
    ('depositStatus', 'Deposit Status'),
    ('mimeType', 'Mime Type'),
)
DOWLOADS_CHOICES = (
    ('datasets', '(Part of) dataset'),
    ('files', 'File'),
)
CUMULATIVE_CHOICES = (
    ('noncumulative', 'Noncumulative'),
    ('cumulative_period', 'Period'),
    ('cumulative_begin', 'From beginning'),
)
DATE_CHOICES = (
    ('deposit', 'Deposit date'),
    ('publish', 'Publish date'),
)
IMPORT_CHOICES = (
    ('bulk_included', 'Bulk imports included'),
    ('bulk_excluded', 'Bulk imports excluded'),
)
START_DATE_CHOICES = (
    ('1991-01-01', '1991-01-01'),
    ('2007-01-01', '2007-01-01'),
    ('2008-01-01', '2008-01-01'),
    ('2009-01-01', '2009-01-01'),
    ('2010-01-01', '2010-01-01'),
    ('2011-01-01', '2011-01-01'),
    ('2012-01-01', '2012-01-01'),
    ('2013-01-01', '2013-01-01'),
    ('2014-01-01', '2014-01-01'),
    ('2015-01-01', '2015-01-01'),
    ('2016-01-01', '2016-01-01'),
    ('2017-01-01', '2017-01-01'),
)
END_DATE_CHOICES = (
    ('2006-12-31', '2006-12-31'),
    ('2007-12-31', '2007-12-31'),
    ('2008-12-31', '2008-12-31'),
    ('2009-12-31', '2009-12-31'),
    ('2010-12-31', '2010-12-31'),
    ('2011-12-31', '2011-12-31'),
    ('2012-12-31', '2012-12-31'),
    ('2013-12-31', '2013-12-31'),
    ('2014-12-31', '2014-12-31'),
    ('2015-12-31', '2015-12-31'),
    ('2016-12-31', '2016-12-31'),
    ('2017-12-31', '2017-12-31'),
    ('2099-12-31', '2099-12-31'),
    ('2015-01-31', '2015-01-31'),
)


class Metrics(models.Model):
    category = models.CharField(max_length=20,
                                choices=CATEGORY_CHOICES,
                                default='Audience')
    start_date = models.CharField(max_length=10,
                                choices=START_DATE_CHOICES,
                                default='2008-01-01')
    end_date = models.CharField(max_length=10,
                                choices=END_DATE_CHOICES,
                                default='2017-12-31')
    downloads = models.CharField(max_length=50,
                                choices=DOWLOADS_CHOICES,
                                default='files')
    cumulative = models.CharField(max_length=15,
                                choices=CUMULATIVE_CHOICES,
                                default='cumulative_period')
    date_type = models.CharField(max_length=15,
                                choices=DATE_CHOICES,
                                default='publish')
    bulk_import_included = models.CharField(max_length=15,
                                choices=IMPORT_CHOICES,
                                default='bulk_included')

    def __str__(self):
        return self.category