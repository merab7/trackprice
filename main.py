import requests
from bs4 import BeautifulSoup
import smtplib
import os
import lxml


my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")
        



header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response  = requests.get(url, headers=header)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "lxml")
price_text = soup.find(name="span", class_="aok-offscreen").get_text()
price = float(price_text.split("$")[1])
print(price)

if price < 100 :

    with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)

                # Encode the message using UTF-8
                subject = "Price is low"
                body = f"Hello, your Pot Duo Plus 9 price is :{price} \nsee on link : {url}  "
                msg = f"Subject: {subject}\n\n{body}"

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="merabtoduapy@gmail.com",
                    msg=msg.encode('utf-8')
                )

                print("Email sent to merabtoduapy@gmail.com")