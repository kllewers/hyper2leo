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

#for i in bands_range:
    #print(i)

#also generate a table

#Sentinel2 based off of ESA Sentinel Handbook

def hyper_to_sentinel2(range_min, range_max):
    if range_min > 430:
        if range_max <=2280 and range_min >= 2100:
            return f"The range {range_min} - {range_max} nanometers is Band 12 (AOT determination) for Sentinel 2."
        elif range_max <= 1655 and range_min >= 1565:
            return f"The range {range_min} - {range_max} nanometers is Band 11 (Soils detection) for Sentinel 2."
        elif range_max <= 1390 and range_min >= 1360:
            return f"The range {range_min} - {range_max} nanometers is Band 10 (Detection of thin cirrus for atmospheric correction) for Sentinel 2."
        elif range_max <= 955 and range_min >= 935:
            return f"The range {range_min} - {range_max} nanometers is Band 9 (Water Vapour absorption atmospheric correction) for Sentinel 2."
        elif range_max <= 855 and range_min >= 875:
            return f"The range {range_min} - {range_max} nanometers is Band 8a (water vapour absorption reference) for Sentinel 2."
        elif range_max <= 899.5 and range_min >= 784.5:
            return f"The range {range_min} - {range_max} nanometers is Band 8 (Leaf Area Index(LAI)) for Sentinel 2."
        elif range_max <= 793 and range_min >= 773:
            return f"The range {range_min} - {range_max} nanometers is Band 7 (Vegetation Red Edge 3) for Sentinel 2."
        elif range_max <= 747.5 and range_min >= 732.5:
            return f"The range {range_min} - {range_max} nanometers is Band 6 (Vegetation Red Edge 2) for Sentinel 2."
        elif range_max <= 712.5 and range_min >= 697.5:
            return f"The range {range_min} - {range_max} nanometers is Band 5 (Vegetation Red Edge 1) for Sentinel 2."
        elif range_max <= 680 and range_min >= 650:
            return f"The range {range_min} - {range_max} nanometers is Band 4 (Red) for Sentinel 2."
        elif range_max <= 577.5 and range_min >= 542.5:
            return f"The range {range_min} - {range_max} nanometers is Band 3 (Green) for Sentinel 2."
        elif range_max <= 522.5 and range_min >= 457.5:
            return f"The range {range_min} - {range_max} nanometers is Band 2 (Blue) for Sentinel 2."
        elif range_max <= 453 and range_min >= 433:
            return f"The range {range_min} - {range_max} nanometers is Band 1 (Coastal blue) for Sentinel 2." 
        else:
            return f"The range {range_min} - {range_max} nanometers is not in the range of Sentinel 2 or the range of a single band."
    elif range_min < 400:
        if range_max < 2.280 and range_min >= 2.100:
            return f"The range {range_min} - {range_max} microns is Band 12 (AOT determination) for Sentinel 2."
        elif range_max <= 1.655 and range_min >= 1.565:
            return f"The range {range_min} - {range_max} microns is Band 11 (Soils detection) for Sentinel 2."
        elif range_max <= 1.390 and range_min >= 1.360:
            return f"The range {range_min} - {range_max} microns is Band 10 (Detection of thin cirrus for atmospheric correction) for Sentinel 2."
        elif range_max <= .955 and range_min >= .935:
            return f"The range {range_min} - {range_max} microns is Band 9 (Water Vapour absorption atmospheric correction) for Sentinel 2."
        elif range_max <= .855 and range_min >= .875:
            return f"The range {range_min} - {range_max} microns is Band 8a (water vapour absorption reference) for Sentinel 2."
        elif range_max <= .8995 and range_min >= .7845:
            return f"The range {range_min} - {range_max} microns is Band 8 (Leaf Area Index(LAI)) for Sentinel 2."
        elif range_max <= .793 and range_min >= .773:
            return f"The range {range_min} - {range_max} microns is Band 7 (Vegetation Red Edge 3) for Sentinel 2."
        elif range_max <= .7475 and range_min >= .7325:
            return f"The range {range_min} - {range_max} microns is Band 6 (Vegetation Red Edge 2) for Sentinel 2."
        elif range_max <= .7125 and range_min >= .6975:
            return f"The range {range_min} - {range_max} microns is Band 5 (Vegetation Red Edge 1) for Sentinel 2."
        elif range_max <= .680 and range_min >= .650:
            return f"The range {range_min} - {range_max} microns is Band 4 (Red) for Sentinel 2."
        elif range_max <= .5775 and range_min >= .5425:
            return f"The range {range_min} - {range_max} microns is Band 3 (Green) for Sentinel 2."
        elif range_max <= .5225 and range_min >= .4575:
            return f"The range {range_min} - {range_max} microns is Band 2 (Blue) for Sentinel 2."
        else:
            return f"The range {range_min} - {range_max} microns is not in the range of Sentinel 2 or the range of a single band."

print(hyper_to_sentinel2(.55, .57))
print(hyper_to_sentinel2(550, 570))
print(hyper_to_sentinel2(4236719, 124156932))
print(hyper_to_sentinel2(.2, .21))
print(hyper_to_sentinel2(.57, .67))


# Improved representation of Sentinel-2 bands
sentinel_bands = [
    {"name": "Band 1 - Coastal blue", "min_wv": 423, "max_wv": 463},
    {"name": "Band 2 - Blue", "min_wv": 457.5, "max_wv": 522.5},
    {"name": "Band 3 - Green", "min_wv": 542.5, "max_wv": 577.5},
    {"name": "Band 4 - Red", "min_wv": 650, "max_wv": 680},
    {"name": "Band 5 - Vegetation Red Edge 1", "min_wv": 697.5, "max_wv": 712.5},
    {"name": "Band 6 - Vegetation Red Edge 2", "min_wv": 732.5, "max_wv": 747.5},
    {"name": "Band 7 - Vegetation Red Edge 3", "min_wv": 773, "max_wv": 793},
    {"name": "Band 8 - Leaf Area Index (LAI)", "min_wv": 784.5, "max_wv": 899.5},
    {"name": "Band 8a - Water vapour absorption reference", "min_wv": 855, "max_wv": 875},
    {"name": "Band 9 - Water Vapour absorption atmospheric correction", "min_wv": 935, "max_wv": 955},
    {"name": "Band 10 - Detection of thin cirrus for atmospheric correction", "min_wv": 1360, "max_wv": 1390},
    {"name": "Band 11 - Soils detection", "min_wv": 1565, "max_wv": 1655},
    {"name": "Band 12 - AOT determination", "min_wv": 2100, "max_wv": 2280}
]

#More elegant code:

# Function to match wavelength range to Sentinel-2 bands
def hyper_to_sentinel2_v2(range_min, range_max):
    matching_bands = []
    for band in sentinel_bands:
        # Check if the given range overlaps with the band's range
        if not (range_max < band["min_wv"] or range_min > band["max_wv"]):
            matching_bands.append(band["name"])
    
    if matching_bands:
        return "Matching bands: " + ", ".join(matching_bands)
    else:
        return "No matching bands found for the given range."
    
#Add the function to also include the ranges of the returned matching bands

# Example usage
print(hyper_to_sentinel2_v2(600, 900))  # An example call to this function




#Make a NEON hyperspectral instrument specific function



#Move on to where DNs are on the curve
