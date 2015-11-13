from openerp import models, fields, api
from openerp.exceptions import ValidationError

class Classroom(models.Model):
    _name = "dtbs.academic.classroom"

    name          = fields.Char("Kode", size=50, required=True)
    desc          = fields.Char("Nama", size=100)
    dosen_id      = fields.Many2one("hr.employee", "Dosen Wali", required=True, domain=['is_teacher', '=', True])
    kuota         = fields.Integer("Kuota", required=True)
    tahun_id      = fields.Many2one("dtbs.academic.acyear", "Tahun Akademik", required=True)
    faculty_id    = fields.Many2one("dtbs.academic.faculty", "Fakultas", required=True)
    department_id = fields.Many2one("dtbs.academic.department", "Jurusan", required=True)
    study_id      = fields.Many2one("dtbs.academic.study", "Program Studi", required=True)
 

    @api.constrains("kuota")
    def _classroom_const(self, cr, uid, ids, context=None):
        new_list2 = []
        for obj in self.browse(cr, uid, ids, context=context):
            if obj.kuota <=0:
                raise ValidationError("Periksa kembali kuota !")
                  
  
    @api.multi
    def onchange_faculty(self, faculty):
        if not faculty:
            return {"domain": {"department_id": []}}

        dpt = self.env['dtbs.academic.department'].search([("faculty_id", "ilike", faculty)])
        return {
            "domain": {"department_id": [("id", "in", dpt.ids)]},
            "value": {"department_id": None}
        }

    @api.multi
    def onchange_department(self, department):
        if not department:
            return {"domain": {"study_id": []}}

        std = self.env['dtbs.academic.study'].search([("department_id", "ilike", department)])
        return {
            "domain": {"study_id": [("id", "in", std.ids)]},
            "value": {"study_id": None}
        }

