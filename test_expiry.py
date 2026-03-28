#!/usr/bin/env python
"""Test script to verify expiry functionality"""
from app import app, db, User, Inventory
from datetime import datetime, timedelta

with app.app_context():
    db.create_all()
    
    # Get or create user
    user = User.query.filter_by(username='testuser').first()
    if not user:
        user = User(
            username='testuser',
            email='test@example.com',
            password='hashed_password'
        )
        db.session.add(user)
        db.session.commit()
    
    print("Testing expiry functionality:")
    
    # Create test inventory items with different expiry dates
    now = datetime.now()
    
    # Item that should be expired (expiry date in the past)
    expired_item = Inventory(
        user_id=user.id,
        product_name='Expired Tomato',
        quantity=5.0,
        unit='kg',
        price_per_unit=2.50,
        harvest_date=now - timedelta(days=15),
        expiry_date=now - timedelta(days=5),  # 5 days ago
        status='in_stock'
    )
    
    # Item that should still be valid
    valid_item = Inventory(
        user_id=user.id,
        product_name='Fresh Tomato',
        quantity=10.0,
        unit='kg',
        price_per_unit=2.50,
        harvest_date=now - timedelta(days=5),
        expiry_date=now + timedelta(days=5),  # 5 days from now
        status='in_stock'
    )
    
    db.session.add(expired_item)
    db.session.add(valid_item)
    db.session.commit()
    
    print(f"✓ Created test items:")
    print(f"  - Expired item: {expired_item.product_name} (expiry: {expired_item.expiry_date})")
    print(f"  - Valid item: {valid_item.product_name} (expiry: {valid_item.expiry_date})")
    
    # Test the update function
    from app import update_expired_inventory
    update_expired_inventory(user.id)
    
    # Check results
    expired_item_updated = Inventory.query.get(expired_item.id)
    valid_item_updated = Inventory.query.get(valid_item.id)
    
    print(f"\nAfter update:")
    print(f"✓ Expired item status: {expired_item_updated.status}")
    print(f"✓ Valid item status: {valid_item_updated.status}")
    
    if expired_item_updated.status == 'expired':
        print("✅ Expiry system working correctly!")
    else:
        print("❌ Expiry system not working - expired item not updated")
    
    if valid_item_updated.status == 'in_stock':
        print("✅ Valid items preserved correctly!")
    else:
        print("❌ Valid items incorrectly marked as expired")

print("\nExpiry test completed!")
