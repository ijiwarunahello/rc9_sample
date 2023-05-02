from caoprov_denso_rc9 import RC9
from common import (
    RC9_PROJ_PATH,
)

rc9 = RC9(RC9_PROJ_PATH)
io = "I0"
value = rc9.get_value(io)
print(f"{io}: {value}")
