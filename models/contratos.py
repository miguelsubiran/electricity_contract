from odoo import models, fields

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    #nombre_contrato = fields.Char(string='Contrato', required=True)
    fecha_firma=fields.Date(string='Fecha de firma')
    fecha_alta=fields.Date(string='Fecha de alta')
    fecha_vencimiento=fields.Date(string='Fecha de Vto.')
    #dias_hasta_vto=fields.char(compute="_get_diasvto")
    estado_id=fields.Many2one('estado.contrato',string='Estado')
    tipo_contrato_id = fields.Many2one('tipo.contrato', string='Tipo de contrato')
    cliente_id = fields.Many2one('res.partner',string='Cliente')
    comercial_id = fields.Many2one('comercial.contrato',string='Comercial')
    cups_id=fields.Many2one('cups.contrato',string='CUPS')
    comercializadora_id=fields.Many2one('comercializadora.contrato', string='Comercializadora')

    #@api.one
    #@api.depends('fecha_vencimiento')
    def _get_diasvto(self):
        for contratos in self:
            if isinstance(contratos.fecha_vencimiento):
                contratos.fecha_vencimiento=contratos.fecha_alta
                #contratos.dias_hasta_vto = "0 dias"
            #else:
                #numdias.dias_hasta_vto == str(numdias.fecha_vencimiento-datetime.today())+" días"

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

class ComercialContrato(models.Model):
    _name = 'comercial.contrato'
    _description='Comerciales'

    name=fields.Char(string='Comercial')