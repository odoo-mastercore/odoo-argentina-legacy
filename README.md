
# Odoo Localization for Argentinians Partners

Entrepreneurs, MiPyme's, SME, Companies, Aut  nomos. 
Work made from ingadhoc/odoo-argentina-ce repositories. 
Thanks to ingadhoc folks, for their efforts and dedication!


# Localización Odoo Argentina (CE)
Versión 13.0 Community edition

------

**Versión fork de los amigos de ADHOC, ¡Gracias totales!.**

------

### Releases incrementales:

#### 13.0/BaseEI
- WebServices Implementados para Factura Electrónica AFIP (+ND, +NC, +FCEMiPyme)
- Duplicado y Triplicado de Facturas
- Reporte de Libro IVA Ventas, Compras
- Reporte de IIBB en Ventas y Compras por Jurisdicción
- Agregado CBU a Bancos y listado de Bancos Argentinos
#### 13.0/Withholding
- Gestión de Cheques 
- Operaciones de pagos con múltiples lineas/medios de pago
- Impuestos de retención, cómputo automático de ellas y certificados
- Mejoras en UX
#### 13.0/FEImp (WIP)
- Fix en conexión AFIP y formato de CUIT
- Incorporación de consulta de padrón A5
- Incorporación de consulta de Actividades, Conceptos e Impuestos AFIP
- Consulta de Comprobantes AFIP (web service AFIP de constatación de comprobantes )
- Actualización automática de cotización USD
<!--
#### 13.0/RegInfAFIP (Future)
- TXT Reg. Inf. Compras/Ventas
- TXT Reg. Inf. para Agentes de percepción IIBB
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

### Instalar los módulos en este orden:

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
