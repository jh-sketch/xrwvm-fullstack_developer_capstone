from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class (inline editing of CarModel in CarMake admin)
class CarModelInline(admin.TabularInline):  # or admin.StackedInline
    model = CarModel
    extra = 1  # How many empty CarModel forms to show
    

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)
    

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)
    

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
