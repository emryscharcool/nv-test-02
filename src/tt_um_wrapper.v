
module tt_um_wrapper (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire ena,            // enable - goes high when design is selected        
    input  wire clk,            // clock
    input  wire rst_n           // not reset
);
    // Not using IOs here
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire [7:0] counter_q;
    assign uo_out = counter_q; // map counter to output pins

    counter #(.WIDTH(8)) my_counter (
        .clk(clk),
        .reset_n(rst_n),
        .counter_q(counter_q)
    );

endmodule
