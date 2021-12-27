from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic(IPlugin):
    """
    This class contains methods to generate and validate bypass logic between
    Load/Store instructions
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
        else:
            self.isa_bit = 'rv64'
            self.xlen = 64
        return True

    def generate_asm(self) -> Dict[str, str]:
        reg_file = base_reg_file.copy()
        test_dict = []

        """
        Load Contents pointed by x2 into x1
        Store contents pointed by x1 into x3
        If same values in x2 and x3, bypass logic works 
        """
        asm = "\n\tli x2,0x00000f44"
        asm += "\n\tlw x1,4(x2) \n\taddi x0,x0,0 \n\tsw x3,0(x1) \n\n"
        asm += "\n\tsw x4,0(x1) \n\taddi x0,x0,0 \n\tlw x3,0(x1) \n\n"
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
