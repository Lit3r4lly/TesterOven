# Created by Lit3r4lly
import CliHandler
import TesterHandler

def manage_tester_oven() -> None:
    """
    This function manage the whole tester process
    """
    tester_handler = TesterHandler.TesterOvenHandler()
    cli_handler = CliHandler.CliAppHandler()
    user_choice = int(input("\n1 - Test inputs - Enter inputs, test your executable file and export the inputs and the outputs to files\n2 - Import test - Import old tested inputs according to option (1) from the inputs (json) file\n3 - Append inputs - Append new inputs to test to old tested inputs according to option (1) to the inputs (json) file\nYour choice: "))

    if user_choice == 1:
        inputs_list = cli_handler.get_inputs()
        output = tester_handler.test_inputs(inputs_list)

        user_choice = input("[;] Would you like to write the tested inputs to file for easy importing test section? (yes / no): ")
        if user_choice == 'yes':
            file_path = input("\n[#] Enter file path (json) for saving the tested inputs: ")
            cli_handler.export_inputs(inputs_list, file_path)

    elif user_choice == 2:
        file_path = input("\n[#] Enter inputs file path (json) for importing old tested inputs: ")

        inputs_list = cli_handler.import_inputs(file_path)
        output = tester_handler.test_inputs(inputs_list)

    elif user_choice == 3:
        file_path = input("\n[#] Enter file path (json) for appending new inputs to old tested inputs: ")
        
        inputs_list = cli_handler.append_inputs(file_path)
        output = tester_handler.test_inputs(inputs_list)

    tester_handler.write_output_to_file(output)
    print("Finished.")

if __name__ == "__main__":
    manage_tester_oven()