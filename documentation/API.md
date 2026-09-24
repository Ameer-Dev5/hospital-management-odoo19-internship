# Hospital REST API

## Base URL

http://localhost:8069

## Authentication

Authentication uses an Odoo Bearer API Key.

Header:

Authorization: Bearer <API_KEY>

Database header:

X-Odoo-Database: odoo19

## 1. API Test

### Endpoint

GET /api/hospital/test

### Authentication

Required

### Response

```json
{
    "success": true,
    "message": "Hospital API is working.",
    "user_id": 2,
    "user_name": "Mitchell Admin"
}
