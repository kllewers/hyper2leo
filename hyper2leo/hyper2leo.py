#GENERAL FUNCTIONS
def um_to_nm(um_measurement: float or int) -> float or int:
    nm_measurement = um_measurement * 1000
    return f"{nm_measurement} nm"

def wv_to_fr(wavelength: float or int) -> float or int:
    frequency = 3e8/wavelength
    return frequency
    
def fr_to_wv(frequency: float or int) -> float or int:
    wavelength = 3e8/frequency
    return wavelength

#LANDSAT

def hyper_to_landsat_mss_1_3(range_min: float, range_max: float or int):
    if range_max <= 900 and range_min > 800:
        return f"The range {range_min} - {range_max} nanometers is Band 7 (the NIR band) for Landsats MSS 1-3"
    if range_max <= 800 and range_min > 700:
        return f"The range {range_min} - {range_max} nanometers is Band 6 (the NIR band) for Landsats MSS 1-3"
    elif range_max <= 700 and range_min >= 600:
        return f"The range {range_min} - {range_max} nanometers is Band 5 (the Red band) for Landsats MSS 1-3"    
    elif range_max <= 600 and range_min >= 500:
        return f"The range {range_min} - {range_max} nanometers is in Band 4 (the Green band) for Landsats MSS 1-3"
    else:
        return "The range entered is outside of ranges for Landsat OSS 1-3"
    
def hyper_to_landsat_mss_4_5(range_min: float or int, range_max: float or int):
    if range_max <= 900 and range_min > 800:
        return f"The range {range_min} - {range_max} nanometers is Band 4 (the NIR band) for Landsats MSS 4-5"
    if range_max <= 800 and range_min > 700:
        return f"The range {range_min} - {range_max} nanometers is Band 3 (the NIR band) for Landsats MSS 4-5"
    elif range_max <= 700 and range_min >= 600:
        return f"The range {range_min} - {range_max} nanometers is Band 2 (the Red band) for Landsats MSS 4-5"    
    elif range_max <= 600 and range_min >= 500:
        return f"The range {range_min} - {range_max} nanometers is in Band 1 (the Green band) for Landsats MSS 4-5"
    else:
        return "The range entered is outside of ranges for Landsat OSS 4-5"
        
def hyper_to_landsat_tm_4_5(range_min: float or int, range_max: float or int):
    if range_max <= 12500 and range_min >= 10400:
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

#I need to figure out what to do about the panchromatic band...

def hyper_to_landsat_etm_7(range_min: float or int, range_max: float or int):
    if range_max and range_min > 430:
        if range_max <= 12500 and range_min >= 10400:
            return f"The range {range_min} - {range_max} nanometers is Band 6 (the Thermal band) for Landsat ETM+ 7"
        elif range_max <= 2350 and range_min > 2090:
            return f"The range {range_min} - {range_max} nanometers is Band 7 (the SWIR 2 band) for Landsat ETM+ 7"
        elif range_max <= 1750 and range_min > 1550:
            return f"The range {range_min} - {range_max} nanometers is Band 5 (the SWIR 1 band) for Landsat ETM+ 7"
        elif range_max <= 900 and range_min > 770:
            return f"The range {range_min} - {range_max} nanometers is Band 4 (the NIR band) for Landsat ETM+ 7"        
        elif range_max <= 690 and range_min > 630:
            return f"The range {range_min} - {range_max} nanometers is Band 3 (the Red band) for Landsat ETM+ 7" 
        elif range_max <= 600 and range_min > 520:
            return f"The range {range_min} - {range_max} nanometers is Band 2 (the Green band) for Landsat ETM+ 7" 
        elif range_max <= 520 and range_min > 450:
            return f"The range {range_min} - {range_max} nanometers is Band 1 (the Blue band) for Landsat ETM+ 7"
        else:
            return f"The entered range of {range_min} - {range_max} nm is not in the range of Landsat ETM+ 7"
    elif range_max and range_min < 430:
        if range_max <= 12.500 and range_min >= 10.400:
            return f"The range {range_min} - {range_max} microns is Band 6 (the Thermal band) for Landsat ETM+ 7"
        elif range_max <= 2.350 and range_min > 2.090:
            return f"The range {range_min} - {range_max} microns is Band 7 (the SWIR 2 band) for Landsat ETM+ 7"
        elif range_max <= 1.750 and range_min > 1.550:
            return f"The range {range_min} - {range_max} microns is Band 5 (the SWIR 1 band) for Landsat ETM+ 7"
        elif range_max <= .900 and range_min > .770:
            return f"The range {range_min} - {range_max} microns is Band 4 (the NIR band) for Landsat ETM+ 7"        
        elif range_max <= .690 and range_min > .630:
            return f"The range {range_min} - {range_max} microns is Band 3 (the Red band) for Landsat ETM+ 7" 
        elif range_max <= .600 and range_min > .520:
            return f"The range {range_min} - {range_max} microns is Band 2 (the Green band) for Landsat ETM+ 7" 
        elif range_max <= .520 and range_min > .450:
            return f"The range {range_min} - {range_max} microns is Band 1 (the Blue band) for Landsat ETM+ 7" 
        else:
            return f"The entered range of {range_min} - {range_max} microns is not in the range of Landsat ETM+ 7"           
    
"""def hyper_to_landsat_8_9(range_min, range_max):
    if range_max < range_min:
        return f"The range " """

#SENTINEL FUNCTIONS

sentinel_info = [
    ["Band 1 - coastal blue", 443, 20],
    ["Band 2 - blue", 490, 65],
    ["Band 3 - green", 560, 35],
    ["Band 4 - red", 665, 30],
    ["Band 5 - Vegetation Red Edge 1", 705, 15],
    ["Band 6 - Vegetation Red Edge 2", 740, 15], 
    ["Band 7 - Vegetation Red Edge 3", 783, 20],
    ["Band 8 - Leaf Area Index(LAI)", 842, 115], 
    ["Band 8a - water vapour absorption reference", 865, 20],
    ["Band 9 - Water Vapour absorption atmospheric correction", 945, 20], 
    ["Band 10 - Detection of thin cirrus for atmospheric correction", 1375, 30],
    ["Band 11 - Soils detection", 1610, 90],
    ["Band 12 - AOT determination", 2190, 180]

]

def sentinel_wavelengths(band_name: str, central_wv: float, bandwidth: int):
    min_wv = central_wv - (bandwidth/2)
    max_wv = central_wv + (bandwidth/2)
    return [band_name, min_wv, max_wv]

bands_range = [sentinel_wavelengths(band[0], band[1], band[2]) for band in sentinel_info] 

for i in bands_range:
    print(i)


#Sentinel2 based off of ESA Sentinel Handbook
def hyper_to_sentinel2(range_min: float or int, range_max: float or int):
    if range_max or range_min > 430:
        if range_max <=2280 and range_min >= 2100:
            return f"The range {range_min} - {range_max} nanometers is Band 12 (AOT determination) for Sentinel 2."
        elif range_max <= 1655 and range_min >= 1565:
            return f"The range {range_min} - {range_max} nanometers is Band 11 (Soils detection) for Sentinel 2."
        elif range_max <= 1390 and range_min >= 1360:
            return f"The range {range_min} - {range_max} nanometers is Band 10 (Detection of thin cirrus for atmospheric correction) for Sentinel 2."
        elif range_max <= 955 and range_min >= 935:
            return f"The range {range_min} - {range_max} nanometers is Band 9 (Water Vapour absorption atmospheric correction) for Sentinel 2."
        else:
            return f"The range {range_min} - {range_max} nanometers is not in the range of Sentinel 2."
    elif range_max or range_min < 400:
        if range_max < 2.280 and range_min >= 2.100:
            return f"The range {range_min} - {range_max} microns is Band 12 (AOT determination) for Sentinel 2."
        elif range_max <= 1.655 and range_min >= 1.565:
            return f"The range {range_min} - {range_max} microns is Band 11 (Soils detection) for Sentinel 2."
        elif range_max <= 1.390 and range_min >= 1.360:
            return f"The range {range_min} - {range_max} microns is Band 10 (Detection of thin cirrus for atmospheric correction) for Sentinel 2."
        elif range_max <= .955 and range_min >= .935:
            return f"The range {range_min} - {range_max} microns is Band 9 (Water Vapour absorption atmospheric correction) for Sentinel 2."
        else:
            return f"The range {range_min} - {range_max} microns is not in the range of Sentinel 2."
