# **Senators Webcrawler**

<img src='runtime.svg'></img>
<img src='database.svg'></img>
<img src='docker.svg'></img>
<img src='license.svg'></img>

This is my first webcrawler ever made using **Scrapy** library.

It's goal is to get the following informations about each active senator of Brazil:

- URL of his public page;
- Name of the senator;
- State where the senator was elected;
- Period of activity;
- Party;
- Cabinet phones;
- Cabinet address;
- Senator email.

After that, all the data scrapped is sent to a **MongoDB** database.

---

## **How to Run:**

You need to have `docker` and `docker-compose` properly installed on your machine.

That way, we can execute the senators webcrawler by simply running the following command: 

```
docker-compose up
```

It will build the crawler and Mongo docker images and right after that it launches them.


---

## License:

This project is licensed under the MIT License - see the <a href='LICENSE.md'>LICENSE</a> file for details.