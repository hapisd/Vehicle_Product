# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VehicleBrand(models.Model):
    _name = 'vehicle.brand'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehicle Brand'

    image = fields.Binary(string='Image')
    name = fields.Char(string='Brand Name', required=True)
    description = fields.Text(string='Description')
    ref = fields.Char(string='Reference', readonly=True, required=True, index=True, copy=False, default='/')
    
    type_line = fields.One2many('vehicle.type', 'brand_id', string='Model', ondelete='cascade')
    model_line = fields.One2many('vehicle.model', 'type_id', string='Model', ondelete='cascade')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('vehicle.brand.sequence')
        return super(VehicleBrand, self).create(vals)

class VehicleType(models.Model):
    _name = 'vehicle.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehicle Type'

    brand_id = fields.Many2one('vehicle.brand', string='Brand', required=True)
    
    image = fields.Binary(string='Image')
    name = fields.Char(string='Type Name', required=True)
    description = fields.Text(string='Description')
    ref = fields.Char(string='Reference', readonly=True, default='/')

    model_line = fields.One2many('vehicle.model', 'type_id', string='Model', ondelete='cascade')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('vehicle.type.sequence')
        return super(VehicleType, self).create(vals)

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehicle Model'

    brand_id = fields.Many2one('vehicle.brand', string='Brand', required=True)
    type_id = fields.Many2one('vehicle.type', string='Type', required=True)

    # vehicle_type = fields.Char(related='brand_id.type_id')
    image = fields.Binary(string='Image')
    name = fields.Char(string='Model Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    ref = fields.Char(string='Reference', readonly=True, default='/')

    price_line = fields.One2many('vehicle.price', 'model_id', string='Price', ondelete='cascade')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('vehicle.model.sequence')
        return super(VehicleModel, self).create(vals)

class VehicleYear(models.Model):
    _name = 'vehicle.year'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehicle Year'

    model_list = fields.Many2many('vehicle.model', 'year_model_rel', 'year_id', 'model_id', string='Models')

    name = fields.Char(string='Year', required=True)
    description = fields.Text(string='Description')
    
    price_line = fields.One2many('vehicle.price', 'year_id', string='Price', ondelete='cascade')

class VehiclePrice(models.Model):
    _name = 'vehicle.price'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Vehicle Price'

    model_id = fields.Many2one('vehicle.model', string='Model', required=True)
    year_id = fields.Many2one('vehicle.year', string='Year', required=True)

    name = fields.Char(string='Price', required=True)
    description = fields.Text(string='Description')
    ref = fields.Char(string='Reference', readonly=True, required=True, index=True, copy=False, default='/')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('vehicle.price.sequence')
        return super(VehiclePrice, self).create(vals)
