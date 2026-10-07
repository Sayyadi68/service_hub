from odoo import fields, models


class ServiceRequest(models.Model):
    _name = 'service.request'
    _description = 'Service Request'
    _order = 'request_date desc, id desc'

    name = fields.Char(string='شماره درخواست', required=True, default='New', copy=False)
    customer_id = fields.Many2one('res.partner', string='مشتری', required=True)
    service_type_id = fields.Many2one('service.type', string='نوع خدمت', required=True)
    description = fields.Text(string='شرح درخواست')
    stage = fields.Selection([
        ('new', 'جدید'),
        ('review', 'در حال بررسی'),
        ('offer', 'منتظر پیشنهاد'),
        ('approved', 'تأیید شده'),
        ('progress', 'در حال انجام'),
        ('done', 'انجام شده'),
        ('cancel', 'لغو شده'),
    ], string='مرحله', default='new', required=True)
    technician_id = fields.Many2one('res.users', string='تکنسین')
    tag_ids = fields.Many2many('service.tag', string='برچسب‌ها')
    request_date = fields.Datetime(string='تاریخ درخواست', default=fields.Datetime.now, required=True)
    planned_date = fields.Datetime(string='تاریخ برنامه‌ریزی')
    completion_date = fields.Datetime(string='تاریخ تکمیل')
    estimated_price = fields.Float(string='قیمت تخمینی')
    total_price = fields.Float(string='قیمت نهایی')
    priority = fields.Selection([
        ('0', 'عادی'),
        ('1', 'متوسط'),
        ('2', 'مهم'),
        ('3', 'فوری'),
    ], string='اولویت', default='0')
    is_urgent = fields.Boolean(string='فوری')
    active = fields.Boolean(string='فعال', default=True)
    offer_ids = fields.One2many('service.offer', 'request_id', string='پیشنهادها')
    order_ids = fields.One2many('service.order', 'request_id', string='سفارش‌ها')
