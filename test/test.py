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
  dut._log.info("Load")
  dut.ena.value = 1
  dut.ui_in.value = 195
  dut.uio_in.value = 0
  dut.rst_n.value = 0
  await ClockCycles(dut.clk, 2)
  dut.rst_n.value = 1
  await ClockCycles(dut.clk, 2)
  dut.ui_in.value = 192
  await ClockCycles(dut.clk, 6)
  
  assert dut.uo_out.value == 16
  
