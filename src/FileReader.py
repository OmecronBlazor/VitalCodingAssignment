import PatientDemographic


def read_input(path):
    patient_list = PatientDemographic.PatientInfoList()
    with open(path, encoding='utf8') as fp:
        for line in fp:
            patient_list.add(line)

    return patient_list