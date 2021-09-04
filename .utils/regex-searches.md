# Searches

## glightbox

### Example
{{< glightbox src="https://media.bennorris.org/images/gospelsketcher/uploads/2020/7eda015c96.jpg" alt="Conference sketchnotes" gallery="apr-2020">}}

### Regex
#### Find
\{\{< glightbox src="(.+?)".+?alt="(.+?)".+?>\}\}

#### Replace
![$2]($1){:loading="lazy"}


## MWH Links

### Example
(https://www.mentalworkhealth.org/2020/11/02/loss-and-uncertainty.html) and more things with (testing.html)

### Regex
#### Find
\(https://www\.mentalworkhealth\.org/(\d{4})/(\d{2})/(\d{2})/([^.]*)\.html[^)]*\)

#### Replace
({% post_url $1-$2-$3-$4 %})


## Post URL Links

### Example
{% post_url 2013-12-08-my-own-cars-moment %} With more things {% testing %}

### Regex
#### Find
\{% post_url (\d{4})-(\d{2})-(\d{2})-(\S*) %\}

#### Replace
https://bennorris.org/$1/$2/$3/$4/


## Wrong date

(Have to then manually look at each one and replace the date and hour)

### Example
date:       2020-05-05 03:02:47-0000
date: 2020-05-06 03:02:47-0700
date: 2020-05-06 03:02:47-0000

### Regex
#### Find
(date:\s*\d{4}-\d{2}-)(\d{2})\s(\d{2})(:\d{2}:\d{2})-0000

#### Replace
$1XX XX$4-0700
