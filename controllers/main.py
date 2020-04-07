from odoo import http

class dms_files(http.Controller):
	@http.route('/dms/files',auth='user')
	def list(self, **kwargs):
		dms_file = http.request.env['dms.file']
		dms_files = dms_file.search([])
		return http.request.render('dms.file_list_template', {'dms_files': dms_files})
