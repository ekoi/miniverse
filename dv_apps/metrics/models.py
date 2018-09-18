from __future__ import unicode_literals

from django.db import models

CATEGORY_CHOICES = (
    ('audience', 'Audience'),
    ('rights', 'Rights'),
    ('depositStatus', 'Deposit Status'),
    ('mimeType', 'Mime Type'),
)
START_DATE_CHOICES = (
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
                                default='2017-07-17')

    def __str__(self):
        return self.category
