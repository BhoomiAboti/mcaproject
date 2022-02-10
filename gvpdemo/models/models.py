from odoo import models,fields,api

class gvpdemo(models.Model):
	_name = 'tbl.student'

	stname=fields.Char()

class teachers(models.Model):
	_name = 'academy.teachers'

	name = fields.Char()
		