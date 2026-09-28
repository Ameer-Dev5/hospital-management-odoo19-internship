No pre-migrate or post-migrate script was needed for this version.
The new `blood_group` field is a nullable Selection field added to an
existing model — Odoo's ORM adds the column automatically on upgrade
with NULL defaults for existing rows, so no data transformation was
required. A migration script would be needed if a field were renamed,
a column type changed incompatibly, or data needed transforming
before the new schema could be used.
