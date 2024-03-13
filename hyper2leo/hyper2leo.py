def um_to_nm(um_measurement):
    nm_measurement = um_measurement * 1000
    return f"{nm_measurement} nm"

def wv_to_fr(wavelength):
    frequency = 3e8/wavelength
    return frequency
    
def fr_to_wv(frequency):
    wavelength = 3e8/frequency
    return wavelength

def hyper_to_landsat_mss_1_3(range_min, range_max):
    if range_max <= 900 and range_min > 800:
        return f"The range {range_min} - {range_max} nanometers is Band 7 (the NIR band) for Landsats OSS 1-3"
    if range_max <= 800 and range_min > 700:
        return f"The range {range_min} - {range_max} nanometers is Band 6 (the NIR band) for Landsats OSS 1-3"
    elif range_max <= 700 and range_min >= 600:
        return f"The range {range_min} - {range_max} nanometers is Band 5 (the Red band) for Landsats OSS 1-3"    
    elif range_max <= 600 and range_min >= 500:
        return f"The range {range_min} - {range_max} nanometers is in Band 4 (the Green band) for Landsats OSS 1-3"
    else:
        return "The range entered is outside of ranges for Landsat OSS 1-3"
    
def hyper_to_landsat_mss_4_5(range_min, range_max):
    if range_max <= 900 and range_min > 800:
        return f"The range {range_min} - {range_max} nanometers is Band 4 (the NIR band) for Landsats OSS 4-5"
    if range_max <= 800 and range_min > 700:
        return f"The range {range_min} - {range_max} nanometers is Band 3 (the NIR band) for Landsats OSS 4-5"
    elif range_max <= 700 and range_min >= 600:
        return f"The range {range_min} - {range_max} nanometers is Band 2 (the Red band) for Landsats OSS 4-5"    
    elif range_max <= 600 and range_min >= 500:
        return f"The range {range_min} - {range_max} nanometers is in Band 1 (the Green band) for Landsats OSS 4-5"
    else:
        return "The range entered is outside of ranges for Landsat OSS 4-5"
    
#THIS STILL NEEDS TO BE FIXED

def hyper_to_landsat_tm_4_5(range_min, range_max):
    if range_max <= 12500 and range_min > 10400:
        return f"The range {range_min} - {range_max} nanometers is Band 6 (the Thermal band) for Landsats TM 4-5"
    elif range_max <= 2350 and range_min > 2080:
        return f"The range {range_min} - {range_max} nanometers is Band 7 (the SWIR 2 band) for Landsats TM 4-5"
    if range_max <= 1750 and range_min > 1550:
        return f"The range {range_min} - {range_max} nanometers is Band 5 (the SWIR 1 band) for Landsats TM 4-5"
    elif range_max <= 760 and range_min >= 900:
        return f"The range {range_min} - {range_max} nanometers is Band 4 (the NIR band) for Landsats TM 4-5"    
    elif range_max <= 690 and range_min >= 630:
        return f"The range {range_min} - {range_max} nanometers is Band 3 (the Red band) for Landsats TM 4-5"
    elif range_max <= 600 and range_min >= 520:
        return f"The range {range_min} - {range_max} nanometers is Band 2 (the Green band) for Landsats TM 4-5"    
    elif range_max < 520 and range_min >= 450:
        return f"The range {range_min} - {range_max} nanometers is Band 1 (the Blue band) for Landsats TM 4-5"         
    else:
        return "The range entered is outside of ranges for Landsat TM 4-5"