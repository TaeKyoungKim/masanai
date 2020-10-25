def makeURL(**kargs):
    myUrl = "http://192.168.1.120/index.php?"
    for k, v in kargs.items():
        myUrl += k + '=' + v + '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)

makeURL(user = 'psychoria', index = '5', page = '10')