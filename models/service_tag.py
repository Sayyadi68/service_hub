from odoo import fields, models


class ServiceTag(models.Model):
    _name = 'service.tag'
    _description = 'Service Tag'

    name = fields.Char(string='نام', required=True)
    color = fields.Integer(string='رنگ')