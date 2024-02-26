from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    nombre_contrato = fields.Char(string='Contrato', required=True)
    tipo_contrato_ids = fields.one2many(comodel_name='tipo.contrato', string='Tipo de contrato', required=True)

class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    tipocontrato_id = fields.many2one(comodel_name='contratos.electricos', string='Tipo de Contrato')
