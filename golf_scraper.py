from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import pandas as pd
import time


output_file = "player_data_result.csv"
driver = webdriver.Chrome()
driver.get("")
elem1 = driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[2]/main/section/div/div/div/div/div[1]/div[2]/div[3]/input")
elem1.click()
elem1.clear()
time.sleep(4)
soup = BeautifulSoup(driver.page_source, "lxml")
table_tag = soup.find("table", {"class", "table table-hover table-condensed table-responsive ranking-table"})
# print(table_tag)
trs = table_tag.tbody.find_all("tr", {"current-page": "currentPage"})
data = []
for tr in trs:   
    player_name = ""
    rating = ""
    event = ""
    rank = ""
    vs_top_10_w = ""
    vs_top_10_l = ""
    vs_top_10_t = ""
    vs_top_50_w = ""
    vs_top_50_l = ""
    vs_top_50_t = ""
    vs_top_100_w = ""
    vs_top_100_l = ""
    vs_top_100_t = ""
    vs_overall_w = ""
    vs_overall_l = ""
    vs_overall_t = ""

    tds = tr.find_all("td") #
    player_name = tds[2]
    # players_name.append(player_name)
    rating = tds[6].text
    # ratings.append(rating)
    event = tds[7].text
    # events.append(event)
    rank = tds[8].text
    # ranks.append(rank)
    vs_top_10_w = tds[9].text
    # vs_top_10_ws.append(vs_top_10_w)
    vs_top_10_l = tds[10].text
    # vs_top_10_ls.append(vs_top_10_l)
    vs_top_10_t = tds[11].text
    # vs_top_10_ts.append(vs_top_10_t)
    vs_top_50_w = tds[12].text
    # vs_top_50_ws.append(vs_top_50_w)
    vs_top_50_l = tds[13].text
    # vs_top_50_ls.append(vs_top_50_l)
    vs_top_50_t = tds[14].text
    # vs_top_50_ts.append(vs_top_50_t)
    vs_top_100_w = tds[15].text
    # vs_top_100_ws.append(vs_top_100_w)
    vs_top_100_l = tds[16].text
    # vs_top_100_ls.append(vs_top_100_l)
    vs_top_100_t = tds[17].text
    # vs_top_100_ts.append(vs_top_100_t)
    vs_overall_w = tds[18].text
    # vs_overall_ws.append(vs_overall_w)
    vs_overall_l = tds[19].text
    # vs_overall_ls.append(vs_overall_l)
    vs_overall_t = tds[20].text
    # vs_overall_ts.append(vs_overall_t)
    
    

# for d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16 in zip(players_name, ratings,events,ranks,vs_top_10_ws,vs_top_10_ls,vs_top_10_ts,vs_top_50_ws,vs_top_50_ls,vs_top_50_ts,vs_top_100_ws,vs_top_100_ls,vs_top_100_ts,vs_overall_ws,vs_overall_ls,vs_overall_ts):
    data.append({

        "players_name":player_name,
        "ratings": rating,
        "events":event,
        "ranks": rank,
        "vs_top_10_ws": vs_top_10_w,
        "vs_top_10_ls": vs_top_10_l,
        "vs_top_10_ts":vs_top_10_t,
        "vs_top_50_ws":vs_top_50_w,
        "vs_top_50_ls":vs_top_50_l,
        "vs_top_50_ts":vs_top_50_t,
        "vs_top_100_ws":vs_top_100_w,
        "vs_top_100_ls":vs_top_100_l,
        "vs_top_100_ts":vs_top_100_t,
        "vs_overall_ws":vs_overall_w,
        "vs_overall_ls":vs_overall_l,
        "vs_overall_ts":vs_overall_t

    })
print(data)
if data:
    df = pd.DataFrame(columns=
        [   "players_name",
            "ratings",
            "events",
            "ranks",
            "vs_top_10_ws",
            "vs_top_10_ls",
            "vs_top_10_ts",
            "vs_top_50_ws",
            "vs_top_50_ls",
            "vs_top_50_ts",
            "vs_top_100_ws",
            "vs_top_100_ls",
            "vs_top_100_ts",
            "vs_overall_ws",
            "vs_overall_ls",
            "vs_overall_ts"
        ])
    df = df.append(data, ignore_index=True)
    df.to_csv(output_file, index=False)

    
driver.close()



