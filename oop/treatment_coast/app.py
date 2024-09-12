##pass  Программа создает объекты пациента и его пройденных процедур

## Импорт классов из модулей
from patient import Patient
from procedure import Procedure

data_patient = {'first_name':'Luck', 'last_name':'Skywalker', 'patronymic': 'Dartovich', 'city':'New-York;', 'region':'57', 'postal_code':'302000','phone_number_person':'+79602345233', 'contact_name':'Dart Wader', 'contact_phone_number':'+79531312341'}

procedures = {1 : {'name_procedure':'medical check-up', 'date':'this day', 'doctor':'Irvish', 'price':250.00}, 
              2 : {'name_procedure':'radiography', 'date':'this day', 'doctor':'Jamison', 'price':500.00},
              3 : {'name_procedure':'blood test', 'date':'this day', 'doctor':'Smit', 'price':200.00}}



def main():
    #print(data_patient['first_name'])
    dict_object_procedures = {} 
    ##create object patient
    object_patient = Patient(
            data_patient['first_name'],
            data_patient['last_name'],
            data_patient['patronymic'],
            data_patient['city'],
            data_patient['region'],
            data_patient['postal_code'],
            data_patient['phone_number_person'],
            data_patient['contact_name'],
            data_patient['contact_phone_number']
            )
            
    show_data_patient(object_patient)
    print()
    ## Create the tree objects 
    for key in procedures:    
        object_procedure = Procedure(
            procedures[key]['name_procedure'],
            procedures[key]['date'],
            procedures[key]['doctor'],
            procedures[key]['price']
            )
        dict_object_procedures[key] = object_procedure
    
    show_data_procedure(dict_object_procedures)


    #create_object_procedure(
    #show_data_procedures(procedures) 

def show_data_procedure(objects):
    for number in objects:
        #print(objects[key].get_procedure_name())
        print()
        print()
        print('-------------------------------------------')
        print(f'Procedure №{number}')
        print('-------------------------------------------')
        print(f'Name procedure: {objects[number].get_procedure_name()}')
        print('-------------------------------------------')
        print(f'Date: {objects[number].get_date()}')
        print('-------------------------------------------')
        print(f'Doctor name: {objects[number].get_doctor_name()}')
        print('-------------------------------------------')
        print(f'Cost: {objects[number].get_procedure_cost()}')
        print('-------------------------------------------')
        print()
    

def show_data_patient(object_patient):
    ##print info about patient
    print('------------------------------------')
    print('____________PATIENT_________________')
    print()
    print('Patient name')
    print(f'first name: {object_patient.get_name()[0]} ||',
          f'last name: {object_patient.get_name()[1]} ||',
          f'patronymic: {object_patient.get_name()[2]}')
    print()
    print('Address')
    print(f'city: {object_patient.get_address()[0]} ||',
          f'region: {object_patient.get_address()[1]} ||',
          f'postal code: {object_patient.get_address()[2]}')
    print()
    print(f'Phone number: {object_patient.get_phone_number_person()}')
    print()
    print('Contact person')
    print(f'contact name: {object_patient.get_contact()[0]} ||',
          f'contant phone: {object_patient.get_contact()[1]}')
    print()




if __name__ == '__main__':
    main()
