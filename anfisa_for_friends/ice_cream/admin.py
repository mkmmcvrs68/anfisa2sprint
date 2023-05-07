from django.contrib import admin
from .models import Category, Wrapper, Topping, IceCream
# Register your models here.


admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    list_filter = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
