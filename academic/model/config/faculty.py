from openerp import models, fields, api

class Faculty(models.Model):
    _name = "dtbs.academic.faculty"

    name = fields.Char("Fakultas", size=50, required=True)
