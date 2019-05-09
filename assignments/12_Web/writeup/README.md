# Crypto II Writeup

Name: **
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (40 Pts)

### Part 2 (60 Pts)

1. I typed the follwing script into the searchbar. This directed the webpage to display the script as a query because search results were not sanitized.

```html
<script>alert("This is XSS");</script>
```

2. I inserted the follwing image into the comment bar. This set the image link to a nonexistent empty link and set the function called after a error with loading the image to trigger the popup dialog. The message box needs to escape the contents of status messages to prevent this issue.

```html
<img src="" onerror="alert('This is XSS')"></img>
```

3. The site does not sanitize the variable value for num (used to find which image to display) so we can exploit it by setting the value of num to a string literal containing a number and quote and set the remaining string to the onerror attribute to trigger the popup. The url is shown below.

```html
https://xss-game.appspot.com/level3/frame#1' onerror='alert("This is XSS")'
```

4.

5.

6.

*Your reflection goes here*
