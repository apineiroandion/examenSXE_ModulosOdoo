# -*- coding: utf-8 -*-

from odoo import models, fields, api


class examen_sxe__angel(models.Model):
    _name = 'examen_sxe__angel.examen_sxe__angel'
    _description = 'examen_sxe__angel.examen_sxe__angel'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    proyecto = fields.Text(string="Proyecto")
    tutor = fields.Selection(
        [
            ("diego_alonso", "Diego Alonso"),
            ("manuel_guimarei", "Manuel Guimarei"),
            ("manuel_araujo", "Manuel Araujo"),
            ("damian_nogueiras", "Damian Nogueiras"),
            ("sin_tutor", "Sin tutor"),
        ],
        string="Tutor",
        default="sin_tutor",
    )
    horas_dia = fields.Integer(string="Horas al día")
    horas_mes = fields.Integer(string="Horas al mes") #, compute="_calcular_horas_mes")

    #@api.depends(horas_dia)
    #def _calcular_horas_mes(self):
        #for record in self:
            #record.horas_mes = record.horas_dia * 30

