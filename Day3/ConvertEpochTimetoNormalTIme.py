import datetime
import os

mod_time=os.path.getmtime("student.dat")
dt_m= datetime.datetime.fromtimestamp(mod_time)
print("\n",dt_m)