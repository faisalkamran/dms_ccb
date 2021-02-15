from odoo import api, fields, models

class DmsFileCheckoutPopup(models.TransientModel):
	_name = 'dms_ccb.file_checkout_popup'
	_description = 'DMS File Checkout Popup Dialog'

	popup_file_assigned_to = fields.Many2one('hr.employee', string='File Assigned To?')
	checkout_file_message = fields.Char(string="Warning", default="File will be marked as Checked Out from File Store. Do you want to continue?", readonly="True")

	@api.multi
	def action_checkout_dms_file(self):
		active_model = self.env.context.get('active_model')
		active_id = self.env.context.get('active_id')
		active_form = self.env[active_model].search([('id','=',active_id)])
		# file_checkout_status = active_form.file_checkout_status
		# file_assigned_to = active_form.file_assigned_to
		active_form.file_checkout_status = True
		# active_form.file_assigned_to = popup_file_assigned_to

		# if file_checkout_status:
		# 	checkout_file_message = fields.Char(string="Warning", default="File will be marked as Checked In to File Store. Do you want to continue?", readonly="True")
		# else: