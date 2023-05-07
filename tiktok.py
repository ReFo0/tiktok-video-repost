from tiktokapi import TikTokApi

api = TikTokApi.get_instance(use_selenium=True)

video_url = "video link"

video_id = api.get_video_by_url(video_url)

api.upload_video("video description", video_id)
