from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    nombre_contrato = fields.Char(string='Contrato', required=True)
    tipo_contrato_ids = fields.One2many('tipo.contrato', 'tipocontrato_id', string='Tipo de contrato', required=True)

class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    tipocontrato_id = fields.Many2one('contratos.electricos', 'tipo_contrato_ids', string='Tipo de Contrato', required=True)
