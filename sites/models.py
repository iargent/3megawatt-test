from django.db import models
from django.db.models import Sum

# Create your models here.

class Site(models.Model):
	name = models.CharField('name of site', max_length=200)
	def __str__(self):
		return self.name
	@staticmethod
	def sum_by_site():
    		return Site.objects.annotate(A_value=Sum('visit__A_value')).annotate(B_value=Sum('visit__B_value'))
	@staticmethod
	def avg_by_site():
		return Site.objects.raw('select s.id, name, round(avg(A_value),2) as A_value, round(avg(B_value),2) as B_value from sites_site s inner join sites_visit sv on sv.site_id_id=s.id group by s.id order by s.id;')

class Visit(models.Model):
	site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
	when = models.DateField('date site visited')
	A_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	B_value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
