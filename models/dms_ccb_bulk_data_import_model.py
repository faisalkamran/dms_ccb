from odoo import models, fields, api, _
from odoo.exceptions import UserError
import os
import base64
import requests
import csv


class LibraryRentWizard(models.TransientModel):
    _name = 'dms_ccb.bulk_data_import'
    start_barcode_number = fields.Char('Start Barcode Number', default='10000001')
    end_barcode_number = fields.Char('End Barcode Number', default='10021069')
    path_to_data_folder = fields.Char('Set Path to Bulk Data Folder', default='/media/odoo12dev/My Passport/CCB-Revenue/')

    def display_attachment_content(self):
        attachment_obj_search_domain = [('name', '=', '20002012_001.jpg'), ('res_id', '=', 3)]
        attachment_object = self.env['ir.attachment'].search(attachment_obj_search_domain)
        print("******************************************************************************")
        print("*********                                                            *********")
        print("")
        print("datas  " + str(attachment_object.datas))
        print("datas_fname  " + str(attachment_object.datas_fname))
        print("db_datas  " + str(attachment_object.db_datas))
        print("description  " + str(attachment_object.description))
        print("display_name  " + str(attachment_object.display_name))
        print("file_size  " + str(attachment_object.file_size))
        print("id  " + str(attachment_object.id))
        print("index_content  " + str(attachment_object.index_content))
        print("local_url  " + str(attachment_object.local_url))
        print("mimetype  " + str(attachment_object.mimetype))
        print("name  " + str(attachment_object.name))
        print("store_fname  " + str(attachment_object.store_fname))
        print("url  " + str(attachment_object.url))
        print("")
        print("*********                                                            *********")
        print("******************************************************************************")

    def bulk_data_import(self):
        # model.power_on()
        for wizard_model in self:
            start_barcode_number_int = int(wizard_model.start_barcode_number)
            end_barcode_number_int = int(wizard_model.end_barcode_number)
            count = 1

            # # this code is to fix the faulty barcode numbers in the MEO files
            # for x in range(9434):
            # 	y = x + 1
            # 	meo_file_obj_search_domain = [('id', '=', y)]
            # 	meo_file_obj = self.env['dms_meo.file'].search(meo_file_obj_search_domain)
            # 	meo_file_obj.file_barcode = str(y + 20000000)
            # 	print(meo_file_obj.file_no)

            for root, dirs, files in os.walk(wizard_model.path_to_data_folder):
                for filename in sorted(files):

                    if filename != 'Thumbs.db':
                        current_barcode_int = int(root[-8:])
                        if current_barcode_int >= start_barcode_number_int and current_barcode_int <= end_barcode_number_int:
                            # meo_barcode_int = current_barcode_int - 20000000
                            meo_barcode_int = current_barcode_int - 9987192
                            filename_full_path = root + "/" + filename
                            file = open(filename_full_path, "rb")
                            file_data = file.read()
                            # print(filename_full_path)
                            try:
                                # encoded_file_data = base64.encodestring(file_data)
                                encoded_file_data = base64.b64encode(file_data)
                                test_id = self.env['ir.attachment'].create({
                                    'name': filename,
                                    # 'type': 'binary',
                                    'datas_fname': filename,
                                    'store_fname': filename,
                                    # 'mimetype': 'image/jpeg',
                                    # 'datas': base64.encodestring(file_data),
                                    'datas': encoded_file_data,
                                    'res_model': 'dms_ccb.file',
                                    'res_id': meo_barcode_int,
                                    # 'res_id': current_barcode_int,
                                })
                            except:
                                print("An unknown error occured")
                            print(filename_full_path)
                            print(count)
                            count = count + 1

    def check_files(self):
        for wizard_model in self:
            start_barcode_number_int = int(wizard_model.start_barcode_number)
            end_barcode_number_int = int(wizard_model.end_barcode_number)
            filename_extension_set = set(())
            dir_path_set = set(())
            check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt", "w")
            # count = 1

            for root, dirs, files in os.walk(wizard_model.path_to_data_folder):

                # check folder names for correct format of barcodes
                for foldername in sorted(dirs):
                    foldername_length = len(foldername)
                    if foldername_length < 8 or foldername_length > 8:
                        check_results_file.write("Folder name length incorrect for.... " + foldername + "\n")

                for filename in sorted(files):
                    # add unique path to set
                    dir_path_set.add(root)
                    current_barcode = root[-8:]
                    if not current_barcode.isdigit():
                    	check_results_file.write("int conversion failed for... " + current_barcode + "\n")
                    	check_results_file.write(root + " \n")
                    if current_barcode.isdigit():
                        # this loop should run between start barcode number & end barcode number
                        current_barcode_int = int(current_barcode)
                        if current_barcode_int >= start_barcode_number_int and current_barcode_int <= end_barcode_number_int:

                            # collect unique filename extensions in a set
                            filename_extension_set.add(filename[-4:])

                            # check filenames for correct length... required length is 16
                            # filename_length = len(filename)
                            # filename_full_path = root + "/" + filename
                            # if filename != "Thumbs.db":
                            #     # if filename_length == 16: check_results_file.write(
                            #     #     filename_full_path + " file check passed\n")
                            #     if filename_length < 16: check_results_file.write(
                            #         "check failed. shorter length. " + filename_full_path + "\n")
                            #     if filename_length > 16: check_results_file.write(
                            #         "check failed. longer length. " + filename_full_path + "\n")

                            # record all TIFF or TIF format images to the check results file
                            # if filename[-4:] == ".tif":    check_results_file.write(filename_full_path + "\n")
                            # if filename[-4:] == "tiff":    check_results_file.write(filename_full_path + "\n")
                            # if filename[-4:] == ".lnk":    check_results_file.write(filename_full_path + "\n")

            # write unique filename extensions to check results file
            for filename_extension in sorted(filename_extension_set):
                check_results_file.write(filename_extension + "\n")
            # print(list(filename_extension))
        # write unique directory paths
        for directory_path in sorted(dir_path_set):
            check_results_file.write(directory_path + "\n")

    def load_page_tags(self):
        # open text file for recording error and status update messages
        check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt", "w")

        # open csv file
        with open('/home/odoo12dev/Desktop/test_page_tags_data.csv', mode='r') as page_tags_file:
            csv_reader = csv.DictReader(page_tags_file)
            # loop through the entire csv file
            for row in csv_reader:
                # get filename field from csv file
                filename_field = row["FILENAME"]
                # print filename field to terminal output as a status update message
                print(filename_field)
                # check that filename field is NOT NULL in the csv file. do not proceed if it is
                if filename_field != "":
                    # search for correct attachment record against filename field. this is a case-insensitive search using ilike
                    attachment_obj_search_domain = [('name', '=', filename_field)]
                    search_attachment_object = self.env['ir.attachment'].search(attachment_obj_search_domain)
                    # check to see if valid object is returned. if not that means valid attachment was not found against filename
                    if search_attachment_object.res_model == False:
                        check_results_file.write(filename_field + " not found in Attachments table" + "\n")
                    if search_attachment_object.res_model == 'dms_ccb.file':
                        # search_attachment_object.dms_page_status = ""
                        # first check Document Date field in csv for Not NULL. if so then set in found attachment object
                        if row["Document Date"] != "":
                            search_attachment_object.dms_page_date = row["Document Date"]
                        # first check Page Tag field in csv for Not NULL. if so then set in found attachment object
                        if row["Page Type"] != "":
                            # search for correct page tag against page tag field in csv
                            page_tag_obj_search_domain = [('tag_name', '=like', row["Page Type"])]
                            page_tag_object = self.env['dms_ccb.page_tags'].search(page_tag_obj_search_domain)
                            if page_tag_object.tag_name == False:
                                check_results_file.write(row["Page Type"] + " tag not found" + "\n")
                                new_page_tag_object = self.env['dms_ccb.page_tags'].create(
                                    {'tag_name': row["Page Type"], 'tag_description': "", })
                                search_attachment_object.dms_ccb_page_tags = new_page_tag_object
                            if page_tag_object.tag_name != False:
                                search_attachment_object.dms_ccb_page_tags = page_tag_object
                        if row["Page TAG"] != "":
                            search_attachment_object.dms_ccb_page_description = row["Page TAG"]

    def check_csv_file(self):
        check_results_file = open("/home/odoo12dev/Desktop/check_file_results.txt", "w")
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
                        if filename_length > 16: check_results_file.write(
                            filename + " Filename length greater than 16\n")
                        if filename_length < 16: check_results_file.write(filename + " Filename length less than 16\n")
                line_count += 1
            print(f'Processed {line_count} lines.')
