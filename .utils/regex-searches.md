# Searches

## glightbox

### Example
{{< glightbox src="https://www.gospelsketcher.org/uploads/2020/7eda015c96.jpg" alt="Conference sketchnotes" gallery="apr-2020">}}

### Regex
#### Find
`\{\{< glightbox src="(.*)" alt="(.*)" .*>\}\}`

#### Replace
`![$2]($1){:loading="lazy"}`

