
#Odoo Localization for Argentinians Partners

Entrepreneurs, MiPyme's, SME, Companies, Aut  nomos. 
Work made from ingadhoc/odoo-argentina-ce and ctmil/odoo-argentina repositories. 
Thanks to these folks!


# Localización Odoo Argentina (CE)
Versión 13.0 Community edition

------

**Versión fork de los amigos de ADHOC y Moldeo, ¡Gracias totales!.**

------

### Comprende las siguientes funcionalidades:

- WebServices Implementados para Factura Electrónica AFIP (+ND, +NC, +FCEMiPyme)
- Duplicado y Triplicado de Facturas
- Reporte de Libro IVA Ventas, Compras
- Reporte de IIBB en Ventas y Compras por Jurisdicción
<!--- Cheques 
- Recibos para pagos con múltiples medios de pago
- Percepciones
- Retenciones
- Tipo de Cambio Automático -->

#### Dependencias externas:

- python3-openssl | pyOpenSSL
- M2Crypto
- cryptography
- httplib2
- pyafipws
- pysimplesoap

#### Instalar Dependencias externas:

```
pip3 install -r requirements.txt
```

#### Usando Docker podeis serviros de la imagen:

```
docker pull pandoo/odoo:13.0
```

### Instalar los módulos en este orden:

- l10n_ar (embebido en Odoo Community edition)
- l10n_ar_afipws
- l10n_ar_afipws_fe
- l10n_ar_invoice_reports
- l10n_ar_reports 

