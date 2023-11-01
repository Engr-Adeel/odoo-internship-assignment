from odoo import fields, models,api
from odoo.exceptions import UserError,ValidationError
class EstateProperties(models.Model):

	_name = "estate.property"

	_description = "Model for Real-Estate Properties"

	status=fields.Char(string='Status', default='Available')
	name = fields.Char(string='Name',required=True)
	prperty_type_id = fields.Many2one("estate.property.type",string='Type',required=True)
	description = fields.Text(string='Description')
	postcode = fields.Char(string='Postcode')
	date_availability = fields.Date(string='Availability Date',)
	expected_price = fields.Float(string='Expected Price',required=True,default=0)
	selling_price = fields.Float(string='Selling Price',)
	bedrooms = fields.Integer(string='Bedrooms',)
	living_areas = fields.Integer(string='Living Areas',)
	facades = fields.Integer(string='Facades',)
	garage = fields.Boolean(string='Garage',)
	garden = fields.Boolean(string='Garden',)
	garden_area = fields.Integer(string='Garden Area',)
	garden_orientation = fields.Selection([('North','North'),('South','South'),('East','East'),('West','West')],string='Garden Orientation',)
	buyer = fields.Many2one("estate.property.buyer",string='Buyer',)
	saleman = fields.Many2one("estate.property.saleman",string='Saleman')
	total_area=fields.Float(compute="_compute_total")
 
	@api.depends("living_areas","garden_area")
	def _compute_total(self):
		for record in self:
			record.total_area = record.garden_area + record.living_areas
	
	@api.onchange("garden")
	def _onchange_garden(self):
		if self.garden:
			self.garden_area = 10
			self.garden_orientation = 'North'
		else:
			self.garden_area = 0
			self.garden_orientation = ''

	@api.constrains('selling_price')
	def _check_selling_price(self):
		for record in self:
			if record.selling_price < (record.expected_price/100)*90:
				raise ValidationError("Selling price must be greater than 90 percent of Expected price")



	def sold_button(self):
		for record in self:
			if record.status=='Available':
				record.status = "Sold"
			else:
				raise UserError("Sold Property cannot be sold again !")
		return True

	def cancel_button(self):
		for record in self:
			if record.status=='Available':
				record.status = "Cancel"
			else:
				raise UserError("This property cannot be canelled !")
		return True
		
 

            

