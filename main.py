from openapi_spec_validator.readers import read_from_filename
from openapi_spec_validator import openapi_v30_spec_validator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spec_dict, spec_url = read_from_filename('C:\\Users\\sucke\\PycharmProjects\\pythonProject\\venv\\openapi.yaml')
    # If no exception is raised by validate_spec(), the spec is valid.
    try:
        errors_iterator = openapi_v30_spec_validator.iter_errors(spec_dict)
        for item in errors_iterator:
            print(item)

    except Exception as e:
        print(e)
