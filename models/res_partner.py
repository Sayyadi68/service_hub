from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    service_request_ids = fields.One2many('service.request', 'customer_id', string='درخواست‌های خدمات')
    service_request_count = fields.Integer(string='تعداد درخواست‌ها', compute='_compute_service_request_count')

    def _compute_service_request_count(self):
        for partner in self:
            partner.service_request_count = len(partner.service_request_ids)