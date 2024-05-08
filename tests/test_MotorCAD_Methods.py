import time

from ansys.motorcad.core import MotorCADCompatibility


# Check MotorCADCompatibility object working as expected
def test_motorcadcompatibility(mc):
    # Ensure Motor-CAD has opened successfully
    time.sleep(5)

    mc2 = MotorCADCompatibility()
    try:
        # should have connected to open instance
        assert mc2.connection._port == mc.connection._port

        # Try simple method
        succ, var = mc2.GetVariable("Tooth_Width")
        assert succ == 0
        assert var is not None
        assert var != 0

        succ, var = mc2.GetVariable("not_a_var")
        assert succ != 0
    except Exception as e:
        raise e
    finally:
        mc2.Quit()
