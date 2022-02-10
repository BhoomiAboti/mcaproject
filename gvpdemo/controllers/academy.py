from odoo import http

class academy(http.Controller):
	@http.route('/gvpdemo/student1/', auth='public')

	def fstpage(self,**kw):
		return http.request.render('gvpdemo.index',{
		'teachers': ["ajaybhai parikh","Dhirenbhai patel","sanjaybhai nalvaya"],
		})