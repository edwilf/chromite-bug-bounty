# chromite-bug-bounty
chromite-bug-bounty special topic coursework

This repository consists of python scripts to generate RISC-V assembly for testing the Regfile + Bypass + Scoreboard in the Chromite core developed by incore semiconductors
The Register file is a part of the decode stage in the pipeline. It consists of 32 registers, each of 32 bit width if the architecture supported by core is RV32. There are 2 read ports and 1 write port.
Bypass logic: It is introduced to solve data hazards. Data dependencies between subsequent instructions can lead to lower performance due to the necessity of stalls to ensure program integrity.This method involves adding multiplexers in front of the ALU
Scoreboarding: In its minimal configuration implements a 32-bit register for each architectural register file .Each bit in this register corresponds to a register in the respective register file.

# File Structure

