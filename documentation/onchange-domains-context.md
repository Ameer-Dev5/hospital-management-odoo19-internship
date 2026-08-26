# Onchange, Domains and Context

## 1. Patient Onchange

The Primary Doctor field has an onchange method.

When the Primary Doctor changes:

- The selected doctor is automatically added to Treating Doctors.
- The patient's Notes field displays the selected doctor's name.
- When the doctor is cleared, the Treating Doctors field and Notes are cleared.

## 2. Second Onchange

The Date of Birth field has an onchange method.

When the Date of Birth changes, the available Primary Doctors are dynamically filtered.

## 3. Static Domain

The Primary Doctor field uses:

    [('active', '=', True)]

This means inactive doctors are not shown in the normal Doctor selection.

## 4. Dynamic Domain

The Doctor domain changes according to the patient's Date of Birth.

For patients under 18:

    [('active', '=', True), ('specialization', '!=', False)]

For adults:

    [('active', '=', True)]

This makes the Doctor selection more relevant.

## 5. Odoo Context

Five common context keys:

1. `default_field_name`
   Provides a default value when a record is created.

2. `active_id`
   Contains the current active record ID.

3. `active_ids`
   Contains the IDs of multiple active records.

4. `active_model`
   Contains the model name of the active record.

5. `group_by`
   Specifies a field to group records by in supported views.

Context is temporary information passed through an Odoo operation. It is not permanent database data.

## 6. Context-Based Default

The Patient action sends:

    {'default_gender': 'male'}

The Patient model reads this value using:

    self.env.context.get('default_gender')

Therefore, when a Patient is created from the Patients menu, Gender defaults to Male.

## 7. Behavioral Observations

1. A Primary Doctor can only be selected from active doctors.
2. Selecting a Primary Doctor automatically updates Treating Doctors.
3. Selecting a Primary Doctor also updates the Patient Notes.
4. Changing Date of Birth dynamically changes the available Doctor selection.
5. Opening Patient creation from the Patients menu defaults Gender to Male.
6. Clearing the Primary Doctor clears the related onchange values.
7. The dynamic behavior happens in the form interface and does not replace server-side validation.
