
{
    'name': 'Eagle Education Library',
    'version': '10.0.3.0.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Library',
    'complexity': "easy",
    'author': 'Md. Ashrafuzzaman',
    'website': 'http://www.eagle-it-services.com',
    'depends': ['openeducat_core', 'account_accountant',
                'openeducat_activity', 'base_action_rule'],
    'data': [
        'data/custom_paperformat.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'report/report_media_barcode.xml',
        'report/report_library_card_barcode.xml',
        'report/report_student_library_card.xml',
        'report/report_menu.xml',
        'wizards/issue_media_view.xml',
        'wizards/return_media_view.xml',
        'wizards/reserve_media_view.xml',
        'views/media_view.xml',
        'views/media_unit_view.xml',
        'views/media_movement_view.xml',
        'views/media_purchase_view.xml',
        'views/media_queue_view.xml',
        'views/library_view.xml',
        'views/author_view.xml',
        'views/publisher_view.xml',
        'views/tag_view.xml',
        'views/media_type_view.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
        'dashboard/library_student_dashboard.xml',
        'media_queue_sequence.xml',
        'menus/library_menu.xml',
        'data/action_rule_data.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
        'demo/media_type_demo.xml',
        'demo/res_users_demo.xml',
        'demo/tag_demo.xml',
        'demo/publisher_demo.xml',
        'demo/author_demo.xml',
        'demo/media_demo.xml',
        'demo/media_unit_demo.xml',
        'demo/media_queue_demo.xml',
        'demo/library_card_type_demo.xml',
        'demo/library_card_demo.xml',
        'demo/media_movement_demo.xml',
    ],
    'test': [
        'test/res_users_test.yml',
        'test/library_sub_values.yml',
        'test/media_movements.yml',
        'test/media_queue_request.yml',
        'test/media_purchase_request.yml',
    ],
    'images': [
        'static/description/openeducat_library_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
