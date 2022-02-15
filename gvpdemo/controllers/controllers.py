from odoo import http

 

class gvpdata(http.Controller):

     @http.route('/home',type="http", auth='public',website=True)
     def home_page(self, **kwargs):
         return http.request.render('gvpdemo.home')
         
     # ***************About us***************

     @http.route('/about/history',type="http", auth='public',website=True)
     def hostory_page(self, **kwargs):
         return http.request.render('gvpdemo.history')


     @http.route('/about/establishment',type="http", auth='public',website=True)
     def establishment_page(self, **kwargs):
         return http.request.render('gvpdemo.establishment')
         
        
     @http.route('/about/values',type="http", auth='public',website=True)
     def values_page(self, **kwargs):
         return http.request.render('gvpdemo.values')
         

     @http.route('/about/emblem',type="http", auth='public',website=True)
     def emblem_page(self, **kwargs):
         return http.request.render('gvpdemo.emblem')

     @http.route('/about/song',type="http", auth='public',website=True)
     def song_page(self, **kwargs):
         return http.request.render('gvpdemo.song')
         
    
     @http.route('/about/salientsfeatures',type="http", auth='public',website=True)
     def salients_page(self, **kwargs):
         return http.request.render('gvpdemo.salientsfeatures')
         
     @http.route('/about/objective',type="http", auth='public',website=True)
     def objective_page(self, **kwargs):
         return http.request.render('gvpdemo.objective')

     @http.route('/about/mission',type="http", auth='public',website=True)
     def mission_page(self, **kwargs):
         return http.request.render('gvpdemo.mission')

     @http.route('/about/gvpact',type="http", auth='public',website=True)
     def gvpact_page(self, **kwargs):
         return http.request.render('gvpdemo.gvpact')

        #*************Administration*********************

     @http.route('/administration/chancellors',type="http", auth='public',website=True)
     def chancellor_page(self, **kwargs):
         return http.request.render('gvpdemo.chancellors')

     @http.route('/administration/vicechancellors',type="http", auth='public',website=True)
     def vicechancellor_page(self, **kwargs):
         return http.request.render('gvpdemo.vicechancellors')

     @http.route('/administration/registrar',type="http", auth='public',website=True)
     def registrar_page(self, **kwargs):
         return http.request.render('gvpdemo.registrar')

    #*****************Academics***************************

     @http.route('/academics/language',type="http", auth='public',website=True)
     def language_page(self, **kwargs):
         return http.request.render('gvpdemo.language')


     @http.route('/academics/social1',type="http", auth='public',website=True)
     def social_page(self, **kwargs):
         return http.request.render('gvpdemo.social1')

     @http.route('/academics/education',type="http", auth='public',website=True)
     def education_page(self, **kwargs):
         return http.request.render('gvpdemo.education')

     @http.route('/academics/managment',type="http", auth='public',website=True)
     def managment_page(self, **kwargs):
         return http.request.render('gvpdemo.managment')

     @http.route('/academics/hindi',type="http", auth='public',website=True)
     def hindi_page(self, **kwargs):
         return http.request.render('gvpdemo.hindi')


     @http.route('/academics/english',type="http", auth='public',website=True)
     def english_page(self, **kwargs):
         return http.request.render('gvpdemo.english')

     @http.route('/academics/anthropology',type="http", auth='public',website=True)
     def anthropology_page(self, **kwargs):
         return http.request.render('gvpdemo.anthropology')

     @http.route('/academics/rural',type="http", auth='public',website=True)
     def rural_page(self, **kwargs):
         return http.request.render('gvpdemo.rural')

     @http.route('/academics/IASE',type="http", auth='public',website=True)
     def IASE_page(self, **kwargs):
         return http.request.render('gvpdemo.IASE')

     @http.route('/academics/biology',type="http", auth='public',website=True)
     def biology_page(self, **kwargs):
         return http.request.render('gvpdemo.biology')



