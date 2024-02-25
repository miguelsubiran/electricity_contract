# Copyright 2023 Miguel Subiran <miguel@navarmedia.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class Contract(models.Model):
    _name = 'electricity.contract.contract.electricity'
    _description = 'Contratos'

    nombre_contrato = fields.Char(string='Contrato', required=True)
    partner_name = fields.Char(string='Cliente', required=True)