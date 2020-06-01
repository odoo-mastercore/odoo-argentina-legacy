# Localización Odoo Argentina
Versión 13.0 Community edition

------

**Versión frok de los amigos de Moldeo interactive y esta de ADHOC, Gracias totales.**

------

### Comprende las siguientes funcionalidades:

- Factura Electrónica
- Cheques
- Recibos para pagos con múltiples medios de pago
- Percepciones
- Retenciones
- Tipo de Cambio Automático

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
*En Docker se debe primero hacer update, upgrade e instalar el paquete git*

#### Descargar la imagen Docker:

```
url
```

### Instalar los módulos en este orden:

- l10n_ar (embebido en Odoo Community edition)
- l10n_ar_afipws
- l10n_ar_afipws_fe
- l10n_ar_bank PENDIENTE
- l10n_ar_vouchers
- 

