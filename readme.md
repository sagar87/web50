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
