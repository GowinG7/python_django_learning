from django.contrib import admin
#GGmomo model import gareko
from .models import GGmomo, momoReview, Store, momoCertificate

# Register your models here.
class momoReviewInline(admin.TabularInline):
    model = momoReview
    extra = 2 
    
class GGmomoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [momoReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('momo_varieties',)
    
class momoCertificateAdmin(admin.ModelAdmin):
    list_display = ('momo', 'certificate_number')

admin.site.register(GGmomo, GGmomoAdmin)
admin.site.register(momoReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(momoCertificate, momoCertificateAdmin)


