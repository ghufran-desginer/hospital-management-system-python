from abc import ABC, abstractmethod


print("=" * 60)
print("     NIZAM AL-MUSTASHFA - HOSPITAL MANAGEMENT SYSTEM     ")
print("=" * 60)


class HospitalInfo:
    #  سمة كلاس (Class Attribute) تشترك فيها جميع المئيلات
    hospital_name = "ALSHEFAA hospital"


    @classmethod
    def get_hospital_name(cls):
        return cls.hospital_name


    @staticmethod
    def validate_phone(phone_num):
        return phone_num.isdigit() and len(phone_num) == 9  and phone_num.startswith('7')


class Appointment:
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def get_details(self):
        return f"Date: {self.date}, Time: {self.time}"


class MedicalRecord:
    def __init__(self, record_id, diagnosis):
        self.record_id = record_id
        self.diagnosis = diagnosis

    def get_info(self):
        return f"Record ID: {self.record_id}, Diagnosis: {self.diagnosis}"

class Person(ABC):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.__phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @abstractmethod
    def show_rol(self):
        pass


class Doctor(Person):
    def __init__(self, name, age, phone, doc_id, Spechilizaition):
        super().__init__(name, age, phone)
        self.doc_id = doc_id
        self.Spechilizaition = Spechilizaition

    def show_rol(self):
        print(f"Role: Doctor  | Name: {self.name} | Age: {self.age} | Phone: {self.phone} | Doc ID: {self.doc_id} |doctor major:{self.Spechilizaition}")

class Nurse(Person):
    def __init__(self, name, age, phone, nur_id,duty_shift):
        super().__init__(name, age, phone)
        self.nur_id = nur_id
        self.duty_shift = duty_shift

    def show_rol(self):
        print(f"Role: Nurse   | Name: {self.name} | Age: {self.age} | Phone: {self.phone} | Nurse ID: {self.nur_id} | Nurse shift:{self.duty_shift}")

class Patient(Person):
    def __init__(self, name, age, phone, patient_id,gender,BirthDate ,record_id,diagnosis):
        super().__init__(name, age, phone)
        self.patient_id = patient_id
        self.gender = gender
        self.BirthDate = BirthDate
        self.medical_record = MedicalRecord(record_id, diagnosis)
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_rol(self):
        print(
            f"Role: Patient | Name: {self.name} | Age: {self.age} | Phone: {self.phone} | Patient ID: {self.patient_id} |Gender:{self.gender} | BirthDate:{self.BirthDate}")

        if self.medical_record:
            print(f"  [Medical Record]: {self.medical_record.get_info()}")
        else:
            print("  [Medical Record]: No medical record")
        if self.appointments:
            print("  [Appointments]:")
            for app in self.appointments:
                print( {app.get_details()})
        else:
            print("  [Appointments]: NO appointments")


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def show_department_info(self):
        print(f"\nDepartment: {self.dept_name}")
        if self.doctors:
            print("Doctors in Department:")
            for doc in self.doctors:
                doc.show_rol()
        else:
            print("No doctors assigned to this department.")


# ---  دوال عادية خارج الفئات (Standalone Functions) ---

def display_person_info(person_object):
    person_object.show_rol()

def print_welcome_message():
    print(f"\nWELLCOME TO {HospitalInfo.get_hospital_name()}")

def format_id(id_number):
    return f"ID-NUMBER: {id_number}"


# ---  هياكل البيانات (تجميع البيانات) ---
# 1. المجموعات (Sets) لتخزين أرقام الهواتف الفريدة
unique_phones = set()

# 2. القواميس (Dictionaries) لتخزين بيانات الأطباء برقم الـ ID
doctors_dict = {}
nurse_dict = {}
patient_dict = {}

# 3. الصفوف (Tuples) لتخزين بيانات ثابتة مثل ساعات العمل
working_hours = ("08:00 AM", "04:00 PM")


print_welcome_message()

cardiology = Department("Cardiology")
doctors_list = []

surgery = Department("surgery")
hee = Department("hee")

while True:
    print("\n--- Enter Doctor Details ---")
    doc_name = input("Please enter doctor name: ")
    doc_age = int(input("Please enter doctor age: "))

    # استخدام الـ staticmethod للتحقق من الهاتف
    while True:
        doc_phone = input("Please enter doctor phone: ")
        if HospitalInfo.validate_phone(doc_phone):
            break
        print("Wrong phone number  try again.")


    doc_id = int(input("Please enter doctor id: "))
    doc_spe=input("Please enter doctor specification: ")

    doc = Doctor(doc_name, doc_age, doc_phone, doc_id,doc_spe)
    cardiology.add_doctor(doc)
    doctors_list.append(doc)

    # إضافة للهياكل الجديدة (Set & Dictionary)
    unique_phones.add(doc_phone)
    doctors_dict[doc_id] = doc_name


    add_more = input("Do you want to add another doctor? (yes/no): ").strip().lower()
    if add_more != 'yes':
        break

print("\n--- Enter Nurse Details ---")
nur_name = input("Please enter nurse name: ")
nur_age = int(input("Please enter nurse age: "))

while True:
    nur_phone = input("Please enter nurse phone: ")
    if HospitalInfo.validate_phone(nur_phone):
        break
    print("Wrong phone number  try again.")


nur_id = int(input("Please enter nurse id: "))
nur_shift=input("pleas enter nurse duty shift: ")
nurse = Nurse(nur_name, nur_age, nur_phone, nur_id,nur_shift)
unique_phones.add(nur_phone)
nurse_dict[nur_id] = nur_name
format_id(nur_id)

print("\n--- Enter Patient Details ---")
pat_name = input("Please enter patient name: ")
pat_age = int(input("Please enter patient age: "))

while True:
    pat_phone = input("Please enter patient phone: ")
    if HospitalInfo.validate_phone(pat_phone):
        break
    print("Wrong phone number  try again.")

pat_id = int(input("Please enter patient id: "))
pat_gen=input("Please enter patient gender: ")
pat_BD=input("Please enter patient birth date: ")
unique_phones.add(pat_phone)
patient_dict[pat_id] = pat_name
pat_re=input("Please enter patient record id: ")
pat_diag=input("Please enter patient diagnosis: ")
patient = Patient(pat_name, pat_age, pat_phone, pat_id,pat_gen,pat_BD,pat_re, pat_diag)

while True:
    add_app = input("\nDo you want to add an appointment for this patient? (yes/no): ").strip().lower()
    if add_app == 'yes':
        app_date = input("Enter appointment date (e.g., 2026-04-01): ")
        app_time = input("Enter appointment time (e.g., 10:00 AM): ")
        app = Appointment(app_date, app_time)
        patient.add_appointment(app)
    else:
        break

print("\n Testing Polymorphism ")
people = []
people.extend(doctors_list)
people.append(nurse)
people.append(patient)

for p in people:
    display_person_info(p)

print("\n Testing Aggregation & Composition ")
cardiology.show_department_info()
surgery.show_department_info()
hee.show_department_info()

print("\n--- show set,dic,tuple ---")
print("unique numbers (Set):", unique_phones)
print("doctors dictionary (Dictionary):", doctors_dict)
print("working hours (Tuple):", working_hours)
print(format_id(nur_id))
x=Doctor('ghufran',21,88777,2,'gg')
x.show_rol()