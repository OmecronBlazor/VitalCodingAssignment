from dataclasses import dataclass


@dataclass
class PatientInfo:
    _id: str
    first_name: str
    last_name: str
    middle_name: str
    sex: str
    date_of_birth: str
    out: str

    def __init__(self, _id: str, f_name: str, l_name: str, m_name: str, sex: str, date_of_birth: str, out: str):
        self._id = _id
        self.first_name = f_name
        self.last_name = l_name
        self.middle_name = m_name
        self.date_of_birth = date_of_birth
        self.out = out


class PatientInfoList:
    def __init__(self):
        self.patient_list = {}

    def add(self, line):
        # Split each line by the comma delimiter
        info = line.split(',')

        # Extract each piece of info, assuming input is valid and remove any potential leading/trailing whitespace
        _id = info[0].strip()

        # Split and extract the first, last, and optional middle name by the '^' delimiter
        f_name, l_name, m_name = self.get_names(info[1])
        sex = info[2].strip()
        dob = info[3].strip()

        # Populate the info object with the extracted information
        patient_info_obj = PatientInfo(_id, f_name, l_name, m_name, sex, dob, line)

        # The key for each element in the hash table will be in the format '<last_name>^<first_name>' all lowercase
        # This will resolve the scenario for grouping patient info with the same name with lower/upper case characters
        name_key = l_name.lower() + "^" + f_name.lower()

        # Add the info object to the hash table given the key where the value will be a list of info objects
        if name_key in self.patient_list:
            self.patient_list[name_key].append(patient_info_obj)
        else:
            self.patient_list[name_key] = [patient_info_obj]

    def get_names(self, names):
        name_list = names.split('^')
        return name_list[1].strip(), name_list[0].strip(), "" if len(name_list) < 3 else name_list[2].strip()

    def print_output(self):
        # Print the output with each patient info grouped by the patient name as desired
        i = 0
        for patient_info in self.patient_list.values():
            itr_num = str(i) + ":"
            print(itr_num)
            i = i + 1
            for single_info in patient_info:
                print(single_info.out)

    # Methods below are for the purpose of testing #
    def clear(self):
        self.patient_list.clear()

    def len(self):
        return len(self.patient_list)

    def exists(self, key):
        return key in self.patient_list

    def get(self, key):
        return [] if key not in self.patient_list else self.patient_list[key]
