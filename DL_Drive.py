import requests
import requests_ftp
import os
import gdown


def DL_Drive(fname): # download a file from my google drive
    # check if I already have the file:
    if not os.path.exists(fname):
    
        # match up the file I want to where I've stored in on google drive
        url_dict = {'omni_2006_21.hdf': 'https://drive.google.com/uc?id=1qKdjrF-VQ9wy-Xp1r1X-8OfgSmQV4zWk',
                    'Matched_crossings_2006_2020.h5':'https://drive.google.com/uc?id=1Lt2456o9zGImAK8hRrvG-nORfXN0ml9U', 
                    'HCSGONG_MAPs.hdf':'https://drive.google.com/uc?id=1T_oP3DIva9qHiKdVxG5MPbfCG40Q4tNm', 
                    'dphi_4d_array.nc':'https://drive.google.com/uc?id=1WDQEuqHmINuTgkqocI6a96GC5BZexQbJ', 
                    'dfss_save_180.hdf':'https://drive.google.com/uc?id=1ilvUJ8E5vgbXPgKpVqs26aArVyphKFmF',
                   './PFSS_HDFs/pfss_2006-10-07T055400.hdf': 'https://drive.google.com/uc?id=1DEWA2yDKOZt4prRcguL_mYbcNPsxj1IG'}
        url = url_dict[fname] 
        gdown.download(url, fname, quiet=False)
        
        return('success')
    else:
        return('file already downloaded')