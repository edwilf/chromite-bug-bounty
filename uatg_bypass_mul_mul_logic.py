from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_mul_mul_logic(IPlugin):
    """
    This class contains methods to generate and validate the tests for bypassing from one 
    MUL instruction to another.
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

    
    def generate_asm(self) -> Dict[str, str]:
        reg_file = base_reg_file.copy()
        test_dict = []

        loop_count = 3
        asm = "\n\tmul x24,x20,x21 \n\n"
        asm += f"\n\taddi t0, x0, {loop_count}\n\taddi t1,x0 ,0 \n\nloop:\n"
        asm += "\taddi t1, t1, 1\n\tblt t1, t0, loop\n"
        asm += "\n\t mul x25,x24,x1"
        
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
