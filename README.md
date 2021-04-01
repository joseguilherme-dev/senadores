# **Senators Webcrawler**

<img src='runtime.svg'></img>

This is my first webcrawler ever made using **Scrapy**.

It's goal is to get the following informations about each active senator of Brazil:

- URL of his public page;
- Name of the senator;
- State where the senator was elected;
- Period of activity;
- Party;
- Cabinet phones;
- Cabinet address;
- Senator email.

After that, all the data scrapped is sent to a MongoDB database.

---

## **How to Run**

First of all, you must have MongoDB running on your localhost.

You also need to install the requirements that are in the `requirements.txt` file, that should be easy with the pip command:

```
pip install -r requirements.txt
```

After that, just run the crawler with:

```
scrapy crawl senators_spider
```

---

## License:

This project is licensed under the MIT License - see the <a href='LICENSE.md'>LICENSE</a> file for details.