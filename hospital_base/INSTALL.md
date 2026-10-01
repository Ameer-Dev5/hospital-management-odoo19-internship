# Installation Guide

## 1. Copy the module
Copy `hospital_base/` into your Odoo custom addons folder, e.g.:

    cp -r hospital_base /path/to/custom_addons/

## 2. Install dependencies
This module depends on Odoo's own base, mail, website, portal, product, sale, and account modules, which ship with Odoo 19 Community. No external Python packages are required beyond what Odoo itself needs.

## 3. Configure the addons path
In `odoo.conf`:

    addons_path = /path/to/odoo/addons,/path/to/custom_addons

## 4. Create a database
    ./odoo-bin -c odoo.conf -d <database_name> --stop-after-init

## 5. Install the module
    ./odoo-bin -c odoo.conf -d <database_name> -i hospital_base --stop-after-init

Or via the UI: Apps > Update Apps List > search "Hospital Management" > Install.

## 6. Configure users
Go to Settings > Users & Companies > Users, create or edit a user, and assign one of:
- Hospital User
- Hospital Doctor
- Hospital Manager

For external patients who need portal access, link their `res.partner` to a `hospital.patient` record via the `partner_id` field, and grant portal access from the Contacts app (Action > Grant Portal Access).

## Verify the install
    ./odoo-bin -c odoo.conf -d <database_name> -u hospital_base --test-tags /hospital_base --stop-after-init

Expect: `0 failed, 0 error(s) of 5 tests`.
