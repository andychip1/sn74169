/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`define default_netname none

module tt06_andychip1_sn74169 (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // will go high when the design is enabled
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
  assign uio_out = 0;
  assign uio_oe  = 0;
  assign uo_out[7:4] = 4'b0000;

sn74169 i1(.A(ui_in[3:0]),.CLK(clk),.ENPB(ui_in[4]),.ENTB(ui_in[5]),.LOADB(ui_in[6]),.Q(uo_out[3:0]),.RCOB(uo_out[4]),.U_DB(ui_in[7]));


endmodule


