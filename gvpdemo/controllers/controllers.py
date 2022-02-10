from odoo import http

 # class student(http.Controller):
 # 	@http.route('/gvpdemo/student/', auth='public')
 # 	def index(self,**kw):
 # 		return "hello odoo"

class Academy(http.Controller):

     @http.route('/my',type="http", auth='user',website=True)
     def index(self, **kwargs):
         return http.request.render('gvpdemo.home')
         
         