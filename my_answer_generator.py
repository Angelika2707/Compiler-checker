import re
import subprocess


def interact_with_jar(jar_path, input_text):
    process = subprocess.Popen(
        ["java", "-jar", jar_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=input_text)
    exit_code = process.returncode

    return output, error, exit_code


def generate_jar_answer(input_file):
    with open(input_file, "r") as f:
        jar_path = "solution.jar"
        input_text = f.read()

        result, error, exit_code = interact_with_jar(jar_path, input_text)

        return result, error, exit_code


def parse_jar_answer(answer):
    error_tags = re.findall(r"java\.lang\.RuntimeException: (\S+)", answer[1])
    return error_tags, answer[2]


# print(parse_jar_answer(generate_jar_answer("1.stella")))
