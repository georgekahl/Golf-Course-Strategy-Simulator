from scipy.optimize import curve_fit

#Putting model
def yards_to_feet(distance):
    return distance*3

def expected_putts_model(x, a, b, c):
    return a * ((x+b)**c - b**c)

def expected_putts(distance, a, b, c):
    return expected_putts_model(distance, a, b, c)

def fit_putting_model(PUTT_LENGTHS_FT_DATA, EXPECTED_PUTTS_DATA):
    params, covariance = curve_fit(expected_putts_model,PUTT_LENGTHS_FT_DATA, EXPECTED_PUTTS_DATA, p0 = [0.5, 1, 0.5], bounds = (0, float("inf")), maxfev=100000)
    a, b, c, = params
    return a, b, c, covariance