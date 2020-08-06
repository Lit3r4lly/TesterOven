from subprocess import Popen, PIPE

def test_inputs(inputs_list: list) -> str:
    """
    This function test the inputs with subprocess pipe
    :param inputs_list: the inputs list to test
    :return: the output
    :rtype: str
    """
    print("\n[+] TesterOven start the test session....")
    executable_file_path = input("[&] Enter executable file path to test: ")

    test_pipe = Popen(executable_file_path, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout_text, stderr_text = test_pipe.communicate(input=" ".join(inputs_list))

    print(f"\n[*] Inputs: \n{inputs_list} \n\n[$] Output: \n\n{stdout_text} \n\n[?] Output Errors: \n{stderr_text}")
    return stdout_text

def write_output_to_file(output: str) -> None:
    """
    This function writing the output to file
    :param output: the output
    """
    user_choice = input("[;] Would you like to write the output to file? (yes / no): ")

    if user_choice == 'yes':
        output_file_path = input("[&] Enter file path for writing the output: ")
        print(f"[@] Writing output to: \n\t{output_file_path}")

        with open(output_file_path, "w") as f:
            f.write(output)