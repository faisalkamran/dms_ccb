from odoo import models, fields, api, _

class dms_ccb_file_record_type(models.Model):
	_name = 'dms_ccb.file_record_type'
	_description = 'DMS CCB File Record Type'
	_rec_name = 'file_record_type'
	file_record_type = fields.Char('Name')
	file_record_type_description = fields.Char('Description')

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

class dms_ccb_file_type_of_land(models.Model):
	_name = 'dms_ccb.file_type_of_land'
	_description = 'DMS CCB File Type of Land'
	_rec_name = 'file_type_of_land'
	file_type_of_land = fields.Char('Name')
	file_type_of_land_description = fields.Char('Description')

class dms_ccb_file_purpose(models.Model):
	_name = 'dms_ccb.file_purpose'
	_description = 'DMS CCB File Purpose'
	_rec_name = 'file_purpose'
	file_purpose = fields.Char('Name')
	file_purpose_description = fields.Char('Description')

class dms_ccb_file_branch(models.Model):
	_name = 'dms_ccb.file_branch'
	_description = 'DMS CCB File Branch'
	_rec_name = 'file_branch'
	file_branch = fields.Char('Name')
	file_branch_description = fields.Char('Description')

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
	file_subject = fields.Text('File Subject',required=True, track_visibility="always") 

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
	file_remarks = fields.Html('Remarks')
	file_attributes = fields.Many2many('dms_ccb.file_attribute', string='Attributes')
	state = fields.Selection([('draft','Draft'),
							('qc_review', 'QC Review'),
							('rejected', 'Rejected'),
							('approved', 'Approved'),],
							string="QC Status",
							readonly=True,default='draft')
	is_public = fields.Boolean(default=False)
	file_address = fields.Text('Address', track_visibility="always")
	file_plot_khasra_cb_no = fields.Char('Plot No / CB No / Khasra No', track_visibility="always")
	file_record_id = fields.Char('Record ID', track_visibility="always")
	
	# file_attachments = fields.Many2many('ir.attachment', string='File Attachments')
	# message_attachment_count = fields.Integer(readonly=False, track_visibility="onchange")

	def file_for_review_state(self):
		for rec in self:
			rec.state = 'qc_review'

	def file_for_approved_state(self):
		for rec in self:
			rec.state = 'approved'

	def file_for_rejected_state(self):
		for rec in self:
			rec.state = 'rejected'

	def mlc_erp_api_call(self):
		return 0

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

class dms_ccb_page_rejection_reasons(models.Model):
	_name = 'dms_ccb.page_rej_reasons'
	_description = 'DMS CCB Page Rejection Reasons'
	_rec_name = 'rej_reason_name'
	rej_reason_name = fields.Char('Rejection Reason')
	rej_reason_description = fields.Char('Description')

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
