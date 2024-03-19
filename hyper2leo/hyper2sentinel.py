#Per Sentinel 2 ESA handbook
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

#Calculation of band range per central wavelength and bandwidth
def sentinel_wavelengths(band_name, central_wv, bandwidth):
    min_wv = central_wv - (bandwidth/2)
    max_wv = central_wv + (bandwidth/2)
    return [band_name, min_wv, max_wv]

bands_range = [sentinel_wavelengths(band[0], band[1], band[2]) for band in sentinel_info] 

for i in bands_range:
    print(i)


#Sentinel2 based off of ESA Sentinel Handbook

def hyper_to_sentinel2(range_min, range_max):
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
