# Step 1: Define the Contact and Lead classes
class Contact:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Contact(Name: {self.name}, Email: {self.email}, Phone: {self.phone})"


class Lead:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Lead(Name: {self.name}, Email: {self.email}, Phone: {self.phone})"


# Step 2: Create initial ContactsList and LeadsList
contacts_list = [
    Contact("Alice Brown", None, "1231112223"),
    Contact("Bob Crown", "bob@crowns.com", None),
    Contact("Carlos Drew", "carl@drewess.com", "3453334445"),
    Contact("Doug Emerty", None, "4564445556"),
    Contact("Egan Fair", "eg@fairness.com", "5675556667")
]

leads_list = [
    Lead(None, "kevin@keith.com", None),
    Lead("Lucy", "lucy@liu.com", "3210001112"),
    Lead("Mary Middle", "mary@middle.com", "3331112223"),
    Lead(None, None, "4442223334"),
    Lead(None, "ole@olson.com", None)
]

# Step 3: Define a function to process registrants (based on JSON data)
def process_registrant(registrant_json, contacts_list, leads_list):
    name = registrant_json["registrant"]["name"]
    email = registrant_json["registrant"]["email"]
    phone = registrant_json["registrant"]["phone"]

    # 1. Match by email in Contacts
    for contact in contacts_list:
        if contact.email == email:
            # Update if fields are missing
            if not contact.phone:
                contact.phone = phone
            if not contact.name:
                contact.name = name
            print(f"Updated existing contact by email: {contact}")
            return

    # 2. Match by phone in Contacts
    for contact in contacts_list:
        if contact.phone == phone:
            # Update if fields are missing
            if not contact.email:
                contact.email = email
            if not contact.name:
                contact.name = name
            print(f"Updated existing contact by phone: {contact}")
            return

    # 3. Match by email in Leads, if found remove from Leads and add to Contacts
    for lead in leads_list:
        if lead.email == email:
            leads_list.remove(lead)
            new_contact = Contact(name or lead.name, email, phone or lead.phone)
            contacts_list.append(new_contact)
            print(f"Moved from leads to contacts by email: {new_contact}")
            return

    # 4. Match by phone in Leads, if found remove from Leads and add to Contacts
    for lead in leads_list:
        if lead.phone == phone:
            leads_list.remove(lead)
            new_contact = Contact(name or lead.name, email or lead.email, phone)
            contacts_list.append(new_contact)
            print(f"Moved from leads to contacts by phone: {new_contact}")
            return

    # 5. If no match found, add as a new contact
    new_contact = Contact(name, email, phone)
    contacts_list.append(new_contact)
    print(f"Added new contact: {new_contact}")

# Step 4: Process each registrant
registrants = [
    {"registrant": {"name": "Lucy Liu", "email": "lucy@liu.com", "phone": None}},
    {"registrant": {"name": "Doug", "email": "doug@emmy.com", "phone": "4564445556"}},
    {"registrant": {"name": "Uma Thurman", "email": "uma@thurs.com", "phone": None}}
]

for registrant in registrants:
    process_registrant(registrant, contacts_list, leads_list)

# Step 5: Print final contacts and leads lists to verify
print("\nFinal Contacts List:")
for contact in contacts_list:
    print(contact)

print("\nFinal Leads List:")
for lead in leads_list:
    print(lead)

