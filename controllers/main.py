from odoo import http

class dms_files(http.Controller):
	@http.route('/dms/files',auth='public', website=True)
	def list(self, **kwargs):
		# dms_file = http.request.env['dms.file']
		# dms_files = dms_file.search([])
		# if 'id' in kwargs:
			# print(kwargs['id'])
		# print(kwargs)
		all_pages = []
		if 'revenue_id' in kwargs.keys():
			file_revenue_id = kwargs['revenue_id']
			dms_files = http.request.env['dms_ccb.file'].sudo().search([('file_revenue_id','=',file_revenue_id)])
			for dms_file in dms_files:
				search_pages = http.request.env['ir.attachment'].sudo().search(['&',('res_id','=',dms_file.id),('res_model','=','dms_ccb.file')])
				all_pages.append(search_pages)
				# print(all_pages)
				# print(search_pages)
		return http.request.render('dms_ccb.file_list_template', {'dms_files': dms_files, 'all_pages': all_pages})
