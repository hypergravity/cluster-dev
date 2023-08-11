
from astropy.table import Table
class SynStars():
    def __init__(self):
        pass
    
    def __call__(self, isochrone:Table, imf: IMF, mag_err: MagErr,  n_star=1000, model="mist.csst", imf_kwargs, mag_err_kwargs):
        sample_stars = imf.sample(n_star, **imf_kwargs)  # a list of star mass
        col_mass = ""
        col_mags = []
        interpolated_mag = ""
        interpolated_mag_err = MagErr("")(interpolated_mag, **mag_err_kwargs)
        return interpolated_mag + interpolated_mag_err

class MockCMD:
    @staticmethod
    def fun():
        pass
    

class MagErr:
    
    def __init__(self, datasrc="gaiadr3"):
        pass
    
    def __call__(self, mag, **kwargs):
        pass
        
        

class IMF:
    def __init__(self, imf="salpeter55", **kwargs):
        pass
    
    def plot(self, mass_grid=None):
        return self.eval(mass_grid)
    
    def eval(self, mass):
        return 0

    def __call__(self, *args, **kwargs):
        return 1
    
    def sample(self, n_star):
        return # a sample of stars
    
    def __getitem__(self, item):
        return 2

imf = IMF()
imf.sample(123)


# config.toml

# [parsec.gaiadr3]

# [parsec.csst]

# [mist.gaiadr3]

# col_mass = "mist_csst_mass"
# col_mags = [ "mag1", "mag2" ]

# [mist.csst]
# col_mass = "mist_csst_mass"
# col_mags = [ "mag1", "mag2" ]

