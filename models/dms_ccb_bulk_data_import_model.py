from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os
import base64
import requests
import csv

class LibraryRentWizard(models.TransientModel):
	_name = 'dms_ccb.bulk_data_import'
	start_barcode_number = fields.Char('Start Barcode Number', default='00000002')
	end_barcode_number = fields.Char('End Barcode Number', default='00000010')
	path_to_data_folder = fields.Char('Set Path to Bulk Data Folder', default='/media/odoo12dev/1TB External/data')

	def bulk_data_import(self):
		for wizard_model in self:
			start_barcode_number_int = int(wizard_model.start_barcode_number)
			end_barcode_number_int = int(wizard_model.end_barcode_number)
			count = 1

			for root, dirs, files in os.walk(wizard_model.path_to_data_folder):
				for filename in sorted(files):

					if filename != 'Thumbs.db':
						current_barcode_int = int(root[-8:])

						if current_barcode_int >= start_barcode_number_int and current_barcode_int <= end_barcode_number_int:
							filename_full_path = root + "/" + filename
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
								'res_id': current_barcode_int,
							})
							print(filename_full_path)
							print(count)
							count = count + 1

	def check_files(self):
		for wizard_model in self:
			start_barcode_number_int = int(wizard_model.start_barcode_number)
			end_barcode_number_int = int(wizard_model.end_barcode_number)
			filename_extension_set = set(())
			check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt","w")

			for root, dirs, files in os.walk(wizard_model.path_to_data_folder):

				# check folder names for correct format of barcodes
				for foldername in sorted(dirs):
					foldername_length = len(foldername)
					if foldername_length < 8 or foldername_length > 8:
						check_results_file.write("Folder name length incorrect for.... " + foldername + "\n")

				for filename in sorted(files):
					# this loop should run between start barcode number & end barcode number
					current_barcode_int = int(root[-8:])
					if current_barcode_int >= start_barcode_number_int and current_barcode_int <= end_barcode_number_int:

						# collect unique filename extensions in a set
						filename_extension_set.add(filename[-4:])

						# check filenames for correct length... required length is 16
						filename_length = len(filename)
						filename_full_path = root + "/" + filename
						# if filename != "Thumbs.db":
						# if filename_length == 16: check_results_file.write(filename_full_path + " file check passed\n")
						if filename_length < 16: check_results_file.write("check failed. shorter length. " + filename_full_path + "\n")
						if filename_length > 16: check_results_file.write("check failed. longer length. " + filename_full_path + "\n")

						# record all TIFF or TIF format images to the check results file
						if filename[-4:] == ".tif":	check_results_file.write(filename_full_path + "\n")
						if filename[-4:] == "tiff":	check_results_file.write(filename_full_path + "\n")

			# write unique filename extensions to check results file
			for filename_extension in sorted(filename_extension_set):
				check_results_file.write(filename_extension + "\n")
				# print(list(filename_extension))

	def check_csv_file(self):
		check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt","w")
		with open('/home/odoo12dev/Desktop/pages_data_dump.csv', mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file)
			line_count = 0
			for row in csv_reader:
				if line_count > 0:
					file_barcode_number = row["Bar-Code"]
					file_barcode_number_length = len(file_barcode_number)
					if file_barcode_number_length > 8: check_results_file.write("File barcode length greater than 8\n")
					if file_barcode_number_length < 8: check_results_file.write("File barcode length less than 8\n")
					filename = row["FILENAME"]
					filename_length = len(filename)
					if filename_length != 16:
						if filename_length > 16: check_results_file.write(filename + " Filename length greater than 16\n")
						if filename_length < 16: check_results_file.write(filename + " Filename length less than 16\n")
				line_count += 1
			print(f'Processed {line_count} lines.')