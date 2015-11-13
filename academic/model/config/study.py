from openerp import models, fields, api

class Study(models.Model):
    _name = "dtbs.academic.study"

    name          = fields.Char("Program Studi", size=50, required=True)
    faculty_id    = fields.Many2one("dtbs.academic.faculty", compute="faculty_list", string="Fakultas", readonly=False, required=True, autosave=False)
    department_id = fields.Many2one("dtbs.academic.department", String="Jurusan", required=True)

    @api.multi
    def onchange_faculty(self, faculty):
        if not faculty:
            return {"domain": {"department_id": []}}
        fcl = self.env["dtbs.academic.department"].search([("faculty_id", "ilike", faculty)])
        return {
            "domain": {"department_id": [("id", "in", fcl.ids)]},
            "value": {"department_id": None}
        }

    @api.one
    def faculty_list(self):
        self.faculty_id = self.department_id.faculty_id
