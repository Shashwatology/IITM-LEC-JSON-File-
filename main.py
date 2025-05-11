import json

with open('playlistExport.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

output = []
for item in data:
    output.append({
        "id": "",
        "title": item.get("title", ""),
        "link": item.get("videoUrl", "")
    })

with open('reformatted_playlist.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
print("Reformatted playlist saved to 'reformatted_playlist.json'")

















































# This script reformats a JSON playlist export from YouTube to a simpler format.
# It reads the original JSON file, extracts the title and video URL from each item,
# and saves the reformatted data to a new JSON file.
# The reformatted JSON file has the following structure:
# [
#     {
#         "id": "",
#         "title": "Video Title",
#         "link": "https://www.youtube.com/watch?v=VIDEO_ID"
#     },
#     ...
# ]
# The "id" field is left empty as it is not provided in the original data.
# The "title" field contains the title of the video, and the "link" field contains the URL to the video.    