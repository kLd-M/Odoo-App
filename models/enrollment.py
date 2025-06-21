from odoo import models, fields

class Enrollment(models.Model):
    _name = 'enrollment'
    _description = 'Enrollment'

    name = fields.Char(string="Name", required=True)
    student_id = fields.Many2one('student', string='Student', required=True)
    course_id = fields.Many2one('courses', string='Course', required=True)
    date = fields.Date(string='Enrollment Date', required=True)
    cost = fields.Float(string='Cost', related='course_id.cost', store=True)
