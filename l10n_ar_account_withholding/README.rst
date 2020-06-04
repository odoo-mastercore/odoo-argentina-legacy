.. |company| replace:: ADHOC SA

.. |icon| image:: https://raw.githubusercontent.com/ingadhoc/maintainer-tools/master/resources/adhoc-icon.png

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==============================================
Automatic Argentinian Withholdings on Payments
==============================================

Tablas modificadas según: http://www.afip.gob.ar/noticias/20160526GananciasRegRetencionModificacion.asp

TODO:
    -A script de instalación sumarle algo tipo esto, por ahora se puede correr manual. En realidad solo es necesario si estamos en localización o algo que requiera doble validation
    -UPDATE account_payment_group SET retencion_ganancias='no_aplica' WHERE retencion_ganancias is null;
    - el ajuste de calculo de impuestos en pedidos de venta (por compatibilidad con arba) lo hicimos en sale_usability, habria que hacerlo en un modulo de la localización

Credits
=======

* |company| |icon|