---
layout: page
title:  "分类"
---

{% assign p_counter = 0 %}
{% for p in site.posts %}
  {% assign p_counter = p_counter | plus: 1 %}
{% endfor %}

嘿嘿，已经有 **{{ p_counter }}** 篇博客啦！

{% for c in site.categories %}
  {% assign my_counter = 0 %}
  {% for p in site.posts %}
    {%- if p.my_category == c.title -%}
      {% assign my_counter = my_counter | plus: 1 %}
    {%- endif -%}
  {% endfor %}
  <h3>
    <a href="{{ c.url }}">{{ c.title }}（{{ my_counter }}）</a>
  </h3>
{% endfor %}
