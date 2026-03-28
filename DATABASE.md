# Database & Data Model Documentation

## Database Overview

The Farm Management System uses SQLite for data storage. All data is stored in `farm_management.db`.

## Database Tables

### 1. User Table

Stores user account information.

| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Unique user identifier |
| username | String(80) | Username for login (unique) |
| password | String(255) | Hashed password |
| email | String(120) | User email address |
| created_at | DateTime | Account creation date |

**Example:**
```
User ID: 1
Username: farmermanuel
Email: manuel@farm.com
Created: 2024-01-10
```

---

### 2. CropField Table

Represents physical agricultural fields.

| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Unique field identifier |
| user_id | Integer (FK) | Reference to User |
| field_name | String(120) | Name of the field |
| field_area | Float | Field area in square meters |
| location | String(255) | Geographic location |
| created_at | DateTime | Field creation date |

**Example:**
```
Field ID: 1
User: manuel
Name: North Field
Area: 5000 m²
Location: Farm District A
```

---

### 3. CropRound Table

Represents a planting cycle for a specific crop in a field.

| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Unique crop round identifier |
| field_id | Integer (FK) | Reference to CropField |
| user_id | Integer (FK) | Reference to User |
| crop_name | String(120) | Crop being planted |
| planting_date | DateTime | Date seed/plant was planted |
| estimated_harvest_date | DateTime | Expected harvest date |
| actual_harvest_date | DateTime | Actual harvest date (if harvested) |
| quantity_planted | Float | Amount planted in kg |
| quantity_harvested | Float | Amount harvested in kg |
| status | String(20) | Current status (planting/growing/ready/harvested) |
| notes | Text | Additional notes about crop |
| created_at | DateTime | Record creation date |

**Crop Status Values:**
- `planting` - Initial planting phase
- `growing` - Active growth period
- `ready` - Ready for harvest (auto-set when within 7 days of estimate)
- `harvested` - Harvest completed

**Example:**
```
Crop Round ID: 5
Field: North Field
User: manuel
Crop: Tomato
Planted: 2024-01-15
Est. Harvest: 2024-03-15
Qty Planted: 50 kg
Status: growing
```

---

### 4. Activity Table

Logs all farming activities performed on crops.

| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Unique activity identifier |
| crop_round_id | Integer (FK) | Reference to CropRound |
| user_id | Integer (FK) | Reference to User |
| activity_type | String(50) | Type of activity performed |
| activity_date | DateTime | When activity was performed |
| description | Text | Detailed description |
| quantity_used | Float | Amount of materials used |
| unit | String(20) | Unit of measurement |
| created_at | DateTime | Record creation date |

**Activity Type Values:**
- `watering` - Irrigation/watering
- `fertilizing` - Adding fertilizer
- `weeding` - Removing weeds
- `spraying` - Pesticide/fungicide spraying
- `pruning` - Plant trimming
- `pest_control` - Pest management
- `mulching` - Adding mulch
- `other` - Other activities

**Unit Values:**
- `liters` - For liquids (water, chemicals)
- `kg` - For solids (fertilizer, pesticides)
- `bags` - For packaged items
- `hours` - For labor tracking

**Example:**
```
Activity ID: 23
Crop Round: 5 (Tomato)
Date: 2024-02-01 10:30
Type: watering
Quantity: 100 liters used
Description: Morning watering with drip irrigation
```

---

### 5. Inventory Table

Manages harvested products and stock.

| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Unique inventory item identifier |
| user_id | Integer (FK) | Reference to User |
| product_name | String(120) | Name of product |
| quantity | Float | Current quantity in stock |
| unit | String(20) | Unit of measurement |
| price_per_unit | Float | Price per unit ($) |
| harvest_date | DateTime | When product was harvested |
| expiry_date | DateTime | When product expires |
| status | String(20) | Current status (in_stock/sold/expired) |
| created_at | DateTime | Record creation date |

**Inventory Status Values:**
- `in_stock` - Available for sale/use
- `sold` - Already sold
- `expired` - Past expiry date

**Example:**
```
Item ID: 42
Product: Tomato
Quantity: 150 kg
Unit: kg
Price/Unit: $2.50
Total Value: $375.00
Harvest: 2024-03-15
Expiry: 2024-05-15
Status: in_stock
```

---

## Data Relationships

```
User (1) ──────────────── (many) CropField
  |
  ├─ (many) CropRound ──────── (1) CropField
  |           |
  |           └─ (many) Activity
  |
  └─ (many) Inventory
```

### Relationship Details:

1. **User → CropField**: One user can have multiple fields
2. **User → CropRound**: One user can have multiple crop rounds
3. **CropField → CropRound**: One field can have multiple crop rounds (different seasons)
4. **CropRound → Activity**: One crop round can have many activities logged
5. **User → Inventory**: One user can have multiple inventory items
6. **CropRound → Inventory**: When crop is harvested, item created in inventory

---

## Database Queries (Advanced)

### Get all crops for a user:
```sql
SELECT * FROM crop_round WHERE user_id = 1;
```

### Get harvested crops:
```sql
SELECT * FROM crop_round WHERE status = 'harvested' AND user_id = 1;
```

### Get crops ready for harvest:
```sql
SELECT * FROM crop_round 
WHERE estimated_harvest_date <= date('now', '+7 days') 
AND status IN ('planting', 'growing')
AND user_id = 1;
```

### Get total inventory value:
```sql
SELECT SUM(quantity * price_per_unit) as total_value 
FROM inventory 
WHERE status = 'in_stock' AND user_id = 1;
```

### Get activity history for a crop:
```sql
SELECT * FROM activity 
WHERE crop_round_id = 5 
ORDER BY activity_date DESC;
```

### Get crops by field:
```sql
SELECT cr.* FROM crop_round cr
JOIN crop_field cf ON cr.field_id = cf.id
WHERE cf.field_name = 'North Field' AND cr.user_id = 1;
```

---

## Data Export Options

### Export to CSV (Manual)
1. Go to Reports page
2. Screenshot or use browser print to PDF
3. For advanced export, use Python:

```python
import csv
from app import db, CropRound

crops = CropRound.query.all()
with open('crops.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Crop', 'Planted', 'Harvest Est', 'Status'])
    for crop in crops:
        writer.writerow([crop.id, crop.crop_name, crop.planting_date, 
                        crop.estimated_harvest_date, crop.status])
```

### Database Backup
Simply copy `farm_management.db` file to safe location.

---

## Data Validation Rules

### User Registration
- Username: 3-80 characters, unique
- Password: Minimum 8 characters recommended
- Email: Valid email format

### Crop Fields
- Field name: 1-120 characters
- Area: > 0 square meters
- Location: 1-255 characters

### Crop Rounds
- Crop name: 1-120 characters
- Quantity: > 0 kg
- Est. harvest date: Must be after planting date

### Activities
- Activity type: Must be from predefined list
- Quantity: > 0 if specified
- Unit: Must be from predefined list

### Inventory
- Product name: 1-120 characters
- Quantity: >= 0
- Price: >= 0

---

## Data Privacy & Security

### Access Control
- Each user can only see their own data
- No cross-user data visibility

### Password Storage
- Passwords are hashed using Werkzeug security
- Never stored in plain text
- Cannot be recovered if forgotten

### Data Retention
- No automatic deletion of historical data
- Manual deletion through database management
- Recommended: Keep for 2+ years for analysis

---

## Performance Considerations

### Database Size Estimation
- Per user: ~10-50 KB (baseline)
- Per crop: ~5-10 KB
- Per activity: ~1-2 KB
- Per inventory item: ~2-3 KB

### For 100 users with 1000 crops total:
- Estimated database size: ~50-100 MB

### For 1000 users:
- Estimated database size: ~500 MB - 1 GB

### Query Performance
- Most queries are optimized for SQLite
- For >10,000 crops, consider moving to PostgreSQL

---

## Data Migration

### From SQLite to PostgreSQL
1. Install PostgreSQL and psycopg2
2. Create new database
3. Use SQLAlchemy migration:

```python
from sqlalchemy import create_engine
from app import db, app

# Create PostgreSQL connection
pg_engine = create_engine('postgresql://user:pass@localhost/farmdb')
db.metadata.create_all(pg_engine)

# Update app.config and re-run
```

### Backup & Recovery Script

```python
import shutil
from datetime import datetime

def backup_database():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backups/farm_management_{timestamp}.db"
    shutil.copy('farm_management.db', backup_file)
    print(f"Backup created: {backup_file}")

def restore_database(backup_file):
    shutil.copy(backup_file, 'farm_management.db')
    print(f"Database restored from: {backup_file}")
```

---

## Troubleshooting Data Issues

### Database Corruption
**Symptoms:** Application won't start, errors accessing data
**Solution:** 
1. Stop application
2. Delete farm_management.db
3. Restart application (new database created)
4. Note: This will erase all data!

### Data Mismatch
**Symptoms:** Fields show incorrect values
**Solution:**
1. Verify user session is correct
2. Clear browser cache
3. Check database for duplicate user records

### Missing Data
**Symptoms:** Some records disappeared
**Solution:**
1. Check if filters are applied
2. Verify correct user is logged in
3. Restore from backup if available

---

## Monitoring & Maintenance

### Regular Checks
- Verify database file exists
- Test backup/restore process
- Monitor database file size
- Check for corrupted records

### Recommended Maintenance
- Weekly backups
- Monthly database optimization
- Quarterly data review
- Annual data archival

---

For more information, see README.md and CONFIGURATION.md
