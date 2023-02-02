import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
youtube_url = 'https://www.youtube.com/feed/trending'


def get_driver():
    print("Getting driver ")
    driver = webdriver.Chrome()
    return driver

def get_videos(driver):
    driver.get(youtube_url)
    videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer") 
    return videos

def parse_videos(videos):
    title_tag = videos.find_element(By.ID, "video-title")
    title = title_tag.text

    url = title_tag.get_attribute('href')
   # thumbnail_url = videos.find_element(By.XPATH, '//div[@class="style-scope ytd-video-renderer"]///img').get_attribute('src')
    thumbnail_url = videos.find_element(By.CSS_SELECTOR, "ytd-thumbnail yt-image>img").get_attribute('src')
    videos_info = videos.find_element(By.CLASS_NAME, 'style-scope ytd-video-meta-block').text
    videos_info = videos_info.strip().split('\n')
    if len(videos_info)%2 == 0 :
       channel_name = videos_info[0]
       videos_views = videos_info[2]
       videos_days = videos_info[3]
    else :
        channel_name = videos_info[0]
        videos_views = videos_info[1]
        videos_days = videos_info[2]
    description = videos.find_element(By.ID, 'description-text').text
    return {
        'title':title,
        'video url':url,
        'thumbnail_url':thumbnail_url,
        'channel_name': channel_name,
        'videos views': videos_views,
        'videos uploaded': videos_days,
        'description':description
    }
if __name__ == "__main__":
    driver = get_driver()
    videos = get_videos(driver)
    print("Parsing Top trending videos")
    trending_videos = [parse_videos(video) for video in videos]
    
    trend_videos_df = pd.DataFrame(trending_videos)
    trend_videos_df.to_csv('Web Scrapping/trending_videos.csv', index=False)
     