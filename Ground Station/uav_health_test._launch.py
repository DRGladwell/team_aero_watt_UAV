#!/usr/bin/env python3
'''
code to run UAV health check. The UAV code on the raspberry pi will check for this message whilst the flight has not
begun. If flight has not begun the UAV code SHOULD acknowledge that it's running the UAV_health_test. Otherwise there's
an issue.
'''

# variable switch_state  (a case statement is used in the main to select current check)

# method to request the UAV to enter health check mode. Return (1 success and 0 failure).

# method to send validation message to uav_health.py

# method to send failure message to uav_health.py

# method to send restart message to uav_health.py

# method to go back_one_step message to uav_health.py

# main
'''
The list of test steps will be hardcoded into uav_health_test_launch.py (ground station) and on the uav_health.py (UAV)
through a switch statement. At a given step the uav_health.py will perform a singular identifiable action, or the 
uav_health_test.py will send a message to make the UAV perform an action.

validation, restart, failure or back_one_step will change the state of both uav_health_test_launch.py and uav_health.py
provided that these messages are received. 

If all checks are validated uav_health_test_launch.py will close and the method in uav_health.py will stop running.
'''

