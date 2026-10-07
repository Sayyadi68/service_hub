from odoo import fields, models


class ServiceOffer(models.Model):
    _name = 'service.offer'
    _description = 'Service Offer'
    _order = 'price desc'

    request_id = fields.Many2one('service.request', string='درخواست', required=True, ondelete='cascade')
    technician_id = fields.Many2one('res.users', string='تکنسین', required=True)
    price = fields.Float(string='قیمت', required=True)
    validity = fields.Integer(string='اعتبار پیشنهاد', default=7)
    date_offer = fields.Date(string='تاریخ پیشنهاد', default=fields.Date.today)
    date_deadline = fields.Date(string='تاریخ انقضا')
    status = fields.Selection([
        ('draft', 'پیش‌نویس'),
        ('accepted', 'تأیید شده'),
        ('refused', 'رد شده'),
    ], string='وضعیت', default='draft', copy=False)
    