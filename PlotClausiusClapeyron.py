import numpy as np
import matplotlib.pyplot as plt

#TC_ lo - lower bound temperature in celsius, user specific
#TC_ hi - upper bound temperature in celsius, user specific
#OutFName = name of thr output figure, user specified


TC_lo = -5.0
TC_hi =  25.0
def main(argv):
    #create an array of air temperatures in degrees celsius
    TC = np.linspace(TC_lo, TC_hi, num=200)

    #compute saturation vapor pressure in kPa using CC equation

    estar = 0.611*np.exp(17.3*TC / (TC + 273.3))

    #plot the results
    plt.figure(figure=(12,10))
    plt.plot(TC, estar,'r')
    plt.xlim([TC_lo, TC_hi])
    plt.xlabel('Temperature in degrees Celsius')
    plt.ylabel('Saturation vapor pressure in Kpa')
   # plt.savefig(OutFName,dpi=300)
    return