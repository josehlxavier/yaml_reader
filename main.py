from openapi_spec_validator.readers import read_from_filename
from openapi_spec_validator import openapi_v30_spec_validator
import argparse
import re

def oasReader(file_path):
    spec_dict, spec_url = read_from_filename(file_path)
    # If no exception is raised by validate_spec(), the spec is valid.
    try:
        errors_iterator = openapi_v30_spec_validator.iter_errors(spec_dict)
        if errors_iterator:
            print("Arquivo: " + str(file_path))
            for item in errors_iterator:
                print(item)
    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=" Script responsável pela leitura\
                                                   de OAS e detecção de incrongruências. \
                                                   Pode receber o path para um arquivo com o parametro '-p'\
                                                   Ou um arquivo com o parametro '-f'. Caso seja enviado um arquivo\
                                                   o mesmo precisa ter os paths para os arquivos separados por ';' ")
    parser.add_argument("-p","--path", help="Path completo para o arquivo que serão validados", type=str)
    parser.add_argument("-f","--file", help="Path para arquivo .csv contendo uma lista com todos os\
                                            paths para os arquivos a serem validados")
    args = vars(parser.parse_args())
    if args['path'] and args['file']:
        raise TypeError('Não é possível receber os dois parametros ao mesmo tempo')

    if args['path']:
        oasReader(args['path'])

    if args['file']:
        import csv
        with open(args['file'], 'r') as file:
            csvreader = csv.reader(file, delimiter=";")
            for row in csvreader:
                for line in row:
                    oasReader(line)
                    print(" \n ")