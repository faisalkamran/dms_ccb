from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os
import base64
import requests

class dms_ccb_file_record_type(models.Model):
	_name = 'dms_ccb.file_record_type'
	_description = 'DMS CCB File Record Type'
	_rec_name = 'file_record_type'
	file_record_type = fields.Char('Name')
	file_record_type_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['file_record_type', 'file_record_type_description']
		res = super(dms_ccb_file_record_type, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

# class dms_ccb_file_area(models.Model):
# 	_name = 'dms_ccb.file_area'
# 	_description = 'DMS CCB File Area'
# 	_rec_name = 'file_area'
# 	file_area = fields.Char('Name')
# 	file_area_description = fields.Char('Description')

class dms_ccb_file_colony(models.Model):
	_name = 'dms_ccb.file_colony'
	_description = 'DMS CCB File Colony'
	_rec_name = 'file_colony'
	file_colony = fields.Char('Name')
	file_colony_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['file_colony', 'file_colony_description']
		res = super(dms_ccb_file_colony, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_file_type_of_land(models.Model):
	_name = 'dms_ccb.file_type_of_land'
	_description = 'DMS CCB File Type of Land'
	_rec_name = 'file_type_of_land'
	file_type_of_land = fields.Char('Name')
	file_type_of_land_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['file_type_of_land', 'file_type_of_land_description']
		res = super(dms_ccb_file_type_of_land, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_file_purpose(models.Model):
	_name = 'dms_ccb.file_purpose'
	_description = 'DMS CCB File Purpose'
	_rec_name = 'file_purpose'
	file_purpose = fields.Char('Name')
	file_purpose_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['file_purpose', 'file_purpose_description']
		res = super(dms_ccb_file_purpose, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_file_branch(models.Model):
	_name = 'dms_ccb.file_branch'
	_description = 'DMS CCB File Branch'
	_rec_name = 'file_branch'
	file_branch = fields.Char('Name')
	file_branch_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['file_branch', 'file_branch_description']
		res = super(dms_ccb_file_branch, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_file_attribute(models.Model):
	_name = 'dms_ccb.file_attribute'
	_description = 'DMS CCB File Attribute'
	_rec_name = 'file_attribute'
	file_attribute = fields.Char('Name')
	file_attribute_description = fields.Char('Description')

class dms_ccb_file(models.Model):
	_name = 'dms_ccb.file'
	_inherit = ['mail.thread','mail.activity.mixin']
	_description = 'DMS CCB File'
	_rec_name = 'file_no'
	file_no = fields.Char('File No.', required=True, track_visibility="always")
	file_subject = fields.Text('File Subject', track_visibility="always") 
	# file_subject = fields.Text('File Subject',required=True, track_visibility="always") 

	# file_barcode = fields.Char('Barcode')
	file_barcode = fields.Char(string='Barcode', required=True, copy=False,
							readonly=True, index= True, default=lambda self: _('New'))

	file_record_type = fields.Many2one('dms_ccb.file_record_type', string='Record Type', track_visibility="always")
	# file_area = fields.Many2one('dms_ccb.file_area', string='Area', track_visibility="always")
	file_colony = fields.Many2one('dms_ccb.file_colony', string='Colony', track_visibility="always")
	file_type_of_land = fields.Many2one('dms_ccb.file_type_of_land', string='Type of Land', track_visibility="always")
	file_purpose = fields.Many2one('dms_ccb.file_purpose', string='Purpose', track_visibility="always")
	file_branch = fields.Many2one('dms_ccb.file_branch', string='Branch', track_visibility="always")
	# file_remarks = fields.Text('Remarks')
	file_remarks = fields.Html('Remarks') # track_visibility does not work on html fields
	file_attributes = fields.Many2many('dms_ccb.file_attribute', string='Attributes')
	state = fields.Selection([('file_received','File Received'),
							('draft','Draft'),
							('scan_complete','Scanning Complete'),
							('qc_review', 'QC Review'),
							('file_unlock', 'File Unlocked'),
							('for_approval','For Approval'),
							('rejected', 'Rejected'),
							('approved', 'Approved'),],
							string="QC Status",
							readonly=True,default='file_received',
							track_visibility='always')
	is_public = fields.Boolean(default=False)
	file_address = fields.Text('Address', track_visibility="always")
	file_plot_khasra_cb_no = fields.Char('Plot No / CB No / Khasra No', track_visibility="always")
	# file_record_id = fields.Char('Record ID', track_visibility="always")
	file_record_id = fields.Many2one('dms_ccb.erp_integration_data', string='Record ID', track_visibility="always")
	
	# file_attachments = fields.Many2many('ir.attachment', string='File Attachments')
	# message_attachment_count = fields.Integer(readonly=False, track_visibility="onchange")

	def file_for_approval_state(self):
		for rec in self:
			rec.state = 'for_approval'

	def file_for_approved_state(self):
		for rec in self:
			rec.state = 'approved'

	def file_for_rejected_state(self):
		for rec in self:
			rec.state = 'rejected'

	def file_back_to_qc_review_state(self):
		for rec in self:
			rec.state = 'qc_review'

	def file_to_unlock_state(self):
		for rec in self:
			rec.state = 'file_unlock'

	def mlc_erp_api_call(self):
		return 0

	@api.multi
	def dms_ccb_change_workflow_state(self):
		flag = self.env['res.users'].has_group('dms_ccb.dms_ccb_qc_workflow_group')
		# count = 1
		# for root, dirs, files in os.walk("/home/odoo12dev/CCB Scanned Pages/Chaklala/"):
		# 	# print(root)
		# 	# print(sorted(dirs))
		# 	# print(sorted(files))
		# 	for filename in sorted(files):
		# 		# filename_full_path = "/home/odoo12dev/CCB Scanned Pages/Chaklala/" + filename
		# 		filename_full_path = root + "/" + filename
		# 		# print(filename)
		# 		print(filename_full_path)
		# 		print(count)
		# 		file = open(filename_full_path, "rb")
		# 		file_data = file.read()
		# 		test_id = self.env['ir.attachment'].create({
		# 			'name': filename,
		# 			# 'type': 'binary',
		# 			'datas_fname': filename,
		# 			'store_fname': filename,
		# 			# 'mimetype': 'image/jpeg',
		# 			'datas': base64.encodestring(file_data),
		# 			# 'datas': file_data.encodestring('base64'),
		# 		})
		# 		count = count + 1
		if flag:
			for rec in self:
				if rec.state == 'file_received':
					rec.state = 'draft'
					break
				if rec.state == 'draft':
					rec.state = 'scan_complete'
					break
				if rec.state == 'scan_complete':
					rec.state = 'qc_review'
					break
				# if rec.state == 'qc_review':
				# 	rec.state = 'draft'
				# 	break
				# if rec.state == 'approved':
				# 	rec.state = 'draft'
				# 	break
		else:
			raise UserError('User is not a member of the QC Workflow Access Group.')

	@api.model
	def create(self, vals):
		if vals.get('file_barcode', _('New')) == _('New'):
			vals['file_barcode'] = self.env['ir.sequence'].next_by_code('dms.ccb.file.barcode.sequence') or _('New')
		result = super(dms_ccb_file, self).create(vals)
		return result

	def dms_manage_pages(self):
		return {
			'name': 'Manage Pages',
			'domain': ['&',('res_id','=',self.id),('res_model','=','dms_ccb.file')],			
			# 'view_type': 'form',
			'res_model': 'ir.attachment',
			'view_id': False,
			'view_mode': 'list,kanban,form',
			'type': 'ir.actions.act_window',
			'target': 'current',
			'context': "{'dms_ccb_key': False, 'dms_meo_key': True}",
		}	

class dms_ccb_page_tags(models.Model):
	_name = 'dms_ccb.page_tags'
	_description = 'DMS CCB Page Tags'
	_rec_name = 'tag_name'
	tag_name = fields.Char('Tag Name')
	tag_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['tag_name', 'tag_description']
		res = super(dms_ccb_page_tags, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_page_rejection_reasons(models.Model):
	_name = 'dms_ccb.page_rej_reasons'
	_description = 'DMS CCB Page Rejection Reasons'
	_rec_name = 'rej_reason_name'
	rej_reason_name = fields.Char('Rejection Reason')
	rej_reason_description = fields.Char('Description')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['rej_reason_name', 'rej_reason_description']
		res = super(dms_ccb_page_rejection_reasons, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class dms_ccb_erp_integration_data(models.Model):
	_name = 'dms_ccb.erp_integration_data'
	_description = 'DMS CCB Integration Data with ML&C ERP'
	_rec_name = 'ccb_erp_id'
	ccb_erp_id = fields.Char('ML&C ERP ID')
	ccb_erp_type = fields.Char('Type')
	ccb_erp_link_id = fields.Char('Link ID')
	ccb_erp_office_id = fields.Char('Office ID')
	ccb_erp_name = fields.Char('Name')
	ccb_erp_address = fields.Char('Address')

	def fields_get(self, allfields=None, attributes=None):
		# selectable_fields_to_hide = ['create_uid', 'create_date', 'id', 'write_date', 'write_uid']
		selectable_fields_to_hide = ['id']
		sortable_fields_to_hide = ['ccb_erp_address', 'ccb_erp_name', 'ccb_erp_id']
		res = super(dms_ccb_erp_integration_data, self).fields_get(allfields=allfields, attributes=attributes)
		for field in selectable_fields_to_hide:
			res[field]['selectable'] = False
			# res[field]['searchable'] = False
		for field in sortable_fields_to_hide:
			res[field]['sortable'] = False
		return res

class Attachment_Extension(models.Model):
	_inherit = ['ir.attachment']

	# the following two fields are independent of office location
	dms_page_date = fields.Date(string='Document Date')
	dms_page_status = fields.Selection([('approved','Approved'),('rejected', 'Rejected')],string="Approval Status")
	
	# the following fields are dependent on office location therefore need re-declaration on opening of new office location
	dms_ccb_page_tags = fields.Many2many('dms_ccb.page_tags', string='Page Tags')
	dms_ccb_page_rej_reasons = fields.Many2many('dms_ccb.page_rej_reasons', string='Rejection Reasons', readonly="True")
	
	# dms_page_tags = fields.Char('Page Tags')
	# attachment_image_preview = fields.Binary('Preview')
	# attachment_image_preview = fields.Binary(string='Image Preview', default='thumbnail')
	# attachment_image_preview = fields.Binary(string='Image Preview')
