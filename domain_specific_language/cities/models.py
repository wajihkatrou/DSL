from django.db import models


#To prevent redundancy when filling the table, we split the schema into two models and we add foreign key link between them

class City(models.Model):

	code = models.IntegerField()
	name = models.CharField(max_length = 100)
	population = models.IntegerField()
	average_age = models.FloatField()
	distr_code = models.IntegerField()
	dept_code = models.IntegerField()
	region = models.ForeignKey("Region", to_field="region_code", db_column="region_code", related_name = "city_region", on_delete=models.CASCADE)
	
	class Meta:
		verbose_name = "Town"


class Region(models.Model):

	region_code = models.IntegerField(unique=True)
	region_name = models.CharField(max_length = 100)
	
	class Meta:
		verbose_name = "Region"
