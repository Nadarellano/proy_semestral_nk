from django.urls import path
from .views import girasoles, index, carrito, nosotros, Ceratostigma, coprosma,datos_seguimiento, Diosma
from .views import girasoles, leonotis, liliums, mac_amarillo, mac_gris,mac_negro, mac_rojo
from .views import nandinas, pago, prod_arbustos, prod_flores, prod_maceteros,prod_sustratos, registrodos
from .views import rosas, stenocarpus, stock, terminos_condiciones, tierra_biológica, tierra_compost, tierra_hoja
from .views import tierra_humus, tulipanes, ubicacion_compra, veronicas, viburnum







urlpatterns = [
    path('', index,name='index'),
    path('index', index,name='index'),
    path('carrito', carrito,name='carrito'),
    path('nosotros', nosotros, name='nosotros'),
    path('Ceratostigma', Ceratostigma, name='Ceratostigma'),
    path('coprosma', coprosma, name='coprosma'),
    path('datos_seguimiento', datos_seguimiento, name='datos_seguimiento'),
    path('Diosma', Diosma, name='Diosma'),
    path('girasoles', girasoles, name='girasoles'),
    path('leonotis', leonotis, name='leonotis'),
    path('liliums', liliums, name='liliums'),
    path('mac_amarillo', mac_amarillo, name='mac_amarillo'),
    path('mac_gris', mac_gris, name='mac_gris'),
    path('mac_negro', mac_negro, name='mac_negro'),
    path('mac_rojo', mac_rojo, name='mac_rojo'),
    path('nandinas', nandinas, name='nandinas'),
    path('pago', pago, name='pago'),
    path('prod_arbustos', prod_arbustos, name='prod_arbustos'),
    path('prod_flores', prod_flores, name='prod_flores'),
    path('prod_maceteros', prod_maceteros, name='prod_maceteros'),
    path('prod_sustratos', prod_sustratos, name='prod_sustratos'),
    path('registrodos', registrodos, name='registrodos'),
    path('rosas', rosas, name='rosas'),
    path('stenocarpus', stenocarpus, name='stenocarpus'),
    path('stock', stock, name='stock'),
    path('terminos_condiciones', terminos_condiciones, name='terminos_condiciones'),
    path('tierra_biológica', tierra_biológica, name='tierra_biológica'),
    path('tierra_compost', tierra_compost, name='tierra_compost'),
    path('tierra_hoja', tierra_hoja, name='tierra_hoja'),
    path('tierra_humus', tierra_humus, name='tierra_humus'),
    path('tulipanes', tulipanes, name='tulipanes'),
    path('ubicacion_compra', ubicacion_compra, name='ubicacion_compra'),
    path('veronicas', veronicas, name='veronicas'),
    path('viburnum', viburnum, name='viburnum'),

    
]