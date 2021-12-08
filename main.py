import schedule
import time
import requests

# slack 에 메시지보내기
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data = {"channel": channel, "text": text}
    )
    print(response)

token = 'xoxb-2798785289607-2813472232595-9ICWPmUWDqYRC0CbNY9F9DGl'

# 사이트 체크
def check_url(url, url_name):
    response = requests.get(url).status_code

    if response != 200:
        post_message(token, "#ddd", url_name +" : "+str(response))

# 사이트 루프
def status_url() :
    for k in site.keys():
        check_url(site.get(k), k)

site = {
    '한국교원대종합교육연수원' : 'https://tcie.knue.ac.kr/',
    '한국교원대원격교육연수원' : 'https://etcie.knue.ac.kr/',
    '공정위가맹사업거래' : 'https://franchise.ftc.go.kr/',
    '세종학생해양수련원' : 'https://sjsea.sje.go.kr/',
    '한국어촌어항공단' : 'https://www.fipa.or.kr/',
    '금천구립도서관' : 'http://geumcheonlib.seoul.kr/',
    '서울신학대학교' : 'https://stu.ac.kr'
}

status_url()


#schedule.every().hours.do(status_url)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

