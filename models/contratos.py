from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    nombre_contrato = fields.Char(string='Contrato', required=True)
    tipo_contrato_ids = fields.Many2one('tipo.contrato', 'tipocontrato_id', string='Tipo de contrato')

class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    tipocontrato_id = fields.One2many('contratos.electricos', 'tipo_contrato_ids', string='Tipo de Contrato', required=True)
