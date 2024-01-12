## TODOS ##
- ~~Implement Logging~~
- Implement authentication for making management requests
- Comments
  - Comment checking (for profanity)
  - Flagging users/ips 
  - reporting system
    - email alerts/notifications 
- Logging how many/who is loading pages
- Re-secure endoints
  - Make sure all calls on comic controller are coming from the website
  - Plan for Admin panel endpoint security
- Write deployment script in python for updating the angular and java apps on the server

# Admin Panel
I think I have decided that the admin panel will be an angular app or a python app

## Python App

### Pros
- You don't have to sign into a website to use it.
- The backend could require a single encrypted keyword which the python app can include in it's http requests
- Would not have to host like an angular app
- A deployment function could be built into the app for updating the website
  - I do not have a good experience of mixing python and remote SSH
- Batch uploading
  - This is the biggest boon. I can easily modify multiple pages in Clip Studio Pro and then have a script look at their file names and determine which chapter the page belongs to. So then I can modify multiple pages and make big changes to the comic and efficiently update the website.

### Cons
- Intellij is very fussy with big python apps
- It might look ugly/ I do not know how to do many things involving lists in tkinter UI

## Angular App

### Pros
- Looks nice
- If this became a real "Product" or thing I can share with friends then they would probably really appreciate having access to an admin panel right in their web browser.
- 
### Cons
- Intellij is very fussy with big python apps
- I would have to come up with login security 😭
- Batch uploading would be much less possible