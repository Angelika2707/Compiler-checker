import re
import subprocess


def interact_with_exe(exe_path, input_text):
    process = subprocess.Popen(
        [exe_path, "typecheck"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=input_text)

    if error:
        print(f"Ошибка: {error}")

    return output


def generate_exe_answer(input_file):
    with open(input_file, "r") as f:
        exe_path = "stella.exe"
        input_text = f.read()

        result = interact_with_exe(exe_path, input_text)

        return result


def parse_exe_answer(answer):
    error_tags = re.findall(r"Type Error Tag: \[(.*?)\]", answer)
    return error_tags
