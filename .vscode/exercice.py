from datetime import datetime
def create_contact():
    last_name = input("last name :")
    first_name = input("first name :")
    phone_number = input("phone number :")
    creation_date = datetime.today()
    nouveau_contact = {
        'last_name' : last_name,
        'first_name' : first_name,
        'phone_number' : phone_number,
        'creation_date' : creation_date,
        
    }
    return nouveau_contact