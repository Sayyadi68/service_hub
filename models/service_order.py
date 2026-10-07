from odoo import fields, models


class ServiceOrder(models.Model):
    _name = 'service.order'
    _description = 'Service Order'
    _order = 'date_order desc, id desc'

    name = fields.Char(string='شماره سفارش', required=True, default='New', copy=False)
    request_id = fields.Many2one('service.request', string='درخواست', required=True, ondelete='restrict')
    customer_id = fields.Many2one('res.partner', string='مشتری', related='request_id.customer_id', store=True)
    technician_id = fields.Many2one('res.users', string='تکنسین', related='request_id.technician_id', store=True)
    service_type_id = fields.Many2one('service.type', string='نوع خدمت', related='request_id.service_type_id', store=True)
    amount = fields.Float(string='مبلغ', related='request_id.total_price', store=True)
    date_order = fields.Datetime(string='تاریخ سفارش', default=fields.Datetime.now)
    notes = fields.Text(string='یادداشت')