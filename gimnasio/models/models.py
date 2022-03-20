# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clase(models.Model):
    _name = 'gimnasio.clase'
    _description = 'Clase'
    name = fields.Char('Nombre', required=True, index=True)
    descripcion = fields.Text('Descripción')
    hora_inicio = fields.Datetime('Hora inicio', required=True)
    hora_fin = fields.Datetime('Hora fin', required=True)
    duracion = fields.Integer('Duración(min)', compute='_compute_duracion')
    dificultad = fields.Selection([
        ('facil','Fácil'),
        ('media','Media'),
        ('dificil','Dificil')
    ], string='Dificultad', default='facil', required=True)
    monitor = fields.Many2one('gimnasio.monitor', string='Monitor')
    alumnos = fields.Many2many('gimnasio.alumno', string='Alumnos')
    
    @api.depends('duracion')
    def _compute_duracion(self):
        for clase in self.filtered('hora_fin'):
            if clase.hora_fin:
                delta = clase.hora_fin - clase.hora_inicio
                seconds = delta.seconds
                clase.duracion = seconds/60
            else:
                clase.duracion = 0




class Monitor(models.Model):
    _name = 'gimnasio.monitor'
    _description = 'Monitor'
    _inherits = {'res.partner' : 'partner_id'}

    #fields específicos del modelo
    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    fecha_inicio = fields.Date('Fecha de inicio', required=True)
    fecha_fin = fields.Date('Fecha de fin')
    numero_miembro = fields.Char('Número de miembro', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')

    _sql_constraints = [
        ('uniq_name', 'unique(numero_miembro)', "Ya existe un miembro con ese número. ¡Debe ser único!"),
    ]


class Alumno(models.Model):
    _name = 'gimnasio.alumno'
    _description = 'Alumno'
    _inherits = {'res.partner' : 'partner_id'}

    #fields específicos del modelo
    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    fecha_inicio = fields.Date('Fecha de inicio', required=True)
    antiguedad = fields.Integer(string='Antigüedad', compute='_compute_antiguedad')
    numero_miembro = fields.Char('Número de miembro', required=True)

    _sql_constraints = [
        ('uniq_name', 'unique(numero_miembro)', "Ya existe un miembro con ese número. ¡Debe ser único!"),
    ]

    @api.depends('antiguedad')
    def _compute_antiguedad(self):
        today = fields.Date.today()
        for alumno in self.filtered('fecha_inicio'):
            if alumno.fecha_inicio:
                delta = today - alumno.fecha_inicio
                alumno.antiguedad = delta.days
            else:
                alumno.antiguedad = 0