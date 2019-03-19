from collections import Counter as CT
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://www.facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png"
]

urls = [url.split("/")[-1] for url in urls]
counted = CT(urls).most_common(3)
for file , count in counted:
    print(file,count)