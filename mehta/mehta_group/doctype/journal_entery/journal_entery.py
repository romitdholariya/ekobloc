
import frappe
from frappe import _, msgprint, scrub

@frappe.whitelist()
def get_party_name(party_type, party, cost_center=None):
    try:
        frappe.log_error(f"Debug: party_type={party_type}, party={party}", "get_party_name")
        
        if party_type == 'Customer':
            party_name = frappe.db.get_value('Customer', party, 'customer_name')
        elif party_type == 'Supplier':
            party_name = frappe.db.get_value('Supplier', party, 'supplier_name')
        else:
            party_name = None
        
        frappe.log_error(f"Debug: party_name={party_name}", "get_party_name")
        
        return party_name
    except Exception as e:
        frappe.log_error(f"Error: {e}", "get_party_name")
        raise


# @frappe.whitelist()
# def get_cust_party_name(party_type, party, cost_center=None):
#     if party_type == "Customer":
#         party_name = frappe.db.get_value('Customer', party, 'customer_name')
#     elif party_type == 'Supplier':
#         party_name = frappe.db.get_value('Supplier', party, 'supplier_name')

#     return party_name
    
    


