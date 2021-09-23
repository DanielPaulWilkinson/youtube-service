# youtube-service
A microservice that uses a python web scraper to scrape the YouTube trending page for all videos. Written in Node.js using Python &amp; various packages. Consumed by the never-late-again Vue.js application.

# Dependencies
- BeautifulSoup4 (Python)
- Selenium Web Driver (Python)
- Simply call npm i in the node application to install all dependencies (Node.js) 

# routes
- /about - simple information about microservice
- /trending - forces the python script to run and then returns the json in the response. 
