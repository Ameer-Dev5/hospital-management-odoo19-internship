{
    "name": "Hospital Management",
    "version": "19.0.1.1.0",
    "summary": "Basic hospital management module",
    "category": "Healthcare",
    "author": "Ameer Nawaz",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
        "website",
        "portal",
        "product",
        'sale',
        "account",
    ],
    "data": [
        "security/hospital_groups.xml",
        "security/ir.model.access.csv",
        "security/hospital_rules.xml",

        "data/product_data.xml",
        "data/urdu_language.xml",
        "data/hospital_demo_data.xml",

        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/prescription_views.xml",
        "views/consultation_views.xml",
        "views/billing_views.xml",
        "views/patient_menus.xml",
        "views/patient_report_templates.xml",
        "views/patient_report.xml",
        "views/appointment_views.xml",
        "views/website_patient_templates.xml",
        "views/website_appointment_templates.xml",
        "views/portal_templates.xml",
        'views/sales_integration_views.xml',
        "views/accounting_integration_views.xml",
        "views/website_menu.xml",
        "views/hospital_dashboard_views.xml",
        "views/patient_upgrade_views.xml",

        "data/patient_cron.xml",
        "data/patient_email_template.xml",
        "data/appointment_email_template.xml",
        "data/sequence_pt.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "hospital_base/static/src/components/hospital_dashboard.js",
            "hospital_base/static/src/components/hospital_dashboard.xml",
        ],
    },

    "installable": True,
    "application": True,
}
