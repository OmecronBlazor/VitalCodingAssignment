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
        info = line.split(',')
        _id = info[0].rstrip()
        f_name, l_name, m_name = self.get_names(info[1])
        sex = info[2].rstrip()
        dob = info[3].rstrip()
        patient_info_obj = PatientInfo(_id, f_name, l_name, m_name, sex, dob, line.rstrip())

        name_key = f_name.lower() + "^" + l_name.lower()

        if name_key in self.patient_list:
            self.patient_list[name_key].append(patient_info_obj)
        else:
            self.patient_list[name_key] = [patient_info_obj]

    def get_names(self, names):
        name_list = names.split('^')
        return name_list[1].rstrip(), name_list[0].rstrip(), "" if len(name_list) < 3 else name_list[2].rstrip()

    def print_output(self):
        i = 0
        for patient_info in self.patient_list.values():
            itr_num = str(i) + ":"
            print(itr_num)
            i = i + 1
            for single_info in patient_info:
                print(single_info.out)

