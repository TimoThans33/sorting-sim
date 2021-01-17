import os
import platform

IP_ADDRESS=os.getenv("CX_TEST_SERVICE_IP_ADDRESS", default="0.0.0.0")
PORT=int(os.getenv("CX_TEST_SERVICE_PORT", default="6543"))