def um_to_nm(um_measurement):
    nm_measurement = um_measurement * 1000
    return f"{nm_measurement} nm"

def wv_to_fr(wavelength):
    frequency = 3e8/wavelength
    return frequency
    
def fr_to_wv(frequency):
    wavelength = 3e8/frequency
    return wavelength

def hyper_to_sentinel_wavelength(range_min, range_max):
    return range(range_min,range_max)