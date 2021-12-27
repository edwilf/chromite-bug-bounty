from yapsy.IPlugin import IPlugin
from uatg.instruction_constants import base_reg_file, arithmetic_instructions,\
    bit_walker
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic_LOAD_ALU_variable(IPlugin):
    """
    This class contains methods to generate and validate bypass
    from Load/Store instructions to ALU instructions with variable depth
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


    def generate_asm(self) -> List[Dict[str,Union[Union[str, List[Any]], Any]]]:
        reg_file = base_reg_file.copy()
        test_dict = []

        loop_count = 2

        asm = "\n\tli x19,4"
        # Perform load store operation
        asm += "\n\tli t1, 1 \n\tsw t1, 0(s0) \n\tlw x18,0(s0)"

        asm += f"\n\taddi t0, x0, {loop_count}\n\taddi t1,x0 ,0 \n\nloop:\n"
        asm += "\taddi t1, t1, 1\n\tblt t1, t0, loop\n"

        # Use data dependent reigster x18 to test if x17 holds 5(4+1)
        # to verify correct bypass logic functioning
        asm += "\n\tadd x17,x18,x19 \n\tor x22,x20,x17 \n\n"
        
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
