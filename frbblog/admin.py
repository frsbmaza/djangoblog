from django.contrib import admin
from frbblog.models import author,category,article

# Register your models here.

class authorModel(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["__str__"]
	class Meta:
		Model = author
admin.site.register(author,authorModel)

class categoryModel(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["__str__"]
	list_per_page = 10
	class Meta:
		Model = category
admin.site.register(category,categoryModel)

class articleModel(admin.ModelAdmin):
	list_display = ["__str__","posted_on"]
	search_fields = ["__str__","details"]
	list_filter = ["posted_on",'category']
	list_per_page = 20
	class Meta:
		Model = article
admin.site.register(article,articleModel)