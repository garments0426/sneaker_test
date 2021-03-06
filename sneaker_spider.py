from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,datetime
import pandas as pd
import requests
import pymysql
from datetime import time,datetime
from fake_useragent import UserAgent



#-------網頁參數-----
ua= UserAgent(verify_ssl=False)
HEADERS={'user-agent' : str(ua.random),
        'cookie' :'__cfduid=d8bfdd7ef32ee56af1da3a8ce20fbc7291594311560; stockx_market_country=TW; _ga=GA1.2.1432156397.1594311562; _gid=GA1.2.1515132717.1594311562; _px_uAB=MTk5MnxmYWxzZQ==; _pxvid=f2ecd888-c1ff-11ea-923f-0242ac120007; _rdt_uuid=1594311563055.5031aa4f-4e67-471a-9847-d33d79ef1a95; _ALGOLIA=anonymous-e845000e-c694-4d9a-9e00-a93451854d6f; _gcl_au=1.1.2002678031.1594311564; tracker_device=524c35e3-dbd9-4073-8361-96bd6787d98e; _fbp=fb.1.1594311565790.1313580209; IR_gbd=stockx.com; ajs_anonymous_id=%2284d667db-d292-451e-8159-1561a5ab4059%22; _px_f394gi7Fvmc43dfg_user_id=ZjVhN2ZkNzAtYzFmZi0xMWVhLTkwZjYtODMyNWZmODJkNGVh; rskxRunCookie=0; rCookie=c8m6qeb2ulh83abjxt1ftkcezxz9y; language_code=en; stockx_selected_locale=en; stockx_selected_region=TW; stockx_dismiss_modal=true; stockx_dismiss_modal_set=2020-07-09T16%3A19%3A29.069Z; stockx_dismiss_modal_expiration=2021-07-09T16%3A19%3A29.069Z; is_gdpr=false; cookie_policy_accepted=true; stockx_ip_region=TW; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=v5; show_bid_education_times=1; multi_edit_option=beatLowestAskBy; show_watch_modal=true; intl_payments=true; bulk_shipping_enabled=false; below_retail_type=; bid_ask_button_type=; show_chatbot=false; riskified_recover_updated_verbiage=false; show_how_it_works=true; sell_ui_refresh=undefined; browse_page_tile_size_update_web=true; product_page_affirm_callout_enabled_web=false; stockx_seen_ask_new_info=true; stockx_product_visits=3; stockx_seen_bid_new_info=true; _dd_r=0; _gat=1; _pk_ses.421.1a3e=*; stockx_session=6f4098a0-cb9b-4939-b657-d83a318020fb; stockx_homepage=sneakers; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; IR_9060=1594323558702%7C0%7C1594323519510%7C%7C; IR_PI=f53565c7-c1ff-11ea-9384-42010a246105%7C1594409958702; _px3=64096217a9ea1e133594d1e94c078393aa07b04133ef18935bf563547c5dfc66:E+OSgKHBzmzaDPUiIY1cUXnXTIbJrtW5QFJwqsPYgBmnrADSJWUlgDgfL3sxVID6rJ5k85yBdtQrcyB4BFz8Xg==:1000:/M2TsHCUWtJqO7+KFq1sTKhvTIsNPIUZu3RHi6ebnIK+vKO9VfyWFIzQiDBjbE+yX7qjFSAIMHnzQGJFq12qM9z7NYsyXSkfwbtzJKFhyR/Y5jMBxPq/I5wKx4vgieRSyEVbiuEss9v+Fm9PAO/WyDDNIFvhiTTCHJVWUKJD/OQ=; _pk_id.421.1a3e=1e349f798e93de9d.1594311566.3.1594323559.1594315897.; default_apple_pay=false; related_products_length=v2; lastRskxRun=1594323560328; _px_7125205957_cs=eyJpZCI6ImM4ZmNhZWQwLWMyMWItMTFlYS1iMmM2LWViZGU4ZTY3OWE2ZiIsInN0b3JhZ2UiOnsiZyI6dHJ1ZX0sImV4cGlyYXRpb24iOjE1OTQzMjUzNjg0MTh9'
        }


PROXIES={
    'http' : 'http://175.44.108.183:9999',
    
    } 


#-------設定無頭參數-----
chrome_options= Options() #啟動無頭模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#-------起始網頁-----

url = 'https://stockx.com/new-releases/sneakers?page=1'


#-------web_driver-------- 未寫完
def driver(self):
    chromedriver= '/Library/Frameworks/Python.framework/Versions/3.8/bin/chromedriver'
    driver= webdriver.Chrome(executable_path= chromedriver, chrome_options= chrome_options)
    driver.get(url)
    
    return driver.page_source    
    
        

    
        


#---------數據分析--------
def web_analysis(self):
    try:
        json_data_list = json_data['Products']
        for data in json_data_list:
            brand = data['brand']  #品牌
            title = data['shortDescription'] #名稱
            styleid = data['styleId'] #型號
            releasedate = data['releaseDate'] #發售時間
            price = data['retailPrice'] #發售價錢
            try:
                image = requests.get(data['media']['thumbUrl'], headers= HEADERS).content #圖片二進制路徑
            except:
                print('null')
            data_dict = pd.Series([brand, title, styleid, releasedate, price, image],index = ['brand','title','styleid','releasedate','price','image'])
    except :
        print('分析失敗')    
    time.sleep(1)

#--------------------------------



#-----資料保存在sql函式---- 有問題
def database(data_list):
    conn = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = '',db = 'text',charset = 'utf8',)
    print('mysql connect OK!!')
    with conn.cursor() as cursor:
        CreateDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = '''
        REPLACE INTO sneaker_new,
        (brand, title, id, releasedate, price, image, caratedate,),
        VALUES
        (data_brand, data_title, data_id, data_releasedate, data_price, data_image, str(CreateDate)),
        '''
        try:
            cursor.execute(sql)
            conn.commit()
            print('寫入完成')
        except:
            conn.rollback()
            print('Error!!!')
    cursor.close() #關閉鼠標
    conn.close() #關閉連線
    print('連線結束')

#-----------------------

xx=driver(url)
print(xx)