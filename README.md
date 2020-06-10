
# Odoo Localization for Argentinians Partners

For Entrepreneurs, MiPyme's, SME, Companies, Autónomos. 
Work made from:

 - [ingadhoc/odoo-argentina-ce](https://github.com/ingadhoc/odoo-argentina-ce)
 - [ingadhoc/odoo-argentina](https://github.com/ingadhoc/odoo-argentina)
 - [ingadhoc/account-payment](https://github.com/ingadhoc/account-payment)
 - [ingadhoc/account-financial-tools](https://github.com/ingadhoc/account-financial-tools)

Thanks to ingadhoc folks, for their efforts and dedication!
:star: :star: :star: :star: :star:


# Localización Odoo Argentina (CE)
Versión 13.0 Community edition

------

**Versión fork de los amigos de ADHOC, ¡Gracias totales!.**

------

### Releases incrementales:

#### [13.0/BaseEI](https://github.com/odoo-mastercore/odoo-argentina/releases/tag/13.0%2FBaseEI)
- WebServices Implementados para Factura Electrónica AFIP (+ND, +NC, +FCEMiPyme)
- Duplicado y Triplicado de Facturas
- Reporte de Libro IVA Ventas, Compras
- Reporte de IIBB en Ventas y Compras por Jurisdicción
- Agregado CBU a Bancos y listado de Bancos Argentinos
#### [13.0/Withholding](https://github.com/odoo-mastercore/odoo-argentina/releases/tag/13.0%2FWithholding)
- Gestión de Cheques 
- Operaciones de pagos con múltiples lineas/medios de pago
- Impuestos de retención, cómputo automático de ellas y certificados
- Mejoras en UX
#### [13.0/RegInfAFIP](https://github.com/odoo-mastercore/odoo-argentina/releases/tag/13.0%2FRegInfAFIP)
- Mejora en conexión AFIP y formato de CUIT
- Incorporación de consulta de Actividades, Conceptos e Impuestos AFIP
- Incorporación de consulta de datos de padrón A5 para Contactos (Clientes y Proveedores)
- Regimen de Información AFIP R.G. 3685 y Libro de IVA Digital Compras/Ventas -R.G. 4597-
<!--
#### 13.0/MercadoPago (Future)
- Método de Pago MercadoPago
#### 13.0/CotizacionUSDAFIP (Future)
- Actualización automática de cotización USD
#### 13.0/ConsultComprobantes (Future)
- Consulta de Comprobantes AFIP (web service AFIP de constatación de comprobantes)
#### 13.0/PercIIBB (Future)
- TXT Reg. Inf. para Agentes de percepción IIBB
#### 13.0/MercadoLibre (Future)
- Integración con MercadoLibre
-->

#### Dependencias externas:

- wheel
- python3-openssl | pyOpenSSL
- M2Crypto
- cryptography
- httplib2
- git+https://github.com/pysimplesoap/pysimplesoap@stable_py3k
- git+https://github.com/ingadhoc/pyafipws@py3k

#### Instalar Dependencias externas:

```
pip3 install -r requirements.txt
```

#### Usando Docker podeis serviros de la imagen:

```
docker pull pandoo/odoo:13.0
```

### Simplemente instalar el módulo:

- l10n_ar_bundle :relaxed:

### O si no, instalar los módulos en este orden:

- l10n_ar (embebido en Odoo Community edition)
- l10n_ar_afipws
- l10n_ar_afipws_fe
- l10n_ar_invoice_reports
- l10n_ar_reports 
- l10n_ar_bank
- account_payment_fix
- account_financial_amount
- account_withholding
- account_payment_group
- account_withholding_automatic
- account_check
- account_payment_group_document
- l10n_ar_ux
- l10n_ar_account_withholding
