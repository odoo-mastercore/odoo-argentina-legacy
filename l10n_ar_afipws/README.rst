=========================================
Modulo Base para los Web Services de AFIP
=========================================

Homologation / production:
--------------------------

First it search for a paramter "afip.ws.env.type" if exists and:

* is production --> production
* is homologation --> homologation

Incluye:
--------

* Wizard para instalar los claves para acceder a las Web Services.
* API para realizar consultas en la Web Services desde Odoo.

El módulo l10n_ar_afipws permite a Odoo acceder a los servicios del AFIP a
travésde Web Services. Este módulo es un servicio para administradores y
programadores, donde podrían configurar el servidor, la autentificación
y además tendrán acceso a una API genérica en Python para utilizar los
servicios AFIP.
