from openerp import fields, models, api
from datetime import datetime
from dateutil import parser
from openerp.exceptions import ValidationError

class Student(models.Model):
    _inherit = 'res.partner'

    #noform        = fields.Char("No Formulir", size=50, required=True)
    #tgluji        = fields.Date("Tgl. Ujian")
    #nilai         = fields.Float("Nilai")
    #tptlhr        = fields.Char("Tempat Lahir", size=50)
    #tgllhr        = fields.Date("Tgl. Lahir")
    #usia          = fields.Integer("Usia")
    #gender        = fields.Selection([("lelaki","Laki-laki"),("perempuan","Perempuan")], "Jenis Kelamin")
    #stsnkh        = fields.Selection([("nikah","Menikah"),("single","Belum Menikah"),("single2","Duda/Janda")], "Status Pernikahan")
    #agama_id      = fields.Many2one("dtbs.academic.religion", string="Agama")
    #faculty_id    = fields.Many2one("dtbs.academic.faculty", string="Fakultas", required=True)
    #department_id = fields.Many2one("dtbs.academic.department", string="Jurusan", required=True)
    #study_id      = fields.Many2one("dtbs.academic.study", string="Program Studi", required=True)
    #tgldft        = fields.Date("Tgl. Daftar")
    #kelas         = fields.Char("Kelas", size=20)
    #tahun         = fields.Many2one("dtbs.academic.acyear", string="Tahun Akademik", required=True)
    #education_ids = fields.One2many("dtbs.academic.education", "partner_id", copy=True)
    #is_registran  = fields.Boolean("Pendaftar", default=0)
    #sts_academic  = fields.Selection([("calon", "Calon"), ("siswa", "Siswa"), ("alumni", "Alumni")], "Status Akademik", default="calon")



    #@api.onchange('tgllhr')
    #def _compute_usia(self):
    #    try:
    #        current_date = datetime.now()
    #        current_year = current_date.year
    #        birth_date = parser.parse(self.tgllhr)
    #        current_age = current_year-birth_date.year
    #        self.usia = current_age
    #    except:
    #        self.usia = 0

    #@api.multi
    #def onchange_faculty(self, faculty):
    #    if not faculty:
    #        return {"domain": {"department_id": []}}

    #    dpt = self.env['dtbs.academic.department'].search([("faculty_id", "ilike", faculty)])
    #    return {
    #        "domain": {"department_id": [("id", "in", dpt.ids)]},
    #        "value": {"department_id": None}
    #    }

    #@api.multi
    #def onchange_department(self, department):
    #    if not department:
    #        return {"domain": {"study_id": []}}

    #    std = self.env['dtbs.academic.study'].search([("department_id", "ilike", department)])
    #    return {
    #        "domain": {"study_id": [("id", "in", std.ids)]},
    #        "value": {"study_id": None}
    #    }

    #@api.model
    #def create(self, vals):
    #    raise ValidationError("Tidak bisa menambah data dari form ini.")
