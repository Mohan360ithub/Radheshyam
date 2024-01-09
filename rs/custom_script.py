import frappe

@frappe.whitelist()
def get_customer_by_sales_person(sales_person=None):
    # Your logic to fetch the customer based on the sales person
    # Replace 'Customer' with the actual doctype you want to query
    customer_records = frappe.get_all('Customer', filters={'sales_person': sales_person}, fields=['name'])
    
    # Extract the customer names from the records
    customer_names = [customer.get('name') for customer in customer_records]

    return customer_names

