from pathlib import Path
import shutil
import frontmatter
import markdown
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# Create templates directory if it doesn't exist
templates_dir = Path("templates")
templates_dir.mkdir(exist_ok=True)

# Create template files
base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rafasacaan</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Open+Sans:wght@400;600&display=swap">
    <style>
        body { 
            font-family: sans-serif; 
            line-height: 1.6;
        }
        h1, h2, h3, .post-title { 
            font-family: 'Lora', serif;
            font-weight: 700;
        }
        a { text-decoration: none; }
        .blog-title { max-width: 800px; margin: 2rem auto; }
        .blog-title h1 { color: darkgreen; }
        .blog-post { max-width: 800px; margin: 2rem auto; }
        .blog-post h1 { color: darkgreen; background: none; }
        .blog-list { padding: 0; }
        .blog-list li {list-style-type: decimal-leading-zero;}
        .post-date { color: #666; font-size: 0.9rem; margin-bottom: 1rem; }
        .post-title { margin-bottom: 0.5rem; color: darkgrey; background: none;}
        .post-title a {color: darkgray;}
    </style>
</head>
<body>
    <main class="container">
        {% block content %}{% endblock %}
    </main>
</body>
</html>
"""

index_template = """
{% extends "base.html" %}

{% block content %}
<div class="blog-title">
    <h1>rafa sacaan</h1>
    <p>
        hola, mi nombre es rafa, soy data scientist y voy a empezar a juntar mis notas por acá. 
        espero que estos pedazos de conocimiento sean de ayuda para alguien más también!
    </p>
    <ul class="blog-list">
    {% for post in posts %}
        <li>
            <h3 class="post-title"><a href="{{ post.url }}">{{ post.title }}</a></h3>
            <div class="post-date">{{ post.date.strftime("%B %d, %Y") }}</div>
            {% if post.description %}
            <p>{{ post.description }}</p>
            {% endif %}
        </li>
    {% endfor %}
    </ul>
</div>
{% endblock %}
"""

post_template = """
{% extends "base.html" %}

{% block content %}
<div class="blog-post">
    <h1>{{ post.title }}</h1>
    <div class="post-date">{{ post.date.strftime("%B %d, %Y") }}</div>
    <div class="markdown-content">
        {{ post.content | safe }}
    </div>
    <p><a href="index.html">← Back to Home</a></p>
</div>
{% endblock %}
"""

# Write templates
(templates_dir / "base.html").write_text(base_template)
(templates_dir / "index.html").write_text(index_template)
(templates_dir / "post.html").write_text(post_template)

# Create output directory
dist_dir = Path("dist")
if dist_dir.exists():
    shutil.rmtree(dist_dir)
dist_dir.mkdir()

# Set up Jinja2
env = Environment(loader=FileSystemLoader("templates"))

# Get all posts
posts_dir = Path("posts")
posts = []
for file in posts_dir.glob("*.md"):
    with open(file) as f:
        post = frontmatter.load(f)
        # Change URL format to match the static site structure
        post.metadata['url'] = f"{file.stem}.html"
        post.metadata['date'] = post.metadata.get('date', datetime.fromtimestamp(file.stat().st_mtime))
        post.metadata['content'] = markdown.markdown(post.content)
        posts.append(post.metadata)

# Sort posts by date
posts.sort(key=lambda x: x['date'], reverse=True)

# Generate post pages
template = env.get_template("post.html")
for post in posts:
    output = template.render(post=post)
    (dist_dir / post['url']).write_text(output)

# Generate index page
template = env.get_template("index.html")
output = template.render(posts=posts)
(dist_dir / "index.html").write_text(output)

print("Static site built successfully!")