# Copyright 2023 Miguel Subiran <miguel@navarmedia.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

class Contract(models.Model):
    _name = "contract"
    _description = "Contratos"
    _order = "priority desc, name"

nombre_contrato = fields.char('Name', required=True)