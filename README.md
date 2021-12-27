# chromite-bug-bounty
chromite-bug-bounty special topic coursework

This repository consists of python scripts to generate RISC-V assembly for testing the Regfile + Bypass + Scoreboard in the Chromite core developed by incore semiconductors

The Register file is a part of the decode stage in the pipeline. It consists of 32 registers, each of 32 bit width if the architecture supported by core is RV32. There are 2 read ports and 1 write port. More information regarding the register file is given [here](https://chromite.readthedocs.io/en/using-csrbox/chromite.html#register-file).

Bypass logic: It is introduced to solve data hazards. Data dependencies between subsequent instructions can lead to lower performance due to the necessity of stalls to ensure program integrity.This method involves adding multiplexers in front of the ALU

Scoreboarding: In its minimal configuration implements a 32-bit register for each architectural register file .Each bit in this register corresponds to a register in the respective register file.
More information regarding the bypass and scoreboarding is given [here](https://chromite.readthedocs.io/en/using-csrbox/chromite.html#scoreboard).

# File Structure

```bash
├── README.md -- Describes  each test and how the ASM is used to check the condition using Python 3.
├── uatg_reg_reset_logic.py -- ASM to check if the reset value of RF correct.
├── uatg_bypass_alu_logic.py --  ASM to check the bypass between ALU instruction.
├── uatg_bypass_logic_DIV_ALU_variable.py -- ASM to check the bypassing between DIV and ALU instruction.
├── uatg_bypass_mul_alu.py --ASM to check the bypassing between MUL and ALU instruction.
├── uatg_bypass_logic_MUL_MUL_variable.py -- ASM to check the bypassing between MUL instructions.
├── uatg_bypass_logic_DIV_MUL_variable.py -- ASM to check the bypass between DIV and MUL instruction.
├── uatg_bypass_logic_LOAD_ALU_variable.py --ASM to verify the bypass logic function between the load/store and ALU instruction.
├── uatg_bypass_pipeline_flush.py --ASM which causes pipeline flush between two bypassing instructions.
├── uatg_bypass_load_store.py --ASM to verify the forwarding between load and store instruction.
```

# Code Description
### uatg_reg_reset_logic.py
* This Script is used to check whether all the registers from the register file are reset to 0.
* Initially  we compare the x0 and x1, if they are not equal we branch to LOC where we make use of the slt instruction to make x1 0.
* Since x0 is hardwired to 0.
* The for loop is used to check all the remaining registers are zero.
* If the registers are not zero then value x1 hold will be non-zero.
* In this way we can identify why the reset test failed.  

### uatg_bypass_alu_logic.py
* This script is used to test bypass from one ALU operation to another.
* The first instruction result is stored in x24 which is used by the susequent instruction.
* The result of x24 is bypassed from memory stage to exuection stage of the second instruction.
* The result of x24 is bypassed from write-back stage to exuection stage of the third instruction.
* This requires no stalling of any operation.

### uatg_bypass_logic_DIV_ALU_variable.py
* This program tests the bypass between the div instruction and alu operation and vice versa
* The result from the div instruction is stored in x24 and the next instruction is dependent on x24.
* So the result is forwarded from memory to execute stage since it contains the loop which consumes some cycles.
* For bypassing from alu to div instruction the register x25 value is bypassed from writeback stage to execute stage of the alu operation.

### uatg_bypass_mul_alu_logic.py
* This program tests the bypass by computing x24 with the multiplication instruction which is obtained using ‘M’ extension.
* x24 is used by next instruction which is a alu operation.
* x24 is forwarded from the memory stage of the mul instruction to the execution stage of dependent sub instruction.
* With the addition of 'M' extension the processor is able to perform multipication and division operation along with the base instruction.
* For bypassing from alu to mul instruction, if there is dependency then the value will be forwarded from any of the stage to execute stage of the next instruction.

### uatg_bypass_logic_MUL_MUL_variable.py
* This program tests the bypass by computing x24 with the multiplication instruction which is obtained using ‘M’ extension.
* x24 is used by next mul instruction after the loop operation
* x24 is forwarded from the memory stage of the mul instruction to the execution stage of dependent sub instruction.
* With the addition of 'M' extension the processor is able to perform multipication and division operation along with the base instruction.
* For bypassing from alu to mul instruction, if there is dependency then the value will be forwarded from any of the stage to execute stage of the next instruction

### uatg_bypass_logic_DIV_MUL_variable.py
* This programs checks the bypassing between the div and mul instruction.
* The 'M' extension is enabled.
* x24 is computed in the execute stage of mul instruction.
* The next instruction is dependent on x24, so the value of x24 is forwarded from memory stage to execution stage of the next instruction which is div.
* Also the next instruction is dependent on x24 so its forwarded from writeback stage to execute stage.

### uatg_bypass_logic_LOAD_ALU_variable.py
* This checks the bypassing from the load/store instruction to the alu operation and vice-versa.
* x17 computed by the add instruction is used by the load instruction to obtain the address of the value to be loaded.
* The value from the memory stage is passed to the execution stage of the load instruction.
* The same value is used by the next instruction to compute the result.
* It also uses the value loaded to  x20 for the next instruction, but the load instruction takes one more cycle to obtain the data.
* the data obtained from the load instruction can be bypassed only after writeback stage, so the susequent instruction will be stalled.

### uatg_bypass_pipeline_flush.py
* This asm causes the pipeline flush between two bypassing instruction.
* Perform a store operation and then flush the pipeline,s0 is data dependent register
* Load performed after pipeline flush.

### uatg_bypass_load_store.py
* This script checks the bypass logic between load and store instruction.
* Load Contents pointed by x2 into x1.
* Store contents pointed by x1 into x3.
* If same values in x2 and x3, bypass logic works.
