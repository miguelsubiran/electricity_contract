from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    #nombre_contrato = fields.Char(string='Contrato', required=True)
    fecha_firma=fields.date(string='F.firma')
    estado_id=fields.Many2one('estado.contrato',string='Estado')
    fecha_alta=fields.date(string='F.alta')
    tipo_contrato_id = fields.Many2one('tipo.contrato', string='Tipo de contrato')
    partner_id = fields.Many2one('res.partner',string='Cliente')


class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    name = fields.Char(string='Tipo de Contrato')

class EstadoContrato(models.Model):
    _name = 'estado.contrato'
    _description='Estados de Contrato'

    name=fields.Char(string='Estados de Contrato')
