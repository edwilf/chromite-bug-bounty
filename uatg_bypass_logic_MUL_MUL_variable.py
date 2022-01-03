
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic_MUL_MUL_variable():
	"""
	This class contains methods to generate and validate the bypass logic between
	2 MUL operations with variable instructions in between
	"""

	def __init__(self) -> None:
		super().__init__()
		self.isa = 'RV32I'
		self.isa_bit = 'rv32'

	def execute(self, core_yaml, isa_yaml) -> bool:
		self.isa = isa_yaml['hart0']['ISA']
		if 'RV32' in self.isa:
			self.isa_bit = 'rv32'

		else:
			self.isa_bit = 'rv64'

		return True

    
	def generate_asm(self) -> Dict[str, str]:

		test_dict = []

		loop_count = 3

        # Load Constants
		asm = "\n\tli x20,4 \n\tli x21,2 \n\tli x1,2"

        # Perform first MUL operation and store in data 
        # dependent register x24
		asm += "\n\tmul x24,x20,x21 \n\n"

        # Loop through {loop_count} cycles
		asm += f"\n\taddi t0, x0, {loop_count}\n\taddi t1,x0 ,0 \n\nloop:\n"
		asm += "\taddi t1, t1, 1\n\tblt t1, t0, loop\n"

        # Perform second MUL op using data dependent register x24
        # If value held in x25 is 16(4*2*2), bypass logic verified
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
