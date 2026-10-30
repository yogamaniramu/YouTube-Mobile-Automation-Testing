
import time


from pageObjects.youtube_page import YouTubePage
from pageObjects.video_page import VideoPage




def test_search_and_play_video(driver):
    youtube_page=YouTubePage(driver)
    youtube_page.click_search_button()
    print("search button clicked successfully")
    print(driver.page_source)
    youtube_page.click_search_box("python")
    print("search text entered successfully")
    video_page=VideoPage(driver)
    video_page.click_python_video()
    time.sleep(5)
    video_page.skip_ad_if_present()
    time.sleep(5)
    video_page.go_back_to_results()
    time.sleep(5)
    video_page.close_play_video()
    time.sleep(5)
    video_page.scroll_results()
    time.sleep(5)
    video_page.click_next_video()
    time.sleep(5)
