import os
from colorama import init, Fore
from answer_generator import parse_exe_answer, generate_exe_answer
from my_answer_generator import parse_jar_answer, generate_jar_answer


def get_all_files(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def print_info(test_path, error_exe, error_jar, exit_code):
    print("-------------------------------------------")
    print(Fore.RED + f"Тест не прошел {test_path}:\n"
                     f"Ожидаемые ошибки: {error_exe}\n"
                     f"Ошибка твоего решения: {error_jar}\n"
                     f"Exit code твоего решения: {exit_code}")
    print("-------------------------------------------")


def compare_results(type_tests):
    all_passed_tests = 0
    for test_path in type_tests:
        error_jar, exit_code = parse_jar_answer(generate_jar_answer(test_path))
        error_exe = parse_exe_answer(generate_exe_answer(test_path))

        if len(error_exe) == 0 and len(error_jar) == 0 and exit_code == 0:
            all_passed_tests += 1
        elif len(error_exe) == 0 and len(error_jar) == 0 and exit_code != 0:
            print_info(test_path, error_exe, error_jar, exit_code)
        elif len(error_exe) != 0 and len(error_jar) == 0 and exit_code == 0:
            print_info(test_path, error_exe, error_jar, exit_code)
        elif len(error_exe) == 0 and len(error_jar) != 0 and exit_code == 0:
            print_info(test_path, error_exe, error_jar, exit_code)
        elif len(error_jar) != 0 and len(error_exe) != 0 and exit_code != 0:
            if error_jar[0] in error_exe and exit_code == 1:
                all_passed_tests += 1
            elif error_jar[0] in error_exe and exit_code == 0:
                print_info(test_path, error_exe, error_jar, exit_code)
            else:
                print_info(test_path, error_exe, error_jar, exit_code)
        else:
            print_info(test_path, error_exe, error_jar, exit_code)
    return all_passed_tests


init(autoreset=True)

# TODO: Какая именно нужна неделя, если все нужны то просто нужно оставить пустую строку ""
current_week = r"\week-2"

all_files = get_all_files("tests" + current_week)

extra_tests = list(filter(lambda file: "extra" in file, all_files.copy()))
main_tests = list(filter(lambda file: "main" in file, all_files.copy()))

# TODO: Флаги какие тесты нужно проходить
main_tests_flag = True
extra_tests_flag = False

all_extra_tests = len(extra_tests)
all_main_tests = len(main_tests)

if main_tests_flag:
    all_passed_main_tests = compare_results(main_tests)

    print(Fore.GREEN + f"Passed {all_passed_main_tests}/{all_main_tests} main tests")

if extra_tests_flag:
    all_passed_extra_tests = compare_results(extra_tests)

    print(Fore.GREEN + f"Passed {all_passed_extra_tests}/{all_extra_tests} extra tests")
