---
layout: default
---

<div class="posts">
  <h1 class="content-subhead">TV Shows</h1>
</div>

I quite enjoy good television shows. Some of them so much that I recommend them
to others. I'm very selective about my recommendations, so the list below
represents only "hands down" great television shows.

Having seen my favorite shows, is there a show you think I'd like?
[Let me know](mailto:tim@timwis.com)!

{% assign shows = site.data.shows | sort: 'title' %}
<ul>
  {% for show in shows %}
  <li>
    <a href="{{ show.url }}">
      {{ show.title }}
    </a>
  </li>
  {% endfor %}
</ul>
