from odoo import fields, models,api

class EstatePropertyType(models.Model):

	_name = "estate.property.type"

	_description = "Model for type of property"


	name = fields.Char(string='Name',required=True)
	
