# Hospital Management (hospital_base)

Odoo 19 Community module for managing a small hospital or clinic.

## Features
- Patient management (registration, states, age groups, blood group)
- Doctors and doctor-patient assignment
- Appointments with email notifications
- Consultations, prescriptions and billing
- Sales integration (quotations) and accounting integration (invoices)
- Website appointment/patient pages and customer portal
- Patient PDF report
- OWL dashboard (client action) showing patient and appointment counts
- Multi-company support
- API controller (`controllers/api.py`)
- Scheduled action and email templates
- Automated tests (`tests/`)

## Requirements
- Odoo 19.0 Community
- Odoo modules: base, mail, website, portal, product, sale, account

## Installation
1. Copy the `hospital_base` folder into your custom addons path.
2. Add that path to `addons_path` in `odoo.conf`.
3. Restart Odoo, then go to Apps > Update Apps List.
4. Install "Hospital Management".

Command line:

    ./odoo-bin -c odoo.conf -d <database> -i hospital_base

## Configuration
- Assign users to the Hospital User, Hospital Doctor or Hospital Manager group (Settings > Users).
- Configure an outgoing mail server for registration and appointment emails.
- Demo data (sample patients, doctor) loads only on databases created with demo data enabled.

## Basic Usage
Open Hospital Management > Dashboard for totals. Create patients and doctors, book appointments, then record consultations, prescriptions and billing from the same menu. Use the buttons on the patient and consultation forms to create quotations and invoices.

## Security
Access is controlled by the Hospital groups, model access rules (`security/ir.model.access.csv`) and record rules (`security/hospital_rules.xml`). The dashboard reads data as the logged-in user, so it only shows records that user can access.

## Testing

    ./odoo-bin -c odoo.conf -d <database> -u hospital_base --test-tags /hospital_base --stop-after-init

## Known Limitations
- Demo data is for testing only.
- Dashboard shows totals only (no charts or filters).
- Urdu (ur_PK) language is activated on install, but translations are partial.
