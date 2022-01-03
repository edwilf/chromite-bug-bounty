
from uatg.instruction_constants import base_reg_file
from typing import Dict, List, Union, Any
import random


class uatg_reg_reset_logic():
	"""
	This class contains methods to generate and validate the tests for
	reset of register file.
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
		""" 
		Checks the reset values of registers
		Method similar to OR Reduction
		Iteratively OR contents of the registers
		in register file and test if 0 at the end
		"""
		reg_file = base_reg_file.copy()
		test_dict = []
	
		asm_code = "\n\tbne x1,x0,LOC"		# Check if x1 is 0 and if yes, use a sum register
		for rs in reg_file:
			asm_code += f'\n\tor x1,x1,{rs}'	# Perform OR Reduction
		asm_code += "\n\nLOC:\n"
		asm_code += "\txor x1,x1,x0"		# Test if final value is 0
		compile_macros = []			# If all registers reset, final value of x1 is 0

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
