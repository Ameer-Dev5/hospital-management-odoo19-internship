{
    "name": "Hospital Management",
    "version": "19.0.1.0.0",
    "summary": "Basic hospital management module",
    "category": "Healthcare",
    "author": "NerithonX Technologies",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/patient_menus.xml",
        'views/patient_report_templates.xml',
        'views/patient_report.xml',
    ],
    "installable": True,
    "application": True,
}
