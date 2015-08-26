# -*- encoding: utf-8 -*-
from osv import fields, osv

class product_label_info(osv.osv):
	_name = 'product.product'
	_inherit = 'product.product'
	_columns = {
		'generic_name': fields.char('Nombre Generico', size=50 , help="nombre generico del articulo"),
		'sale_qty_multiple': fields.integer('Cantidad de venta'),
		'product_country': fields.many2one('res.country','Pais origen'),
		'risk_advices': fields.text('Riesgos de manejo', size=200),
		'handle': fields.text('Instrucciones de uso', size=200),
		'electric_info': fields.text('Caracteristicas electricas', size=200),
	}
product_label_info()

class country_asignment(osv.osv):
    _name = 'res.country'
    _inherit ='res.country'
    _columns = {
       'country_id': fields.one2many('product.product','product_country','Pais origen'),
        }