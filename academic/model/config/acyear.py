from openerp import models, fields, api
from datetime import datetime

class Acyear(models.Model):
    _name = "dtbs.academic.acyear"

    current_date = datetime.today()
    ta = current_date.year

    name  = fields.Char("Kode", size=20, required=True)
    tahun = fields.Integer("Tahun Akademik", default=ta)
    desc  = fields.Text("Keterangan")
