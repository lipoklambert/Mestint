from trial_error import trial_error
from farmer import Farmer

f = Farmer((0,0,0,0), (1,1,1,1))
print(trial_error(f).solution())