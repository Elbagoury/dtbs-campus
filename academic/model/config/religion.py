from openerp import models, fields, api

class Religion(models.Model):
    _name = "dtbs.academic.religion"

    name = fields.Char("Agama", size=50, required=True)
