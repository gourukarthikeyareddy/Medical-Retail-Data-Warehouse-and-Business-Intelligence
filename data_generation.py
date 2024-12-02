import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

fake = Faker()

# Number of rows to generate for each table
NUM_SUPPLIERS = 1000
NUM_EQUIPMENT = 1000
NUM_WAREHOUSES = 500
NUM_HOSPITALS = 1000
NUM_ORDERS = 1500
NUM_EMPLOYEES = 1000
NUM_SHIPMENTS = 1500
NUM_ORDER_DETAILS = 5000
NUM_INVENTORY = 5000

# Helper Functions
def random_date(start, end):
    """Generate a random date between two datetime objects."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_phone_number():
    """Generate a 10-digit phone number that doesn't start with 0."""
    first_digit = random.randint(1, 9)  # Ensures the first digit is between 1-9
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])  # Generates 9 remaining digits
    return str(first_digit) + remaining_digits

def truncate_string(string, max_length=50):
    """Truncate the string to the maximum length allowed."""
    return string[:max_length]

# Countries and States
countries_and_states = {
    "United States": ["Massachusetts", "New York", "Arizona", "Utah", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia"],
    "Canada": ["Alberta", "British Columbia", "Manitoba", "Ontario", "Quebec"],
    "Australia": ["New South Wales", "Victoria", "Queensland", "Tasmania", "Australian Capital Territory"],
    "Germany": ["Bavaria", "Berlin", "Hamburg", "Hesse", "Lower Saxony", "North Rhine-Westphalia", "Rhineland-Palatinate", "Saarland", "Saxony", "Schleswig-Holstein"],
    "United Kingdom": ["England", "Scotland", "Wales", "Northern Ireland"],
    "India": ["Andhra Pradesh", "Bihar", "Gujarat", "Karnataka", "Kerala", "Maharashtra", "Punjab", "Rajasthan", "Tamil Nadu", "Uttar Pradesh"],
    "Brazil": ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Goiás", "Maranhão", "Mato Grosso", "Pernambuco"],
    "Mexico": ["Aguascalientes", "Baja California", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero"],
    "France": ["Auvergne-Rhône-Alpes", "Brittany", "Corsica", "Grand Est", "Hauts-de-France", "Île-de-France", "Normandy", "Nouvelle-Aquitaine", "Occitanie", "Pays de la Loire"],
    "Italy": ["Abruzzo", "Basilicata", "Calabria", "Campania", "Emilia-Romagna", "Lazio", "Liguria", "Lombardy", "Marche", "Piedmont"],
    "Spain": ["Andalusia", "Aragon", "Asturias", "Balearic Islands", "Basque Country", "Canary Islands", "Cantabria", "Castile and León", "Castilla-La Mancha", "Catalonia"],
    "Japan": ["Hokkaido", "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima", "Ibaraki", "Tochigi", "Gunma"],
    "China": ["Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei"],
    "Russia": ["Adygea", "Altai Republic", "Amur Oblast", "Arkhangelsk Oblast", "Astrakhan Oblast", "Bashkortostan", "Belgorod Oblast", "Bryansk Oblast"],
    "South Africa": ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "Northern Cape", "North West", "Western Cape"],
    "Argentina": ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa"],
    "Chile": ["Antofagasta", "Araucanía", "Atacama", "Aysén", "Biobío", "Coquimbo", "Los Lagos", "Magallanes", "Maule", "Metropolitana"],
    "Nigeria": ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta"],
    "Kenya": ["Baringo", "Bomet", "Bungoma", "Busia", "Elgeyo-Marakwet", "Embu", "Garissa", "Homa Bay", "Isiolo", "Kajiado"],
    "Egypt": ["Alexandria", "Aswan", "Asyut", "Beheira", "Beni Suef", "Cairo", "Dakahlia", "Damietta", "Faiyum", "Gharbia"],
    "Turkey": ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin"],
    "Saudi Arabia": ["Al Bahah", "Al Jawf", "Al Madinah", "Al-Qassim", "Asir", "Eastern Province", "Hail", "Jizan", "Mecca", "Najran"],
    "South Korea": ["Busan", "Chungbuk", "Chungnam", "Daegu", "Daejeon", "Gangwon", "Gwangju", "Gyeongbuk", "Gyeonggi", "Gyeongnam"],
    "Vietnam": ["An Giang", "Ba Ria-Vung Tau", "Bac Giang", "Bac Kan", "Bac Lieu", "Bac Ninh", "Ben Tre", "Binh Dinh", "Binh Duong", "Binh Phuoc"],
    "Indonesia": ["Aceh", "Bali", "Banten", "Bengkulu", "Central Java", "Central Kalimantan", "Central Sulawesi", "East Java"],
    "Malaysia": ["Johor", "Kedah", "Kelantan", "Kuala Lumpur", "Labuan", "Malacca", "Negeri Sembilan", "Pahang", "Penang", "Perak"],
    "Thailand": ["Bangkok", "Chiang Mai", "Chiang Rai", "Chonburi", "Krabi", "Phang Nga", "Phatthalung", "Phuket", "Songkhla", "Surat Thani"],
    "Netherlands": ["Drenthe", "Flevoland", "Friesland", "Gelderland", "Groningen", "Limburg", "North Brabant", "North Holland", "Overijssel", "Utrecht"],
    "Sweden": ["Blekinge", "Dalarna", "Gävleborg", "Gotland", "Halland", "Jämtland", "Jönköping", "Kalmar", "Kronoberg", "Norrbotten"],
    "New Zealand": ["Auckland", "Bay of Plenty", "Canterbury", "Gisborne", "Hawke's Bay", "Manawatu-Wanganui", "Marlborough", "Nelson", "Northland", "Otago"]
}

us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# 1. Supplier Table
suppliers = []
for _ in range(NUM_SUPPLIERS):
    country = random.choice(list(countries_and_states.keys()))
    state = random.choice(countries_and_states[country])
    suppliers.append({
        "supplier_id": _ + 1,
        "name": truncate_string(fake.company()),  # Ensure name is less than 50 characters
        "contact_number": generate_phone_number(),  # 10 digits not starting with 0
        "email": truncate_string(fake.unique.company_email()),  # Ensure email is less than 50 characters
        "address": state,  # Ensure address is less than 50 characters
        "country": country,  # Ensure country is less than 50 characters
        "supplier_rating": round(random.uniform(2.5, 5), 1)
    })

# 2. Equipment Table
equipment_types = ['Diagnostic', 'Surgical', 'Respiratory', 'Monitoring']
statuses = ['Available', 'In Use', 'Under Repair', 'Retired']
equipment = []
for i in range(NUM_EQUIPMENT):
    price = round(random.uniform(5000, 200000), 2)  # Price per unit
    equipment.append({
        "equipment_id": i + 1,
        "name": truncate_string(fake.catch_phrase()),  # Ensure name is less than 50 characters
        "type": random.choice(equipment_types),
        "manufacturer": truncate_string(fake.company()),  # Ensure manufacturer is less than 50 characters
        "purchase_date": random_date(datetime(2018, 1, 1), datetime(2024, 1, 1)),  # Adjusted for 6 years
        "warranty_expiration_date": random_date(datetime(2024, 1, 1), datetime(2029, 1, 1)),  # 5 years warranty
        "cost": price,
        "status": random.choice(statuses),
        "supplier_id": random.randint(1, NUM_SUPPLIERS)
    })

# 3. Warehouse Table
warehouses = []
manager_ids = []  # List to keep track of manager_ids
for i in range(NUM_WAREHOUSES):
    manager_id = random.randint(1, NUM_EMPLOYEES)  # Randomly choose a manager
    while manager_id in manager_ids:  # Ensure the manager_id is unique
        manager_id = random.randint(1, NUM_EMPLOYEES)

    manager_ids.append(manager_id)  # Add the chosen manager_id to the list

    warehouses.append({
        "warehouse_id": i + 1,
        "location": random.choice(us_states),  # Ensure location is less than 50 characters
        "capacity": random.randint(500, 2000),
        "current_inventory": random.randint(0, 1000),
        "manager_id": manager_id  # Assigning a unique manager_id
    })

# 4. Employee Table (Updated to include warehouse_id)
positions = ['Warehouse Manager', 'Logistics Coordinator', 'Supervisor', 'Technician']
employees = []
for i in range(NUM_EMPLOYEES):
    employees.append({
        "employee_id": i + 1,
        "name": truncate_string(fake.name()),  # Ensure name is less than 50 characters
        "position": random.choice(positions),
        "email": truncate_string(fake.unique.email()),  # Ensure email is less than 50 characters
        "contact_number": generate_phone_number(),  # 10 digits not starting with 0
        "warehouse_id": random.choice(warehouses)["warehouse_id"]  # Assigning a valid warehouse_id
    })

# 5. Hospital Table
hospitals = []
for i in range(NUM_HOSPITALS):
    hospitals.append({
        "hospital_id": i + 1,
        "name": truncate_string(fake.company() + " Hospital"),  # Ensure name is less than 50 characters
        "location": random.choice(us_states),  # Ensure location is less than 50 characters
        "department_name": truncate_string(random.choice(['Cardiology', 'Radiology', 'Emergency', 'Orthopedics'])),  # Ensure department name is less than 50 characters
        "contact_person": truncate_string(fake.name()),  # Ensure contact person name is less than 50 characters
        "contact_number": generate_phone_number(),  # 10 digits not starting with 0
    })

# 6. Orders Table
orders = []
order_dates = []  # List to store order dates for shipment reference

# Create order entries
for i in range(NUM_ORDERS):
    order_date = random_date(datetime(2018, 1, 1), datetime(2024, 1, 1))  # Adjusted for 6 years
    order_dates.append(order_date)  # Store the order date
    delivery_date = random_date(order_date, datetime(2024, 12, 31))  # Delivery date must be after order date

    # Assign status based on specified distribution
    rand_val = random.random()  # Generates a float between 0.0 to 1.0
    if rand_val < 0.3:
        status = 'Pending'
    elif rand_val < 0.9:
        status = 'Completed'
    else:
        status = 'Cancelled'

    orders.append({
        "order_id": i + 1,
        "order_date": order_date,
        "delivery_date": delivery_date,
        "status": status,
        "hospital_id": random.randint(1, NUM_HOSPITALS)
    })

# 7. Order_Details Table
order_details = []
for i in range(NUM_ORDER_DETAILS):
    order_id = random.randint(1, NUM_ORDERS)
    equipment_id = random.randint(1, NUM_EQUIPMENT)
    quantity = random.randint(1, 10)  # Random quantity for order details
    cost = next((eq['cost'] for eq in equipment if eq['equipment_id'] == equipment_id), 0)  # Fetch the cost of the equipment
    order_details.append({
        "order_detail_id": i + 1,
        "order_id": order_id,
        "equipment_id": equipment_id,
        "quantity": quantity,
        "total_cost": round(quantity * cost, 2)
    })

# 8. Inventory Table
inventory = []
for i in range(NUM_INVENTORY):
    equipment_id = random.randint(1, NUM_EQUIPMENT)
    warehouse_id = random.choice(warehouses)["warehouse_id"]  # Ensure the warehouse_id is valid
    quantity = random.randint(0, 100)  # Random quantity for inventory
    inventory.append({
        "inventory_id": i + 1,
        "equipment_id": equipment_id,
        "warehouse_id": warehouse_id,
        "quantity": quantity
    })

# 9. Shipments Table
shipments = []
for i in range(NUM_SHIPMENTS):
    order_id = random.randint(1, NUM_ORDERS)  # Ensure shipment is related to an existing order
    shipment_date = random_date(order_dates[order_id - 1], datetime(2024, 12, 31))  # Ensure shipment date is after the order date
    shipment_status = random.choice(['In Transit', 'Delivered', 'Returned'])
    shipments.append({
        "shipment_id": i + 1,
        "shipment_date": shipment_date,
        "shipment_status": shipment_status,
        "supplier_id": random.randint(1, NUM_SUPPLIERS),
        "warehouse_id": random.choice(warehouses)["warehouse_id"]  # Ensure the warehouse_id is valid
    })

# Convert lists to DataFrames
suppliers_df = pd.DataFrame(suppliers)
equipment_df = pd.DataFrame(equipment)
warehouses_df = pd.DataFrame(warehouses)
employees_df = pd.DataFrame(employees)
hospitals_df = pd.DataFrame(hospitals)
orders_df = pd.DataFrame(orders)
order_details_df = pd.DataFrame(order_details)
inventory_df = pd.DataFrame(inventory)
shipments_df = pd.DataFrame(shipments)

# Save DataFrames to CSV files
suppliers_df.to_csv('suppliers.csv', index=False)
equipment_df.to_csv('equipment.csv', index=False)
warehouses_df.to_csv('warehouses.csv', index=False)
employees_df.to_csv('employees.csv', index=False)
hospitals_df.to_csv('hospitals.csv', index=False)
orders_df.to_csv('orders.csv', index=False)
order_details_df.to_csv('order_details.csv', index=False)
inventory_df.to_csv('inventory.csv', index=False)
shipments_df.to_csv('shipments.csv', index=False)
