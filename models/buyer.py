from odoo import fields, models,api

class Buyer(models.Model):

	_name = "estate.property.buyer"

	_description = "Model for Buyers"


	name = fields.Char(string='Name',required=True)
	
