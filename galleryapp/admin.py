from django.contrib import admin 
from django.utils.html import format_html

from .models import Carousel,Category_Activity_Gallery, Activity_Gallery, GalleryImage
from .forms import MyCustomForm


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('thumbnail',)  # Display the thumbnail and title in the list view

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;" />', obj.image.url)
        return "No Image"
    
    thumbnail.short_description = 'Thumbnail'  # Set column header in the admin panel

    class Media:
        js = ['src/js/jquery.js', 'src/js/image-compression/image_compress.js', 'src/js/image-compression/carousel.js']


admin.site.register(Category_Activity_Gallery)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    readonly_fields = ('thumbnail',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 100px; width: auto;"/>',
                obj.image.url
            )
        return 'No Image'
    thumbnail.short_description = 'Thumbnail'




@admin.register(Activity_Gallery)
class Activity_GalleryAdmin(admin.ModelAdmin):
    # form = GalleryAdminForm
    form = MyCustomForm
    inlines = [GalleryImageInline]

    class Media:
        js = ['src/js/jquery.js', 'src/js/image-compression/image_compress.js', 'src/js/image-compression/gallery_activity.js']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'gallery', 'image')

    class Media:
        js = ['src/js/jquery.js', 'src/js/image-compression/image_compress.js', 'src/js/image-compression/gallary_image_inline.js']

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 100px; width: auto;"/>',
                obj.image.url
            )
        return 'No Image'
    thumbnail.short_description = 'Thumbnail'