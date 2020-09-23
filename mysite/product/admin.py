

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

import mysite
# Register your models here.
from product.models import catagory, product, Images

from product.models import Comment

from product.models import Size, Color, Variants
import admin_thumbnails


class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(qs,
                Product,
                'categoriy',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = catagory.objects.add_related_count(qs,
                 product,
                 'catagory',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    #readonly_fields = ('id',)
    extra = 5

class ProductVariantsInline(admin.TabularInline):
    model=Variants
    #readonly_fields = ('image_tag')
    extra = 1
    show_change_link = True


@admin_thumbnails.thumbnail('image')
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class productAdmin(admin.ModelAdmin):
     list_display = ['title','catagory','status']
     list_filter = ['status']
     #readonly_fields = ('image_tag',)
     inlines =[ProductImageInline,ProductVariantsInline]
     prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields= ('subject','comment','ip','user','product','rate')

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','code','color_tag']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']

class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','color','size','price','quantity','image_tag']


admin.site.register(catagory,CategoryAdmin2)
admin.site.register(product,productAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Images)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)

