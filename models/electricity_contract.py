# Copyright 2023 Miguel Subiran <miguel@navarmedia.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class Contract(models.Model):
    _name = 'electricity.contract.contract.electricity'
    _description = 'Contratos'

    nombre_contrato = fields.Char()
