from openerp import fields, models, api

class Teacher(models.Model):
    _inherit = 'hr.employee'

    is_teacher  = fields.Boolean("Dosen", default=0)


