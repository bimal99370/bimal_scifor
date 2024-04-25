class Patient:
    def __init__(self, patient_id, patient_name, disease, doctor_incharge):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.disease = disease
        self.doctor_incharge = doctor_incharge

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Patient Name: {self.patient_name}, Disease: {self.disease}, Doctor Incharge: {self.doctor_incharge}"

class RainbowHospital:
    def __init__(self):
        self.patients = []

    def admit_patient(self, patient_id, patient_name, disease, doctor_incharge):
        new_patient = Patient(patient_id, patient_name, disease, doctor_incharge)
        self.patients.append(new_patient)
        print("Patient admitted successfully!")

    def get_patient(self, search_key, search_value):
        found_patients = [patient for patient in self.patients if getattr(patient, search_key) == search_value]
        return found_patients

    def show_all_patients(self):
        if not self.patients:
            print("No patients in the hospital.")
        else:
            for patient in self.patients:
                print(patient)

    def discharge_patient(self, search_key, search_value):
        patients_to_remove = self.get_patient(search_key, search_value)
        if not patients_to_remove:
            print("No matching patient found.")
        else:
            for patient in patients_to_remove:
                self.patients.remove(patient)
            print("Patient discharged successfully!")

# Main program
rainbow_hospital = RainbowHospital()

while True:
    print("\nOptions:")
    print("1. Admit a new patient")
    print("2. Get a patient")
    print("3. Show all patients")
    print("4. Discharge a patient")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        patient_name = input("Enter Patient Name: ")
        disease = input("Enter Disease: ")
        doctor_incharge = input("Enter Doctor Incharge: ")
        rainbow_hospital.admit_patient(patient_id, patient_name, disease, doctor_incharge)

    elif choice == "2":
        search_key = input("Enter search key (patient_id/patient_name/disease/doctor_incharge): ")
        search_value = input(f"Enter {search_key} to search for: ")
        found_patients = rainbow_hospital.get_patient(search_key, search_value)
        if found_patients:
            for patient in found_patients:
                print(patient)
        else:
            print("No matching patient found.")

    elif choice == "3":
        rainbow_hospital.show_all_patients()

    elif choice == "4":
        search_key = input("Enter search key (patient_id/patient_name/disease/doctor_incharge) for patient to discharge: ")
        search_value = input(f"Enter {search_key} to search for: ")
        rainbow_hospital.discharge_patient(search_key, search_value)

    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
