# Production Readiness Report, Day 39

| Feature | Status | Issue | Severity | Action Required |
|---|---|---|---|---|
| Website appointment booking | Fail | Requires login now (fixed Day 38); portal users have no read access to hospital.patient, so external/unauthenticated patients cannot use the public booking form at all | Medium | Redesign so a visitor submits their own contact details and a new patient record is created for them, instead of selecting from the existing patient list |
| Portal access boundary (/my/appointments) | Pass | Logged in as a portal-only test user linked to one patient; own appointment loads, other appointment IDs return not found | | |
| Hospital role access (User/Doctor/Manager) | Not fully tested | Only the admin account is assigned Hospital Manager; no separate Hospital User or Hospital Doctor test accounts exist in this database | Medium | Create dedicated test accounts for each Hospital role and verify record rules before go-live |
| REST API (/api/hospital/*) | Pass | All 4 routes use auth="bearer" with no sudo(); access errors are caught and returned as 403/404 JSON instead of leaking data | | |
| Multi-company isolation | Not tested | Only one company exists in this database | Medium | Set up a second company and test company-scoped record visibility before production |
| Multi-currency conversion | Not tested | Depends on multi-company setup | Medium | Same as above |
| Automated tests | Pass | 0 failed, 0 error(s) of 5 tests | | |
| Module upgrade | Pass | Clean upgrade, no errors | | |

## Summary
Total features tested: 8
Passed: 4
Failed: 1
Not tested: 3 (Hospital role separation, multi-company, multi-currency)

## Remaining issues
- Website appointment booking needs a redesign for genuine public/unauthenticated use.
- Hospital User/Doctor/Manager role separation is not verified with real test accounts; only admin has been checked.
- Multi-company and multi-currency behavior has not been verified; this database only has one company configured.
