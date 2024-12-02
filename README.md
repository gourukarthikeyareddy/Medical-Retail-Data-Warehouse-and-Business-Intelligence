# Medical-Retail-Data-Warehouse-and-Business-Intelligence

**1. Project Objective:**

This project aims to build a data warehouse for medical equipment supply and management. It will help
in managing inventory, processing orders, tracking equipment deliveries, monitoring warehouse stock, and assessing supplier
performance. The solution will reduce inefficiencies, prevent equipment shortages, and ensure timely deliveries.

#  

**2. Problem Statement:**

Hospitals and healthcare providers often face challenges such as delayed deliveries, poor equipment tracking,
overstocking, or understocking of critical medical supplies. Existing systems may lack real-time visibility into
equipment availability, supplier performance, or maintenance needs. This results in operational inefficiencies,
increased costs, and potential risks to patient care.
Key pain points include:

• Lack of real-time tracking of medical equipment inventory.

• Delayed response to restocking requests or equipment shortages.

• Inefficient supplier management and delivery tracking.

• Absence of comprehensive data-driven insights for better decision-making.

#  

**3. Proposed Solution:**

The proposed system will address these challenges by creating a centralized PostgreSQL database to manage the
supply and distribution of medical equipment. This will include:

• Inventory Management: Real-time tracking of equipment in various warehouses, with automated alerts for
restocking or shortages.

• Order Management: Streamlined order processing for hospitals and departments, with clear visibility into
order statuses (pending, shipped, delivered).

• Supplier Management: Monitoring supplier performance, ensuring compliance with contractual delivery
timelines and assessing quality.

• Shipment Tracking: Tracking and recording shipments to provide insights into delivery performance and
transit times.

#  
 
**4. Data Warehouse Tables:**



    |        Fact Tables            |      Dimension Tables   	|     Bridge Table     |
    ----------------------------------------------------------------------------------------
             Orders	                         Hospital	              Order_details     
            Inventory	                 Equipment         	                     
            Shipment	                 Warehouse	                              
	                                         Employee	                              
	                                         Suppliers	                              
	                                         Date	                                  
    ----------------------------------------------------------------------------------------

#  

**5. Conceptual Model:**

![conceptual design](https://github.com/user-attachments/assets/3cca0a2b-6733-4483-be5a-e0ecad83e62a)


#  

**6. Logical Model**
![logical design](https://github.com/user-attachments/assets/596ac1c2-c2df-403b-87ef-dbe8e11641d8)

#  

**7. Features**

**a. Slowly Changing Dimension 3 (SCD3):** 

Each record stores the previous value and the current value of the selected attribute. When the value of any chosen attribute changes, the current value is stored as the old value and the new value becomes the current value. In this project, I have implemented SCD3 to track employee positions and the warehouse an employee is assigned to.



![image](https://github.com/user-attachments/assets/8898c743-a9ba-47b2-877b-0d42d87bb2e0)




**b. Incremental Loading:**

Implemented incremental loading by comparing the source data with the data already present in the data warehouse enabling low-latency and low-cost data transfer.


![image](https://github.com/user-attachments/assets/aeb8b363-08fa-4860-988d-b5e82a89d90d)

