from odoo import models, fields
from datetime import date

class contratos(models.Model):
    _name = 'contratos.electricos'
    _description = 'Contratos'

    #nombre_contrato = fields.Char(string='Contrato', required=True)
    fecha_firma=fields.Date(string='Fecha de firma')
    fecha_alta=fields.Date(string='Fecha de alta')
    fecha_vencimiento=fields.Date(string='Fecha de Vto.')
    dias_hasta_vto=fields.Char(compute="_get_diasvto")
    estado_id=fields.Many2one('estado.contrato',string='Estado')
    tipo_contrato_id = fields.Many2one('tipo.contrato', string='Tipo de contrato')
    cliente_id = fields.Many2one('res.partner',string='Cliente')
    comercial_id = fields.Many2one('comercial.contrato',string='Comercial')
    usuario_id = fields.Many2one('res.users',string='Usuario')
    cups_id=fields.Many2one('cups.contrato',string='CUPS')
    comercializadora_id=fields.Many2one('comercializadora.contrato', string='Comercializadora')
    cups_domicilio = fields.Char(string="Domicilio")
    cups_poblacion = fields.Char(string="Poblacion")
    cups_cod_postal = fields.Char(string="Cod. Postal")
    cups_provincia = fields.Many2one('res.country.state', string="Provincia")
    observaciones = fields.Text(string="Observaciones")
    #incidencia_ids = fields.Many2many('incidencias.contrato', string="Incidencias de Contrato")

    #@api.one
    #@api.depends('fecha_vencimiento')
    def _get_diasvto(self):
        for contratos in self:
            if isinstance(contratos.fecha_vencimiento, date):
                contratos.dias_hasta_vto = str((contratos.fecha_vencimiento - date.today()).days) + " días"
            else:
                contratos.dias_hasta_vto = "---"

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
    
class IncidenciasContrato(models.Model):
    _name = 'incidencias.contrato'
    _description='Incidencias'

    fecha_incidencia=fields.Date(string='Fecha')
    motivo_incidencia=fields.Char(string="Motivo")
    resuelta=fields.Boolean(string="Resuelta")
    fecha_resolucion=fields.Date(string="Fecha Resol.")
    observacion_incidencia=fields.Texto(string="Observaciones")