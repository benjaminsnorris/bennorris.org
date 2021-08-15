---
layout: page
title: Writing
---

One of the greatest technologies we have for communicating with each other is the written word. While I am not a professional writer, I constantly aspire to be better.

## [bennorris.blog](http://bennorris.blog)

My personal blog is a place for me to share whatever is on my mind. Much of what I write here is related to parenting, leadership, or mental health.


## [mentalworkhealth.org](https://mentalworkhealth.org)

This is a passion project of mine. I deal with severe OCD, and have found that as I share about my experiences, I understand them better, and it creates space for others to share their story as well. So that it’s easier to remember, you can find my story at [mwh.is/personal](http://mwh.is/personal).


<div class="post">
  <div class="post-content">
    <div class="posts">
      {% for post in site.posts %}
          <div class="post py3">
            <a href="{{ post.url | prepend: site.baseurl }}" class="post-link"><h3 class="post-title">{{ post.title }}</h3></a>
            <p class="post-meta">{{ post.date | date: site.date_format }}</p>
            <p class="post-summary">
              {% if post.introduction %}
                {{ post.introduction }}
              {% else %}
                {{ post.excerpt }}
              {% endif %}
            </p>
          </div>
      {% endfor %}
    </div>
  </div>
</div>
