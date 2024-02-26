from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    nombre_contrato = fields.Char(string='Contrato', required=True)
    tipo_contrato_id = fields.Many2one('tipo.contrato', string='Tipo de contrato')

class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    name = fields.Char(string='Tipo de Contrato')
