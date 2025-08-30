import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

@cocotb.test()
async def test_counter_basic(dut):
    """Check that counter increments correctly"""

    # Start a 10ns clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Apply reset
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)  # wait one edge after reset release

    last_val = int(dut.uo_out.value)
    dut._log.info(f"After reset, uo_out = {last_val}")

    # Now check increments over 20 cycles
    for i in range(20):
        await RisingEdge(dut.clk)
        new_val = int(dut.uo_out.value)
        dut._log.info(f"Cycle {i}: uo_out = {new_val}")

        assert new_val == (last_val + 1) % 256, \
            f"Counter did not increment correctly at cycle {i}! Expected {last_val+1}, got {new_val}"

        last_val = new_val 
   