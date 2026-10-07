from odoo import fields, models


class ServiceType(models.Model):
    _name = 'service.type'
    _description = 'Service Type'

    name = fields.Char(string='نام خدمت', required=True)
    description = fields.Text(string='توضیحات')
    base_price = fields.Float(string='قیمت پایه')
    duration = fields.Float(string='مدت تقریبی')
    active = fields.Boolean(string='فعال', default=True)