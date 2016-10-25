url ='https://www.facebook.com/colleen.atkins.33?fref=ts'
os.makedirs('TestFacebook', exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
imgElems = soup.select('img')

if imgElems == []:
    print('Nothing Here!')
else:
    imgUrl = 'https://' + imgElems[0].get('src')

    res = requests.get(imgUrl)
    res.raise_for_status()
    faceFile = open(os.path.join('TestFacebook', os.path.basename(imgUrl)), 'wb')
    for chunk in res.iter_content(100000):
        faceFile.write(chunk)
    faceFile.close()
    
