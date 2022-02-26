# Web Scraper

# Introduction

Using this project, you’ll be able to extract the first 30 entries from https://news.ycombinator.com/.

And select one of the following operations over that data:

-> Filter all previous entries with more than five words in the title ordered by the number of comments first.
-> Filter all previous entries with less than or equal to five words in the title ordered by points.

# How to launch it

You must have docker installed in your machine. Then, execute the following commands in the command prompt:

```Bash
    docker build . -t flask_app
    docker run  --shm-size="2g" -d -p 5000:5000 flask_app
```

Finally, go a web browser and look for the following url, localhost:5000