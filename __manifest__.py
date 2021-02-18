{
	'name': 'Document Management System (CCB)',
	'sequence': 1,
	'summary': 'DMS developed by EGS Pvt Ltd for Chaklala Cantonment Board',
	'description': 'DMS developed by EGS Pvt Ltd for Chaklala Cantonment Board',
	'version': '12.0.1.0',
	'author': 'EGS Pvt. Ltd.',
	'license': 'LGPL-3',
	'website': 'http://www.egs.net.pk/',
	'category': 'Document Management',
	'depends': ['base','mail'],
	'application': True,
	# if installable is set to false module will be disabled
	'installable': True,
	'data': [
		'security/dms_ccb_file_security.xml',
		'security/dms_ccb_page_security.xml',
		'security/dms_ccb_colony_obj_security.xml',
		'security/dms_ccb_branch_obj_security.xml',
		'security/dms_ccb_type_of_land_obj_security.xml',
		'security/dms_ccb_page_tags_security.xml',
		'security/dms_ccb_record_type_obj_security.xml',
		'security/dms_ccb_purpose_object_security.xml',
		'security/dms_ccb_rej_reasons_security.xml',
		'security/dms_ccb_qc_audit_access_security.xml',
		'security/dms_ccb_record_rules.xml',
		'security/dms_ccb_erp_integ_security.xml',

		'security/dms_meo_file_security.xml',
		'security/dms_meo_page_security.xml',
		'security/dms_meo_colony_obj_security.xml',
		'security/dms_meo_branch_obj_security.xml',
		'security/dms_meo_type_of_land_obj_security.xml',
		'security/dms_meo_page_tags_security.xml',
		'security/dms_meo_record_type_obj_security.xml',
		'security/dms_meo_purpose_object_security.xml',
		'security/dms_meo_rej_reasons_security.xml',
		'security/dms_meo_qc_audit_access_security.xml',
		'security/dms_meo_record_rules.xml',
		'security/dms_meo_erp_integ_security.xml',

		'security/ir.model.access.csv',

		'data/sequence.xml',

		'views/dms_ccb_menu.xml',
		'views/dms_ccb_record_type_views.xml',
		'views/dms_ccb_colony_views.xml',
		'views/dms_ccb_type_of_land_views.xml',		
		'views/dms_ccb_purpose_views.xml',		
		'views/dms_ccb_branch_views.xml',		
		'views/dms_ccb_attribute_views.xml',		
		'views/dms_ccb_page_tag_views.xml',		
		'views/dms_ccb_file_views.xml',
		'views/dms_ccb_page_rej_reasons_views.xml',
		'views/attachment_view_extension.xml',
		'views/dms_ccb_erp_integration_views.xml',
		'views/dms_ccb_bulk_data_import_view.xml',
		# 'views/dashboard.xml',

		'views/dms_meo_menu.xml',
		'views/dms_meo_record_type_views.xml',
		'views/dms_meo_colony_views.xml',
		'views/dms_meo_type_of_land_views.xml',		
		'views/dms_meo_purpose_views.xml',		
		'views/dms_meo_branch_views.xml',		
		'views/dms_meo_attribute_views.xml',		
		'views/dms_meo_page_tag_views.xml',		
		'views/dms_meo_file_views.xml',
		'views/dms_meo_page_rej_reasons_views.xml',
		'views/dms_meo_erp_integration_views.xml',		
		# 'views/attachment_view_extension.xml',

		'reports/report.xml',
		'reports/dms_file_card.xml',
		'views/file_list_template.xml',

		'data/demo_data_record_type.xml',
		'data/demo_data_colony.xml',
		'data/demo_data_type_of_land.xml',
		'data/demo_data_purpose.xml',
		'data/demo_data_page_tags.xml',
		'data/demo_data_branches.xml',		
	],
}