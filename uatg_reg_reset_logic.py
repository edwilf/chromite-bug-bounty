from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_reg_reset_logic(IPlugin):
    """
    This class contains methods to generate and validate the tests for
    reset of register file.
    """

    def __init__(self) -> None:
        super().__init__()
        self.isa = 'RV32I'
        self.isa_bit = 'rv32'
        self.offset_inc = 4
        self.xlen = 32
        self.num_rand_var = 100

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.isa = isa_yaml['hart0']['ISA']
        if 'RV32' in self.isa:
            self.isa_bit = 'rv32'
            self.xlen = 32
            self.offset_inc = 4
        else:
            self.isa_bit = 'rv64'
            self.xlen = 64
            self.offset_inc = 8
        return True

    def generate_asm(self) -> List[Dict[str,Union[Union[str, List[Any]], Any]]]:
        reg_file = base_reg_file.copy()
        test_dict = []
	""" We would check the register x0 and x1 for equality.
	The for loop is used to perform the or operation of register x1 with all the remaining 		registers.
	"""
        asm_code = "\n\tbne x1,x0,LOC"
        for rs in reg_file:
            asm_code += f'\n\tor x1,x1,{rs}'
        asm_code += "\n\nLOC:\n"
        asm_code += "\tslt x1,x1,x0"
        compile_macros = []

        test_dict.append({
            'asm_code': asm,
            'asm_sig' : '',
            'compile_macros': compile_macros,
            })


        return test_dict

    def check_log(self, log_file_path, reports_dir) -> bool:
        return False

    def generate_covergroups(self, config_file) -> str:
        sv = ""
        return sv
