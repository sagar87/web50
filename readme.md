# C50W

## Git Lecture
### HTML
* `<!DOCTYPE html>` tells the browser that this file is an HTML file
* html consists in <tags></tags>
* indentation is optional
* headings: html has 6 different sizes for headings
    * `<h1>largest heading</h1>` ... `<h6></h6>`
* lists
    * `<ul><li>first item</li></ul>` unorderded list
    * `<ol><li>first item</li></ol>` orderded list
* images
    * `<img src="cat.jpg">` 
    * `src` is called a html attribute which contains the path to the picture
    * `height`, `width` attributes can change the dimension of the image in pixel, also accepts arguments like `50%` which allows the picture to resize automatically
* tables `<table>`
    * `<tr>` table row
    * `<th>` table head
    * `<td>` table data
* forms `<form>`
    ```
    <form>
        <input type="text", placeholder="full name">
        <button "">
    </form>
    ```
* Document object model - hierarchy in the file
    * `<html>`
        * `<head>`
            * `<title>`
        * `<body>`
            * `<h1>`
### CSS
* example for a header

```
<h1 style="color:blue;text-align:center;">welcome to my page</h1>
```

* CSS properties color and text-align
* with html color picker (in Google) we can pick exact hexcodes for each color
* in this way however CSS and html code get mixed

```
<!DOCTYPE html> 
<html>
    <head>
        <title>My Web page!</title>
        <style>
            h1 {
                color: blue;
                text-align: center;
            }
        </style>
    </head>
    <body>
        Hello World!
    </body>
</html>
```

* here we put the style for h1 headers into the header which changes for all headings the color and alignment
* we can even put the css code into a seperate file (define in `<head>`)

```
<link rel="stylesheet" href="styles.css">
```

* `<div>` are arbitrary sections of the page

```
<!DOCTYPE html> 
<html>
    <head>
        <title>My Web page!</title>
        <style>
            table {
                border 2px solid black;
                bordercollapse collapse;
                width: 50%;
            }
            th, td {
                border: 1px solid black;
                padding: 5px;
                text-align: center;
            }
            th {
                background-color: light-grey;
            }
            div {
                font-family: Arial, sans-serif;
                font-size: 28px;
                font-weight: bold;
                color: blue;
                text-align: center;
                margin: ;
                padding: ;
                border: 5px dotted red;
            }
        </style>
    </head>
    <body>
        <div>
        Some text
        </div>
    </body>
</html>
```

* digging deeper intor div and span
    * `id` attributes allow to name divs, can only be used once in a HTML
    *  `span ` has the attributes `class` which can be used more often

```
<!DOCTYPE html> 
<html>
    <head>
        <title>My Web page!</title>
        <style>
            #top {
                font-size:36;
            }
            #middle {
                font-size:24;
            }
            #bottom {
                font-size:16;
            }            
            .name {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div id="top">
            This is the <span class="name"> top</span> of my page.
        </div>
        <div id="middle">
            This is the <span class="name">middle</span> of my page.
        </div>
        <div id="bottom">
            This is the <span class="name">bottom</span> of my page.
        </div>
    </body>
</html>
```

## Lecture 2: Python and JavaScript

