import numpy as np

def classify_by_base_and_step(band, base, step, n_step):
    raster_dem_for_poly = band.copy()
    base_h = base
    step_h = step

    raster_dem_for_poly[raster_dem_for_poly == 0] = 0
    c=1
    raster_dem_for_poly[(raster_dem_for_poly != 0)&(raster_dem_for_poly < base_h)] = c
    print(base_h, "-", c)
    c += 1
    for i in range(n_step):
        a = base_h + step_h * i
        b = base_h + step_h * i + step_h
        print(a, b, "-", c)
        raster_dem_for_poly[(raster_dem_for_poly >= a) & (raster_dem_for_poly < b)] = c
        c += 1
    print(b, "-", c)
    raster_dem_for_poly[raster_dem_for_poly >= b] = c

    return raster_dem_for_poly

def classify_by_list_of_values(band, break_list):
    raster_dem_for_poly = band.copy()
    base_h = break_list[0]

    raster_dem_for_poly[raster_dem_for_poly == 0] = 0
    c=1
    raster_dem_for_poly[(raster_dem_for_poly != 0)&(raster_dem_for_poly < base_h)] = c
    print(base_h, "-", c)
    c += 1
    for i in range(1, len(break_list)):
        a = break_list[i]
        b = break_list[i+1]
        print(a, b, "-", c)
        raster_dem_for_poly[(raster_dem_for_poly >= a) & (raster_dem_for_poly < b)] = c
        c += 1
    print(b, "-", c)
    raster_dem_for_poly[raster_dem_for_poly >= b] = c

    return raster_dem_for_poly


def get_quantile_values(band, break_list):
    raster_dem_for_poly = band.copy()
    output_break_list = []
    print("min ==>", raster_dem_for_poly.min())
    for i in break_list:
        quantile_value = round(np.quantile(raster_dem_for_poly, i), 2)
        output_break_list.append(quantile_value)
        print(i, "==>", quantile_value)
    print("max ==>", raster_dem_for_poly.max())
    return output_break_list


def classify_by_quantile(band, break_list):
    output_break_list = get_quantile_values(band, break_list)
    output_image = classify_by_list_of_values(band, output_break_list)
    return output_image