import requests
import requests_ftp
import os
import numpy as np
import sunpy
#download gong data at around 6am on the given date.



def DL_GONG(datstr,datetype = 'datstr'):
    if datetype=='datstr':
        url = 'https://gong2.nso.edu/oQR/zqs/'+datstr[0]+datstr[1]+'/mrzqs'+datstr[0][2:]+datstr[1]+datstr[2]+'/'
    elif datetype == 'datetime':
        datstr = [str(datstr.year),str(datstr.month).zfill(2),str(datstr.day).zfill(2)]
        url = 'https://gong2.nso.edu/oQR/zqs/'+datstr[0]+datstr[1]+'/mrzqs'+datstr[0][2:]+datstr[1]+datstr[2]+'/'
    requests_ftp.monkeypatch_session()
    s = requests.Session()
    rpage = s.get(url)
    savname = './GONG/gong'+datstr[0]+datstr[1]+datstr[2]+'.fits'
    zipsavname = savname+'.gz'
    if rpage.status_code == 200:
        page = rpage.text
        soup = BeautifulSoup(page,'html.parser')
        files = [node.get('href') for node in soup.find_all('a') if node.get('href').endswith('.fits.gz')]
        fname = files[0]
        savname
        full_url = url+fname
        if not os.path.exists(savname) and not os.path.exists(zipsavname):
            import urllib.request
            urllib.request.urlretrieve(full_url,zipsavname)

        if not os.path.exists(savname):
            import gzip
            with gzip.open(zipsavname, 'rb') as f:
                with open(savname, 'wb') as g:
                    g.write(f.read())
    else: 
        return(np.array([0]),'error')
    # The mean is subtracted to enforce div(B) = 0 on the solar surface: n.b. it is
    # not obvious this is the correct way to do this, so use the following lines
    # at your own risk!
    [[br, header]] = sunpy.io.fits.read(savname)
    br = br - np.mean(br)
    ###############################################################################
    # GONG maps have their LH edge at -180deg in Carrington Longitude,
    # so roll to get it at 0deg. This way the input magnetic field is in a
    # Carrington frame of reference, which matters later when lining the field
    # lines up with the AIA image.
    br = np.roll(br, header['CRVAL1'] + 180, axis=1)
    return(br,header)