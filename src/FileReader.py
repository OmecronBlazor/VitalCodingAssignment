from PatientDemographic import PatientInfoList


def read_input(path):
    # Construct the Patient Demographic list
    patient_list = PatientInfoList()
    with open(path, encoding='utf8') as fp:
        for line in fp:
            # Add each line read from the input file to the list
            patient_list.add(line)

    return patient_list
