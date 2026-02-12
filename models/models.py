# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_tareas(models.Model):
    _name = 'lista_tareas.tareas'
    _description = 'Lista de tareas'

    tarea = fields.Char(string="Nombre de la tarea", required=True)
    
    # CAMBIO 1: Convertimos el número en un desplegable (Selection)
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('critica', 'Crítica')
    ], string='Prioridad', default='baja')

    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    # CAMBIO 2: Actualizamos la lógica para detectar los nuevos niveles
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            # Si la prioridad es Alta o Crítica, se marca como urgente
            if record.prioridad in ('alta', 'critica'):
                record.urgente = True
            else:
                record.urgente = False