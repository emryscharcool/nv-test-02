import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

# Helper function to safely convert signals to int
def safe_int(signal, default=0):
    """Convert signal to int, default if value is unresolved ('x' or 'z')"""
    return int(signal.value) if signal.value.is_resolvable else default

@cocotb.test()
async def test_counter_basic(dut):
    """Test that the counter increments correctly"""

    # Start a 10 ns clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Apply reset for 2 cycles
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)

    # Release reset
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)  # wait one clean edge

    # Get initial counter value safely
    last_val = safe_int(dut.uo_out)
    dut._log.info(f"After reset, uo_out = {last_val}")

    # Check increments over 20 cycles
    for i in range(20):
        await RisingEdge(dut.clk)
        new_val = safe_int(dut.uo_out)
        dut._log.info(f"Cycle {i}: uo_out = {new_val}")

        expected_val = (last_val + 1) % (2**len(dut.uo_out))
        assert new_val == expected_val, (
            f"Counter did not increment correctly at cycle {i}! "
            f"Expected {expected_val}, got {new_val}"
        )

        last_val = new_val
