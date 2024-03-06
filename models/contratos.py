from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    #nombre_contrato = fields.Char(string='Contrato', required=True)
    fecha_firma=fields.Date(string='F.firma')
    estado_id=fields.Many2one('estado.contrato',string='Estado')
    fecha_alta=fields.Date(string='F.alta')
    fecha_vencimiento=fields.Date(string='F.Vto.')
    tipo_contrato_id = fields.Many2one('tipo.contrato', string='Tipo de contrato')
    partner_id = fields.Many2one('res.partner',string='Cliente')
    comercial = fields.Many2one('res.user',string='Comercial')
    cups=fields.many2one('cups.contrato',string='CUPS')
    comercializadora=fields.many2one('comercializadora.contrato', string='Comercializadora')


class TipoContrato(models.Model):
    _name = 'tipo.contrato'
    _description = 'Tipos de Contrato'

    name = fields.Char(string='Tipo de Contrato')

class EstadoContrato(models.Model):
    _name = 'estado.contrato'
    _description='Estados de Contrato'

    name=fields.Char(string='Estados de Contrato')

class CupsContrato(models.Model):
    _name = 'cups.contrato'
    _description='CUPS'

    name=fields.Char(string='CUPS')
    domicilio=fields.Char(string='Domicilio')
    cod_postal=fields.Char(string='Cod.Postal')
    provincia=fields.Char(string='Provincia')
    poblacion=fields.Char(string='Población')

class ComercializadoraContrato(models.Model):
    _name = 'comercializadora.contrato'
    _description='Comercializadoras'

    name=fields.Char(string='Comercializadora')
