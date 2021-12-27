# chromite-bug-bounty
chromite-bug-bounty special topic coursework

This repository consists of python scripts to generate RISC-V assembly for testing the Regfile + Bypass + Scoreboard in the Chromite core developed by incore semiconductors

The Register file is a part of the decode stage in the pipeline. It consists of 32 registers, each of 32 bit width if the architecture supported by core is RV32. There are 2 read ports and 1 write port. More information regarding the register file is given [here](https://chromite.readthedocs.io/en/using-csrbox/chromite.html#register-file).

Bypass logic: It is introduced to solve data hazards. Data dependencies between subsequent instructions can lead to lower performance due to the necessity of stalls to ensure program integrity.This method involves adding multiplexers in front of the ALU

Scoreboarding: In its minimal configuration implements a 32-bit register for each architectural register file .Each bit in this register corresponds to a register in the respective register file.
More information regarding the bypass and scoreboarding is given [here](https://chromite.readthedocs.io/en/using-csrbox/chromite.html#scoreboard).

# File Structure


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
* Here for example 3 instructions are considered.
* These 3 instructions have x24 as a dependent register across the instructions.
* The result of x24 is bypassed from memory stage to exuection stage of the second instruction.
* The result of x24 is bypassed from write-back stage to exuection stage of the third instruction.
* This requires no stalling of any operation.

### 



