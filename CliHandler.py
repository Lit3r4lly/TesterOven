import json

TESTER_OVEN = """
████████╗███████╗███████╗████████╗███████╗██████╗        ██████╗ ██╗   ██╗███████╗███╗   ██╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗      ██╔═══██╗██║   ██║██╔════╝████╗  ██║
   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝█████╗██║   ██║██║   ██║█████╗  ██╔██╗ ██║
   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗╚════╝██║   ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
   ██║   ███████╗███████║   ██║   ███████╗██║  ██║      ╚██████╔╝ ╚████╔╝ ███████╗██║ ╚████║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝ """

class CliAppHandler:
    def __init__(self) -> None:
        print(TESTER_OVEN)
        print("Hello, welcome to TesterOven. \nSimple testing system for executable files.")
        print("All you need to do is to follow the instructions according to the chosen option in the next menu.")

    def get_inputs(self) -> list:
        """
        This function gets the input for the tests
        :return: list of the tested inputs
        :rtype: list
        """
        i = 0
        flag = True
        inputs_list = []

        print("\nEnter the inputs by order (One each time), and press ctrl+c when you want to stop insert the inputs.")
        while flag:
            try:
                i += 1
                tested_input = input(f"[#] Input {i}: ")
                inputs_list.append(tested_input)

            except KeyboardInterrupt:
                print(f"[A{'' * len(tested_input)}\033[A") # clear last output line
                print(f"\n[&] New tested inputs list: \n\t{inputs_list}")

                flag = False

        return inputs_list

    def import_inputs(self, file_path: str) -> list:
        """
        This function import the tested inputs from the file
        :return: list of the tested inputs
        :rtype: list
        """
        with open(file_path, "r") as f:
            file_content = f.read()
            inputs_list = json.loads(file_content)
            
        return inputs_list
        

    def export_inputs(self, inputs: list, file_path: str):
        """
        This function export the tested inputs into file
        :param inputs: The tested inputs for the testing
        :inputs type: list
        """
        with open(file_path, "w") as f:
            json.dump(inputs, f)

        print(f"[&] Inputs has been expotred to : \n\t{file_path}")

    def append_inputs(self, file_path: str) -> None:
        """
        This function append new inputs to the tested inputs list
        :param inputs: The tested inputs for the testing
        :inputs type: list
        """
        new_tested_inputs = self.get_inputs()
        current_tested_inputs = self.import_inputs(file_path)

        for tested_input in new_tested_inputs:
            current_tested_inputs.append(tested_input)

        self.export_inputs(current_tested_inputs, file_path)

        return current_tested_inputs