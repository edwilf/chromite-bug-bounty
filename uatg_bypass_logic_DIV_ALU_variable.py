
from typing import Dict, List, Union, Any
import random


class uatg_bypass_logic_DIV_ALU_variable():
	"""
	This class contains methods to generate and validate the tests bypass
	logic between DIV and ALU instructions
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
		With x24 being data dependent register, bypass logic is tested
		First DIV op is performed to check if x24 holds 5
		Result after sub instruction should indicate 4(5-1) for
		verifying bypass functioning 
		"""

		loop_count = 3
        
        # Load constants
		asm = "\n\tli x20,20 \n\tli x21,4 \n\tli x1,1"

        # DIV operation
		asm += "\n\tdiv x24,x20,x21 \n\n"
        
        # Loop through NOP instructions loop_count times(cycles)
		asm += f"\n\taddi t0, x0, {loop_count}\n\taddi t1,x0 ,0 \n\nloop:\n"
		asm += "\taddi t1, t1, 1\n\tblt t1, t0, loop\n"

        # ALU oPs
		asm += "\n\t sub x25,x24,x1"
		asm += "\n\t or x2,x3,x4"
		asm += "\n\t div x24,x20,x21"
        
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
