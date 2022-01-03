
from typing import Dict, List, Union, Any
import random


class uatg_bypass_pipeline_flush():

	"""
	This class contains methods to generate and validate the tests for bypass from
	2 operations while performing a pipieline flush in between
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
		Perform a store operation and then flush the pipeline
		s0 is data dependent register
		Load performed after pipeline flush
		"""
        
		test_dict = []
		asm = "\n\tli t1, 1 \n\t sw t1, 0(s0) \n\taddi x0,x0,0"     # Store t1 contents into location pointed by s0
		asm += "\n\t fence.i"                                       # Perform pipeline flush
		asm += "\n\t lw a0,0(s0)"                                   # Load contents pointed by s0
        
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



