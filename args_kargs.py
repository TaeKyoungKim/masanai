def makeURL(*args , **kwargs):
    result = 0
    for i in args:
        result += i
    myUrl = "http://192.168.1.120/index.php?"
    for k, v in kwargs.items():
        myUrl += k + '=' + v + '&'

    myUrl = myUrl.rstrip('&')
    print(myUrl)
    print(result)

makeURL(1, 2, 3, 4, 5, user = 'psychoria', index = '5', page = '10')




[1,32,32] : 리스트
(1,32,32):튜플
{} :집합
{"마산회원구":["봉림동","봉원동","봉수동"], "x":"y"} : 딕셔너리