#function to re-centre angles with new limits
import numpy as np
def re_angle(ang_input,low,high):
	ang_in = ang_input*1.
	under = (ang_in < low)
	over =  (ang_in > high)
	ang_in[under] = ang_in[under] + (2*np.pi)#*(np.floor_divide(abs(ang_in[under]),2*np.pi)+1)
	ang_in[over] = ang_in[over] - (2*np.pi)
	return(ang_in)

def re_angle_deg(ang_input,low,high):
	ang_in = ang_input*1.
	under = (ang_in < low)
	over =  (ang_in > high)
	ang_in[under] = ang_in[under] + (360)#*(np.floor_divide(abs(ang_in[under]),2*np.pi)+1)
	ang_in[over] = ang_in[over] - (360)
	return(ang_in)


def ang_add(ang1,ang2,low,high):
	ang_out = ang1+ang2
	ang_out = re_angle(ang_out,low,high)
	return(ang_out)