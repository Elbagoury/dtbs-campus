from openerp import models, fields, api

class Education(models.Model):
    _name = "dtbs.academic.education"

    name    = fields.Char("Nama Sekolah", size=50, required=True)
    tingkat = fields.Selection([("sd","SD"),("sltp","SLTP"),("slta","SLTA"),("d1","Diploma 1"),("d2","Diploma 2"),("d3","Diploma 3"), ("s1","Sarjana"), ("s2","Magister"), ("s3","Doktor"), ("s4","Spesialis")], "Tingkat")
    thnm    = fields.Integer("Tahun Masuk")
    thnl    = fields.Integer("Tahun Lulus")
    nilai   = fields.Float("Nilai Akhir")
    partner_id = fields.Many2one("res.partner", "Siswa")
