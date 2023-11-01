from odoo import fields, models,api

class Saleman(models.Model):

	_name = "estate.property.saleman"

	_description = "Model for Salemen"


	name = fields.Char(string='Name',required=True)
	
