{
	'name': 'DGI Partners Panamá',
    'version': '1.1c',
    'category': 'Hidden/Dependency',
    'description': """
	Pestaña Partners Panama DGI
	Parámetros para idendificar a los contribuyentes en la Rep. de Panamá
	RUC, DV y Tipo de Persona; Tabla maestra de Conceptos de Anexos, Clasificaión por linea de la factura de partner proveedor del concepto de anexo DGI Panama
	version: 19-04-21
""",
    'author': 'Alconsoft-Sistech e ITGeo Panamá',
    'website': 'http://alconsoft.net',
    'depends': ['account',],
    'init_xml':[],
    'data': ['vista_partner_panama.xml',
             'anexosconceptos.csv',
             'reports/report_anexos_itgeo.xml'],
    'demo': [],
    'installable': True,
    'application': True,
}
