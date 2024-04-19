# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_ac(dut):
  dut._log.info("Start")
  
  # Our example module doesn't use clock and reset, but we show how to use them here anyway.
  clock = Clock(dut.clk, 10, units="us")
  cocotb.start_soon(clock.start())

  # Load
  dut._log.info("ResetLoad in=131= 1000 0011")
  dut.ena.value = 1
  dut.ui_in.value = 131
  dut.uio_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 2)
  dut.rst_n.value = 1
  dut._log.info(dut.uo_out.value)
  dut._log.info("Load")
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  dut.ui_in.value = 192
  dut._log.info("Up6")
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  await ClockCycles(dut.clk, 1)
  dut._log.info(dut.uo_out.value)
  # 56 = 0011 1000  -- value 8 + RCOB*16 + !ui_in[0]*32
  assert dut.uo_out.value == 56
  
  
