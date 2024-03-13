def um_to_nm(um_measurement):
    nm_measurement = um_measurement * 1000
    return nm_measurement

def wv_to_fr(wavelength):
    frequency = 3e8/wavelength
    return frequency
    
def fr_to_wv(frequency):
    wavelength = 3e8/frequency
    return wavelength