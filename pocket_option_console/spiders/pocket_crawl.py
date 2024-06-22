from scrapy import Spider, Request
from scrapy.utils.response import open_in_browser
from twocaptcha import TwoCaptcha
import requests
import json


class PocketCrawlSpider(Spider):
    name = "pocket_crawl_v2"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'lang=en; uuid=e4f9cf3b-3c2e-4f13-b491-9a6e0e28115e; no-login-captcha=1; guide=1; loggedIn=1; _gid=GA1.2.60535226.1718854998; brief-period=; laravel_session=eyJpdiI6IlA2TVZxTFhCNEs5Uy96b3AxK2lmR3c9PSIsInZhbHVlIjoiR2pPR0RtYnR2VHMzT0JZYjVxS0lqdlFCQVdQa0ttOHVrWUU0bGhINDlGZVdTOGJFV0VwUlBqazRLYWNRaWZ5cExoQzl0TVJHQ1U0SzkrcjNtMmNKQVpmQ3Z2K085dnprTHovMmpMVUpqMlZRZWNNMFEzMDllUHlKbExxNlM2VEMiLCJtYWMiOiI2MWY3MWEyMjg2Nzc5MzI0NTlkNzU1M2YwZDk2NDBhZTZjNTBhMjdlZmFkMzQxZjVhMjIzMmI5MjIwOGU5MmFhIiwidGFnIjoiIn0%3D; _gat_UA-251659701-1=1; _ga=GA1.1.1357881239.1718854998; _ga_GTNB8BMG31=GS1.2.1718854999.1.1.1718856434.0.0.0; _ga_4QRFFGPLFT=GS1.1.1718854998.1.1.1718856437.0.0.0',
        'priority': 'u=0, i',
        'referer': 'https://affiliate.pocketoption.com/en/dashboard',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://affiliate.pocketoption.com/en/login'
        yield Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response, **kwargs):
        token = response.css('[name="_token"]::attr(value)').get('')
        site_key = response.css('#recaptcha-element::attr(data-sitekey)').get('')
        solver = TwoCaptcha("095ba510e3c7aa6195507a27f7b0824d")
        while True:
            try:
                result = solver.recaptcha(
                    sitekey=site_key,
                    url='https://affiliate.pocketoption.com/en/login')
                code = result["code"]
                if code:
                    break
                else:
                    continue
            except Exception as e:
                print(e)
                code = ''
                result = {}
                continue
        url = "https://affiliate.pocketoption.com/en/login"
        payload = f'_token={token}&email=fasehfaizan0%40gmail.com&password=Faseh!%40%231234&g-recaptcha-response={result["code"]}'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'lang=en; uuid=e4f9cf3b-3c2e-4f13-b491-9a6e0e28115e; no-login-captcha=1; guide=1; loggedIn=1; _gid=GA1.2.60535226.1718854998; brief-period=; laravel_session=eyJpdiI6IndyVURkSWZZcW40RzZpdDRUTy9Yc3c9PSIsInZhbHVlIjoiWm1TUmYzY3hsY1EyQjEwQ1Y5SjU4ZjlVTERTNWdhUERwYjB4OWxsT0swUDVwcHdtN0hHQ3BIc003SllzbGwwZWRzUlFBWWdHQjBJMFh5Z2FrODNoVkUvVzRxM29PTkdaMEZDQ1ZBSVFOamhqV09kSzNMRHJxMVdWR0syUEE3aGgiLCJtYWMiOiIzZDFkOTNkMDJiNjY5ZTNhNTI4NDdlZGNhNTQ5ZjVjNTAyMWU1OWE4ODYwOTRjZmM5NTZmOTVkZmY4ZjEzNzRlIiwidGFnIjoiIn0%3D; _ga=GA1.1.1357881239.1718854998; _ga_GTNB8BMG31=GS1.2.1718854999.1.1.1718856442.0.0.0; _ga_4QRFFGPLFT=GS1.1.1718854998.1.1.1718856746.0.0.0',
            'origin': 'https://affiliate.pocketoption.com',
            'priority': 'u=0, i',
            'referer': 'https://affiliate.pocketoption.com/en/login',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        yield Request(url=url, callback=self.parse_captcha, headers=headers, body=payload, method="POST")

    def parse_captcha(self, response):
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'lang=en; uuid=e4f9cf3b-3c2e-4f13-b491-9a6e0e28115e; no-login-captcha=1; guide=1; loggedIn=1; _gid=GA1.2.60535226.1718854998; brief-period=; _ga=GA1.1.1357881239.1718854998; _ga_GTNB8BMG31=GS1.2.1718854999.1.1.1718856442.0.0.0; laravel_session=eyJpdiI6Im81MzZ1WFdkMW9Sc1ZFUUxwMkFFc3c9PSIsInZhbHVlIjoiQ1I2Zm5BWFZwUmsvVnZIZlY1SCtoRUlBRURaSjVDclNWQkRRdUVFWUdMNXl5R3RXZjRoZTJxS0Y3UkFweTUwZWwzQXFUNVQ1dVZ6ZFBzU3pqNFYvMCtWaXpZczBNSGM4WWdSMUFvZjZPN3dUTHErQ05WSVlhUHhiTXdyQzc0VnQiLCJtYWMiOiJiNTM3NjNhMGI2NjFiNzk1YmQwZWY4M2Y3M2U4ZDdjNzk0OTViYWYwZmY4NWUxNjM1MWNlNGNiZDU4NTk0ZjVlIiwidGFnIjoiIn0%3D; _ga_4QRFFGPLFT=GS1.1.1718854998.1.1.1718856748.0.0.0',
            'priority': 'u=1, i',
            'referer': 'https://affiliate.pocketoption.com/en/dashboard',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        url = 'https://affiliate.pocketoption.com/en/statistics/brief/'
        yield Request(url=url, callback=self.parse_details, headers=headers)
        pass

    def parse_details(self, response):
        data = response.json()
        print(f"Visitor: {data.get('partnerVisits', '')}\n",
              f"Registrations: {data.get('partnerClients', '')}\n",
              f"FTD: {data.get('partnerFTDs', '')}\n",
              f"Deposits: {data.get('partnerDeposits', '')}\n",
              f"Withdrawals: {data.get('partnerClientsWithdrawals', '')}\n",
              f"Hold Commission: {data.get('partnerHoldCommission', '')}\n",
              f"Commission: {data.get('partnerCommission', '')}\n",
              f"Balance: {data.get('partnerBalance', '')}\n")

        message = "ℹ Pocket Affiliate Report\n"
        message += f"📥 Deposits: {data.get('partnerDeposits', '')}\n"
        message += f"📥 Withdrawals: {data.get('partnerClientsWithdrawals', '')}\n"
        message += f"👥 Visitor: {data.get('partnerVisits', '')}\n"
        message += f"📋 Registrations: {data.get('partnerClients', '')}\n"
        message += f"🔄 FTD: {data.get('partnerFTDs', '')}\n"
        message += f"🔀 Hold Commission: {data.get('partnerHoldCommission', '')}\n"
        message += f"💵 Commission: {data.get('partnerCommission', '')}\n"
        message += f"💰 Balance: {data.get('partnerBalance', '')}"

        payload = {'message': f'{message}'}
        response = requests.request("POST", "https://codewithninja.com/pocket-option-telegram-bot-2/webhook.php",
                                    data=json.dumps(payload))
        if response.status_code == 200:
            print("Message sent successfully")
        else:
            print("Message failed")
