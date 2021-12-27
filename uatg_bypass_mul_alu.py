from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic_mul_alu(IPlugin):
    """
    This class contains methods to generate and validate the bypass logic
    between MUL and ALU instructions.
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

        test_dict = []
        """
        Tests bypass from MUL to ALU operation with x24 as dependent register
        If x25 holds 14(2*5 + 4), then data dependency handled
        """
        asm = "\n\tli x20,2 \n\tli x21,5"      # Load Values
        asm += "\n\t li x1,4"
        asm += "\n\tmul x24,x20,x21 \n\n"       # Perform MUL operation
        asm += "\n\taddi x0,x0,0"               # One cycle NOP
        asm += "\n\t sub x25,x24,x1"            # Perform ALU OP with x24 as
                                                # dependent register
        asm += "\n\t or x2,x3,x4"               
        asm += "\n\t mul x24,x20,x21"
        
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
