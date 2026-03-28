# Feature Guide & Best Practices

## Feature Overview

### 1. Authentication System

#### Login
- Username and password required
- Session-based authentication
- All user data is isolated and private

#### Registration
- Create new account with username, email, password
- Passwords are securely hashed
- Account creation is instant

**Best Practices:**
- Use memorable but unique username
- Use strong password (8+ characters, uppercase, numbers)
- Keep login credentials private
- Log out when leaving device

---

### 2. Crop Management

#### Fields (Physical Land Areas)

**Purpose:** Organize your farm into manageable sections

**Fields Tab Information:**
- Field Name: Descriptive name (e.g., "North Field", "Greenhouse 1")
- Area: Size in square meters
- Location: Geographic or descriptive location

**Best Practices:**
- Name fields logically for easy reference
- Enter accurate area for resource planning
- Create fields based on soil type, irrigation, or geography
- One field = one consistent growing area

**Example Setup:**
```
Field 1: Main Field
- Area: 5000 m²
- Location: North farm, Sandy soil

Field 2: Greenhouse
- Area: 200 m²
- Location: West side, Climate controlled

Field 3: Organic Section
- Area: 3000 m²
- Location: Southeast, No pesticides
```

#### Crop Rounds (Planting Cycles)

**Purpose:** Track each planting event within a field

**Key Information:**
- Crop Type: What vegetable (Tomato, Lettuce, etc.)
- Planting Date: When seeds/plants went in ground
- Est. Harvest: When you expect to harvest
- Quantity: How much was planted (in kg)

**Status Values:**
- Planting: Recently planted, establishing
- Growing: Active growth phase
- Ready: Ready for or should be harvested
- Harvested: Harvest complete, moved to inventory

**Status Transitions (Automatic):**
```
planting → growing → ready → harvested
           (manual transitions)
```

**Best Practices:**
- Use realistic harvest estimates (consider crop variety)
- Track quantity for yield calculation
- Plan successive plantings for continuous harvest
- Note any special conditions or varieties
- Review past harvests for planning

**Example Timeline:**
```
Crop: Tomato Variety X
Planted: 2024-01-15
Est. Harvest: 2024-03-15 (60 days)
- 01-15: Plant seeds
- 02-15: Transplant to field
- 03-01: First flowering
- 03-10: Start harvesting
- 03-15: Peak harvest
```

---

### 3. Activity & Task Logging

#### Purpose
Track all farming operations to:
- Maintain complete operational records
- Plan future activities
- Calculate production costs
- Identify successful practices

#### Activity Types

**Watering**
- Frequency: Usually 2-3 times weekly
- Track: Liters of water used
- Log immediately after irrigation

**Fertilizing**
- Quantity: Amount of fertilizer used (kg)
- Type: Note fertilizer type in description
- Timing: Follow feeding schedule for crop

**Weeding**
- Note: Hours spent if manual
- Or: Type of weeds (optional)
- Frequency: As needed

**Spraying**
- Quantity: Liters of spray used
- Type: Pesticide/fungicide/herbicide name
- Reason: What problem you're addressing

**Pest Control**
- Method: Manual removal/traps/insecticide
- Pest type: Identify pest in description
- Effectiveness: Note results

**Pruning**
- Hours: Labor hours spent
- Purpose: Thinning/training/maintenance
- Notes: Any special techniques

**Mulching**
- Quantity: Amount of mulch applied (kg)
- Type: Hay/straw/plastic/etc
- Purpose: Weed control/moisture/temperature

**Best Practices:**
- Log activities daily for accuracy
- Be specific in descriptions
- Track quantitatively for cost analysis
- Photos helpful (saved separately)
- Note unexpected issues
- Review patterns monthly

**Example Log:**
```
Date: 2024-02-01 10:30 AM
Activity: Watering
Quantity: 100 liters (drip irrigation)
Notes: Morning watering, all plants look healthy

Date: 2024-02-05 9:00 AM
Activity: Fertilizing
Quantity: 25 kg (NPK 20-20-20)
Notes: Second feeding, plants responding well

Date: 2024-02-10 14:00
Activity: Pest Control
Quantity: 10 liters (Neem oil spray)
Notes: Treating early aphids on leaves
```

---

### 4. Harvest Management

#### Recording Harvest

**Process:**
1. Go to crop details
2. Scroll to actions section
3. Enter harvest quantity (actual amount harvested)
4. Enter price per unit (expected selling price)
5. Click "Mark as Harvested"

**What Happens:**
- Crop status changes to "Harvested"
- Item automatically added to inventory with 10-day expiry
- Expiry date calculated: Harvest Date + 10 days
- Data moved to Reports for analysis
- History preserved for future reference

**Key Data Points:**
- Date: Automatically recorded
- Quantity: Amount harvested (kg)
- Price: Unit price for value calculation
- Expiry: Automatically set to 10 days from harvest
- Crop name: Food item name in inventory

**Best Practices:**
- Record immediately after harvest
- Weigh produce accurately
- Set realistic market prices
- Note if yield was above/below estimate
- Compare with past harvests

**Example:**
```
Crop: Tomato (planted 60 days ago)
Quantity Planted: 50 kg seeds/transplants
Quantity Harvested: 425 kg
Price Per Unit: $2.50/kg
Total Value: $1,062.50
Yield: 8.5x (425/50)
```

---

### 5. Inventory Management

#### Purpose
Track harvested products for:
- Sales management
- Stock levels
- Revenue calculation
- Expiry tracking

#### Inventory Status

**In Stock**
- Product currently available
- Ready for sale/use
- No expiry date needed (optional)

**Sold**
- Product has been sold
- Moved out of available inventory
- Still tracked for revenue records

**Expired**
- Product past expiry date
- No longer available
- Tracked for waste management

#### Managing Inventory

**View:**
- Check At-a-glance: Inventory value on Dashboard
- Detailed view: Inventory page with all items
- Filter by status: In Stock, Sold, Expired

**Update:**
1. Find item in Inventory page
2. Edit quantity (if picking/using stock)
3. Change status if needed (Sold/Expired)
4. Click "Save" button

**Important Fields:**
- Product Name: What it is (auto-filled from crop)
- Quantity: Current stock level (update as sell)
- Unit: kg, bags, liters (per crop)
- Price/Unit: Selling price per unit
- Total Value: Auto-calculated (Qty × Price/Unit)
- Harvest Date: When harvested (auto-filled)
- Expiry Date: When product expires (optional)

**Best Practices:**
- Update quantities as you sell
- Set realistic expiry dates for perishables
- Review inventory weekly
- Archive old items to "Sold" status
- Track inventory value for financial planning
- Set expiry alerts for perishables

**Example Inventory:**
```
Tomatoes (Fresh):
- Quantity: 120 kg
- Unit Price: $2.50/kg
- Total: $300
- Harvest: 2024-03-15
- Expiry: 2024-05-15
- Status: In Stock

Carrots (Stored):
- Quantity: 85 kg
- Unit Price: $1.20/kg
- Total: $102
- Harvest: 2024-03-10
- Expiry: 2024-06-30
- Status: In Stock

Lettuce (Sold):
- Quantity: 50 kg (sold out)
- Unit Price: $3.00/kg
- Total: $150 (revenue)
- Status: Sold
```

---

### 6. Alerts System

#### Alert Types

**Harvest Ready**
- Triggered: Estimated harvest date ≤ 7 days away
- Shows: Crop name, dates, current status
- Action: Review crop and prepare for harvest

**Inventory Expiry**
- **Automatic Expiry**: Items expire exactly 10 days after harvest date
- **Expiry Calculation**: Harvest Date + 10 days = Expiry Date
- **Status Update**: Items automatically marked as "Expired" when expiry date passes
- **Alert Trigger**: Items expiring within 7 days show in alerts
- **Shows**: Product name, expiry date, quantity remaining

**Where to See:**
- Dashboard: Summary of active alerts
- Alerts page: Full details and actions
- Inventory page: Items automatically show as "Expired" status

**Best Practices:**
- Check alerts daily for items expiring soon
- Plan sales for items approaching expiry (within 7 days)
- Items automatically expire after 10 days - no manual action needed
- Monitor inventory value to track at-risk assets
- Use expiry alerts to prioritize sales

**Expiry Timeline Example:**
```
Day 0: Harvest tomatoes → Expiry = Harvest + 10 days
Day 3: Still fresh (7 days until expiry)
Day 7: Alert shows (3 days until expiry)
Day 10: Automatically marked as "Expired"
Day 11+: Status remains "Expired"

Wednesday:
- Lettuce: Expiring in 5 days
- Action: Mark for sale this week

Thursday:
- Peppers: Next round ready to plant
- Action: Prepare seedlings
```

---

### 7. Activity Log & Analytics

#### Activity History

**View:**
- Find Activities menu → Activity Log
- Chronological list of all tasks
- Pagination for easy browsing

**Filter:**
- By date (oldest/newest first)
- By activity type
- Search description

**Purpose:**
- Complete farm record
- Compliance documentation
- Cost calculation
- Trend analysis

**Best Practices:**
- Review regularly
- Export for record keeping
- Calculate average cost per crop
- Identify most frequent activities
- Plan next season based on history

**Example Analysis:**
```
June Tomato Crop Statistics:
- Total Waterings: 24 (100 liters each = 2,400L)
- Total Fertilizing: 4 times (50 kg total)
- Days from plant to harvest: 65 days
- Total harvested: 425 kg
- Water efficiency: 5.6 kg per liter
- Cost analysis: Track expenses vs. yield
```

---

### 8. Reports & Dashboard

#### Dashboard Stats

**At-a-Glance Metrics:**
- Total Fields: Count of all farm sections
- Active Crops: Currently growing crops
- Inventory Count: Items in stock
- Inventory Value: Total value of stock
- Harvest Alerts: Ready-to-harvest crops
- Recent Activities: Latest farm tasks

**Purpose:** Quick farm status check

#### Reports Page

**Production Summary:**
- All crops with planting/harvest dates
- Quantities planted vs. harvested
- Life cycle of each crop
- Status of all crops

**Inventory Summary:**
- All products with quantities
- Unit prices and total values
- Storage status
- Revenue potential

**Calculations:**
- Yield per crop (planted vs. harvested)
- Revenue per crop (qty × price)
- Inventory value (total at-risk asset)
- Productivity metrics

**Reports Best Practices:**
- Generate monthly summaries
- Compare year-over-year data
- Identify high-performing crops
- Plan rotations based on yield
- Track ROI (revenue vs. inputs)
- Generate for tax/accounting purposes

**Example Report:**
```
Monthly Report - March 2024

Total Harvested Crops: 3
Total Harvest Quantity: 890 kg

Crop Breakdown:
- Tomatoes: 425 kg @ $2.50/kg = $1,062.50
- Carrots: 300 kg @ $1.20/kg = $360.00
- Lettuce: 165 kg @ $3.00/kg = $495.00

Current Inventory Value: $1,500.23
Items in Stock: 8 products

Production Efficiency:
- Avg Yield: 7.2x (total harvested / total planted)
- Waste: 2% of harvest
```

---

## Workflow Examples

### Example 1: Seasonal Plantation

```
Step 1: Create Field (January)
- Field: "Spring Garden"
- Area: 2000 m²
- Location: South section

Step 2: Add First Crop (January 15)
- Crop: Tomato
- Planted: 01-15
- Est. Harvest: 03-15 (60 days)
- Qty: 50 kg

Step 3: Log Activities (January - March)
- 01-20: Watering (50L)
- 02-01: Fertilizing (10kg NPK)
- 02-10: Pest Control (spray)
- 02-20: Fertilizing (10kg NPK)
- 03-01: Watering (75L)

Step 4: Other Side Plant (February 15)
- Crop: Lettuce
- Planted: 02-15
- Est. Harvest: 03-25 (40 days)
- Qty: 30 kg

Step 5: Succession Plant (March 1)
- Crop: Peppers
- Planted: 03-01
- Est. Harvest: 05-15 (75 days)
- Qty: 40 kg

Step 6: Harvest & Record (March 15)
- Tomatoes ready
- Quantity: 420 kg
- Price: $2.50/kg
- Move to inventory

Step 7: Continue Activities
- Lettuce picking (03-22 onward)
- Peppers maturing
- Start watering peppers more

Result: Continuous harvest and income generation
```

### Example 2: Full Farm Rotation

```
Year 1 - Spring:
Field 1: Tomatoes
Field 2: Peppers
Field 3: Fallow (rest)

Year 1 - Summer:
Field 1: Fallow
Field 2: Tomatoes
Field 3: Peppers

Year 1 - Fall:
Field 1: Peppers
Field 2: Fallow
Field 3: Tomatoes

Benefits:
- Disease prevention
- Soil nutrition maintenance
- Pest cycle disruption
- Production continuity
```

---

## Tips & Tricks

### Maximize Yield
- Choose varieties suited to climate
- Track successful varieties in notes
- Replicate best practices
- Plan plantings 2-3 weeks apart
- Monitor alerts for optimal harvest timing

### Reduce Costs
- Compare activity costs in logs
- Optimize watering schedules
- Use seasonal discounts for inputs
- Share equipment with other farms
- Track exact quantities used

### Quality Control
- Log any issues in activity notes
- Track pest outbreaks
- Document disease treatments
- Note environmental stresses
- Compare crops with special conditions

### Record Keeping
- Update data daily if possible
- Review weekly for accuracy
- Archive old data monthly
- Generate reports quarterly
- Back up database regularly

### Planning
- Use past data for next season
- Set realistic harvest estimates
- Plan succession planting
- Allocate resources efficiently
- Track market demand

---

## Troubleshooting Features

### Crop not showing harvest alert
**Solution:** Check that estimated harvest date is within next 7 days

### Inventory not updating
**Solution:** Click "Save" button after making changes, don't just refresh

### Activities not appearing
**Solution:** Verify crop is selected correctly, check date filter

### Reports showing zero values
**Solution:** Ensure crops are "harvested" status with value in quantity_harvested

### Dashboard looks wrong
**Solution:** Clear browser cache (Ctrl+Shift+Delete), refresh page (F5)

---

For more information on features, see README.md
