# Code Review Notes — Day 38

## Reviewed
- models/, views/, security/, controllers/, tests/

## Issues found and fixed
- Removed unnecessary/unsafe sudo() usage in controllers/main.py on 4 public
  website routes (/hospital/patients, /hospital/appointment,
  /hospital/appointment/submit). These routes used sudo() combined with
  auth='public', exposing all active patient records and allowing
  appointment creation for any patient ID without an ownership check.
  Changed auth to 'user' on all four routes, removed sudo(), and added
  patient.check_access('read') in appointment_submit before creating the
  appointment. Removed sitemap=True from the patients listing page so it
  is no longer indexed by search engines.

## Issues reviewed, no change needed
- sudo() usage in controllers/portal.py (2 calls): kept. Portal users
  don't have direct read access to hospital.patient, and both calls are
  scoped to request.env.user.partner_id.id, so a user can only ever look
  up their own patient record.
- Raw SQL: none found in models or controllers.
- search() inside loops: none found.
- Multi-record method handling: reviewed all 18 action_* methods across
  appointment.py, billing.py, patient.py, doctor.py,
  sales_integration.py, accounting_integration.py. All either use
  self.write({...}) (safe across recordsets), an explicit
  `for record in self:` loop, or self.ensure_one() where the method
  genuinely only makes sense for a single record. No changes needed.
- Duplicated business logic: no _prepare_*/_get_* helper pattern exists
  in the module; no significant duplication found across models.
- XML: no duplicate record IDs found across views/*.xml.

## Regression testing
- Module upgrade (odoo19): clean, no errors
- Automated tests: 0 failed, 0 error(s) of 5 tests
- Manual check (logged in as normal user): patients, appointments,
  consultations, prescriptions, billing, dashboard, website appointment
  booking, portal /my/appointments, patient PDF report — all working
- Confirmed /hospital/patients and /hospital/appointment now require
  login (previously public)
