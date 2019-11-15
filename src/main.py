import FileReader
import PatientDemographic

path = '../input/input.txt'


def main():
    patient_list = FileReader.read_input(path)
    patient_list.print_output()


if __name__ == "__main__":
    main()