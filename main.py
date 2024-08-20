from googleapiclient.discovery import build
from googlesearch import search

def search_youtube_links(text, api_key, max_results=10):
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        search_response = youtube.search().list(
            q=text,
            part="id",
            maxResults=max_results
        ).execute()

        youtube_links = []
        for item in search_response.get("items", []):
            if item["id"]["kind"] == "youtube#video":
                video_id = item["id"]["videoId"]
                youtube_links.append(f"https://www.youtube.com/watch?v={video_id}")

        if youtube_links:
            print("YouTube links:")
            for link in youtube_links:
                print(link)
            return youtube_links
        else:
            print("No YouTube links found for:", text)
            return []

    except Exception as e:
        print("Error finding YouTube links:", e)
        return []

def search_web_links(text):
    try:
        search_results = search(text, num_results=5)
        web_links = list(search_results)
        if web_links:
            print("Web links:")
            for link in web_links:
                print(link)
            return web_links
        else:
            print("No web links found for:", text)
            return []
    except Exception as e:
        print("Error finding web links:", e)
        return []

if __name__ == "__main__":
    api_key = input("Enter your YouTube Data API key: ")
    search_text = input("Enter text to search on YouTube and the web: ")
    youtube_links = search_youtube_links(search_text, api_key)
    web_links = search_web_links(search_text)
