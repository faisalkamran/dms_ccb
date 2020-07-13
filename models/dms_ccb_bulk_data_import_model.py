from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os
import base64
import requests

class LibraryRentWizard(models.TransientModel):
	_name = 'dms_ccb.bulk_data_import'
	start_barcode_number = fields.Char('Start Barcode Number', default='00000001')
	end_barcode_number = fields.Char('End Barcode Number', default='00000007')
	path_to_data_folder = fields.Char('Set Path to Bulk Data Folder', default='/home/odoo12dev/CCB Scanned Pages/Chaklala/')

	def bulk_data_import(self):
		for wizard_model in self:
			start_barcode_number_int = int(wizard_model.start_barcode_number)
			end_barcode_number_int = int(wizard_model.end_barcode_number)
			# count = 1
			for root, dirs, files in os.walk(wizard_model.path_to_data_folder):
				for filename in sorted(files):
					# print(filename)
					if filename != 'Thumbs.db':
						filename_barcode_int = int(filename[0:8])
						if filename_barcode_int >= start_barcode_number_int and filename_barcode_int <= end_barcode_number_int:
							filename_full_path = root + "/" + filename
							# print(count)
							print(filename_full_path)
							file = open(filename_full_path, "rb")
							file_data = file.read()
							test_id = self.env['ir.attachment'].create({
								'name': filename,
								# 'type': 'binary',
								'datas_fname': filename,
								'store_fname': filename,
								# 'mimetype': 'image/jpeg',
								'datas': base64.encodestring(file_data),
								# 'datas': file_data.encodestring('base64'),
								'res_model': 'dms_ccb.file',
								'res_id': filename_barcode_int,
							})
							# count = count + 1

	def check_files(self):
		for wizard_model in self:
			start_barcode_number_int = int(wizard_model.start_barcode_number)
			end_barcode_number_int = int(wizard_model.end_barcode_number)
			# count = 1
			check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt","w")
			for root, dirs, files in os.walk(wizard_model.path_to_data_folder):
				for filename in sorted(files):
					filename_length = len(filename)
					filename_full_path = root + "/" + filename
					# if filename_length == 16:
					# 	check_results_file.write(filename_full_path + " file check passed\n")
					check_results_file.write(filename + "\n")
					if filename != "Thumbs.db":
						if filename_length < 16:
							check_results_file.write(filename_full_path + " check failed.... shorter length\n")
						if filename_length > 16:
							check_results_file.write(filename_full_path + " check failed... longer length\n")

					# # print(filename)
					# if filename != 'Thumbs.db':
					# 	filename_barcode_int = int(filename[0:8])
					# 	if filename_barcode_int >= start_barcode_number_int and filename_barcode_int <= end_barcode_number_int:
					# 		filename_full_path = root + "/" + filename
					# 		# print(count)
					# 		print(filename_full_path)
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
					# 			'res_model': 'dms_ccb.file',
					# 			'res_id': filename_barcode_int,
					# 		})
					# 		# count = count + 1