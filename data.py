import urllib.request
import bs4
import ssl
import pandas as pd

# get data which not consider the login

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    # 浏览器
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

# 网址 (url)
url = "https://stockx.com/air-jordan-1-retro-high-white-university-blue-black"
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
# html
text = response.read().decode()
html = bs4.BeautifulSoup(text, 'html.parser')
# 储存最新价格的表格（table store the latest price
content = html.find_all("div", class_="latest-sales-container")
print(content)
df = pd.read_html(req)[0]
print(df)

# Cookies (use for login)
cookies = '_ga=GA1.2.248218820.1608350127; _pxvid=0899bb0f-41ae-11eb-b619-0242ac120007; ' \
          'tracker_device=aecfba50-9942-414a-a473-362be7b152ba; ' \
          '_scid=ac9107b6-577b-49fe-a744-ca03211144fb; _' \
          'fbp=fb.1.1608350146353.765582053; QuantumMetricUserID=6f8bb99ec455180de50965cfd2d71505;' \
          ' rskxRunCookie=0; rCookie=de7dmgupyy5im2qyhjgntpkiv65wpk; ' \
          'ajs_anonymous_id="642e12c1-9c62-45fe-9c03-d338e288b101"; _' \
          'px_f394gi7Fvmc43dfg_user_id=OGY1MmE4NjAtNzFjZi0xMWViLTg1MjAtYWY5ZjA1NjQ3MDU0; ' \
          'ajs_user_id="05396906-3783-11ea-8d77-124738b50e12"; stockx_dismiss_modal=true; ' \
          'stockx_dismiss_modal_set=2021-03-12T13:26:40.566Z; ' \
          'stockx_dismiss_modal_expiration=2022-03-12T13:26:40.565Z;' \
          ' __cfduid=d750fc5a487e04800593e2e24c98596411616395231; ' \
          '_gcl_au=1.1.816706639.1616395240; stockx_experiments_id=web-75b1dbc8-8c46-4074-940f-127a14451f4e; ' \
          'language_code=en; stockx_market_country=HK; IR_gbd=stockx.com; ' \
          'below_retail_type=; brand_tiles_version=v1; ' \
          'default_apple_pay=false; product_page_affirm_callout_enabled_web=false; ' \
          'related_products_length=v2; riskified_recover_updated_verbiage=true; ' \
          'show_all_as_number=false; show_how_it_works=true; recently_viewed_web_home=false; ' \
          'salesforce_chatbot_prod=true; home_vertical_rows_web=true; ' \
          'ops_banner_id=blteaa2251163e21ba6; stockx_default_sneakers_size=6; ' \
          'QuantumMetricSessionID=8cd31de738f4c70074b114a534d4b7aa; qmexp=1618326406420; ' \
          '_gid=GA1.2.1507601497.1618721610; ' \
          'ajs_group_id="ab_buy_now_rage_click_android.false,' \
          'ab_ios_enable_suggested_addresses.false,ab_ios_seller_profile_redesign.novariant,' \
          'ab_multiask_redesign_android_v2.false,ab_product_page_refactor_android_v2.false,' \
          'ab_product_page_refactor_ios_v3.false,ab_seller_profile_redesign_android.false,' \
          'ab_test_product_page_refactor_web.false,ab_web_genesis_v3.false"; ' \
          'stockx_selected_currency=HKD; stockx_homepage=sneakers; show_watch_modal=true; ' \
          'stockx_session=9e253e63-c588-4674-ae71-e17356c8db39; ' \
          '_pk_ref.421.1a3e=["","",1618732745,"https://www.google.com/"]; ' \
          '_pk_ses.421.1a3e=1; ' \
          'com.auth0.auth.{"state":{"forceLogin":true}}={"nonce":null,"state":"{\"state\":{\"forceLogin\":true}}",' \
          '"lastUsedConnection":"production"}; stockx_product_visits=6; ' \
          '_px3=56530162ce73158c2d7b2e0ddcf4813733579d0e16080f62ddb41b9711c97619:' \
          'JcMJgM7qe6IJEIu85ppluMTDlMXImiStmJNXOvPglfeIsgaDd/RaTKCI0DsK32YaPp68I73ndvmXzJ4FXEgGuQ==:' \
          '1000:uZ3/X1ZYu5r61k2lthVS2kkvqTNTo1U9nWFwqRVQtNGpkSGQZk/MPFTNWlfZpW25EI4Yg+H8MMmSr+' \
          'RsyD7f89hTCTTNtkH6lAVWyBELFOcqotk4mbxNkVINItcbj/FWSUzl7rElel0gtEAf60iD28wUEkCO+9DTwUGqhm4Dkcc=; ' \
          '_pk_id.421.1a3e=6f90592a21e6bde1.1608350146.19.1618732878.1618732745.; ' \
          'IR_9060=1618732878115|0|1618732878115||; ' \
          'IR_PI=54cd837b-1d91-11eb-b1aa-42010a246308|1618819278115; ' \
          'lastRskxRun=1618732879296; ' \
          '_px_7125205957_cs=' \
          'eyJpZCI6ImIwMDAyMWIwLWEwMTgtMTFlYi04NTA4LTYzZDAyZjA2NWRhZiIsInN0b3JhZ2UiOnt9LCJleHBpcmF0aW9uIjoxNjE4NzM0Njg3NzkzfQ==; ' \
          '_dd_s=rum=0&expire=1618733855740'


