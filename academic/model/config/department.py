from openerp import models, fields, api

class Department(models.Model):
    _name = "dtbs.academic.department"

    name       = fields.Char("Jurusan", size=50, required=True)
    faculty_id = fields.Many2one("dtbs.academic.faculty",string="Fakultas", required=True)
