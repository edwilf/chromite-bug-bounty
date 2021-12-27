from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic_DIV_MUL_variable(IPlugin):
    """
    This class contains methods to generate and validate the tests for
    correct functioning of bypass logic between MUL and DIV operations
    """

    def __init__(self) -> None:
        super().__init__()
        self.isa = 'RV32I'
        self.isa_bit = 'rv32'
        self.xlen = 32

    def execute(self, core_yaml, isa_yaml) -> bool:
        self.isa = isa_yaml['hart0']['ISA']
        if 'RV32' in self.isa:
            self.isa_bit = 'rv32'
            self.xlen = 32
        else:
            self.isa_bit = 'rv64'
            self.xlen = 64
        return True

    def generate_asm(self) -> Dict[str, str]:
        reg_file = base_reg_file.copy()
        test_dict = []

        asm = "\n\tli x20,4 \n\tli x21,3 \n\tli x19,2"              # Load Constants
        asm += "\n\tmul x24,x20,x21"                                # Perform MUL operation
        
        asm += f"\n\taddi t0, x0, {loop_count}\n\taddi t1,x0 ,0 \n\nloop:\n"        # Loop through {loop_count} cycles
        asm += "\taddi t1, t1, 1\n\tblt t1, t0, loop\n"
        asm += "\n\tdiv x18,x24,x19 \n\tadd x25,x31,x24 \n\n"       # Perform DIV operation to check if x18 holds 6 for correct bypass functioning
        
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
