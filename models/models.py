# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = "courses"
    _description = "Courses"
    name = fields.Char(string="Course Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    cost = fields.Float(string="Cost", required=True)
    teacher_id = fields.Many2one(
        "res.partner",
        string="Teacher",
        required=True,
    )
    enrollment_id = fields.One2many('enrollment', 'course_id', string="Enrollment")