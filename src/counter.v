// Author: Emrys Leowhel Oling
// Date: 2024-06-17
// Description: Simple counter module
// Usage: Instantiate with desired WIDTH parameter
// Github: https://github.com/emryscharcool/nv-test

`default_nettype none
`timescale 1ns/1ns

module counter #(parameter WIDTH=8) (
    input  clk, 
    input  reset_n,
    output reg [WIDTH-1:0]  counter_q
);

always @(posedge clk or negedge reset_n)
    begin
        if(!reset_n)
            counter_q <= 0;
        else
            counter_q <= counter_q + 1;
    end
endmodule