from tiktokapi import TikTokApi

# TikTok API'ya erişmek için kullanılacak kimlik bilgileri
api = TikTokApi.get_instance(use_selenium=True)

# Videonun URL'si
video_url = "video link"

# Videoyu almak için TikTok API'sini kullanın
video_id = api.get_video_by_url(video_url)

# Videoyu paylaşmak için TikTok API'sini kullanın
api.upload_video("Yeniden paylaşılan video açıklaması", video_id)
