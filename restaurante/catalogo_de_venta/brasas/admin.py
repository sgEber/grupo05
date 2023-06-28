from django.contrib import admin
from .models import Usuario, Categoria, Producto, Pedido, DetallePedido

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio']
    list_filter = ['categoria']
    search_fields = ['nombre']

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha', 'estado']
    list_filter = ['estado']
    search_fields = ['usuario__nombre']
    inlines = [DetallePedidoInline]

admin.site.site_header = 'Administración del Restaurante'
admin.site.site_title = 'Restaurante Admin'