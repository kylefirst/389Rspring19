# Crypto II Writeup

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (40 Pts)

To show all the items on the website included unlisted ones, I injected an or operator with a statement that is always true in the url ```http://1337bank.money:5000/item?id='||'a'='a```. I found the flag ```CMSC389R-{y0u_ar3_th3_SQ1_ninj@}``` listed for $1337.

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

4. The onload function for the timer is reading in the value from the input box as a string without sanitizing for quotes so we can inject a popup dialog by closing the start timer function and adding an additional call to ```alert()```. The following text was entered into the timer text box.

```html
'); alert('XSS
```

5. After inspecting the code for the next hyperlink where you enter your email, I found that it uses the value in the ```?next``` parameter in the URL so setting that to a javascript alert will display the popup when next is pressed. The URL is shown below.

```html
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('This is XSS');
```

6. The website will load anyscript after the # in the url so in order to inject the alert I injected the javascript alert script as text.

```html
https://xss-game.appspot.com/level6/frame#data:,alert('This is XSS')
```
