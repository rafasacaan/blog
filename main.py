from fasthtml.common import *

import markdown
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

from pathlib import Path
import frontmatter
import markdown
from datetime import datetime


app, rt = fast_app(
    hdrs=(
        MarkdownJS(),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Open+Sans:wght@400;600&display=swap"),    
        
        # Search bar javascript
        Script("""
            function filterPosts() {
                const query = document.getElementById('search').value.toLowerCase();
                const posts = document.querySelectorAll('.blog-list li');
                
                posts.forEach(post => {
                    const title = post.querySelector('.post-title').textContent.toLowerCase();
                    const description = post.querySelector('p') ? 
                        post.querySelector('p').textContent.toLowerCase() : '';
                    
                    if (title.includes(query) || description.includes(query)) {
                        post.style.display = '';
                    } else {
                        post.style.display = 'none';
                    }
                });
            }
        """),

        # Web css
        Style("""            
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
            .blog-title h1 { color: darkgrey; }
            .blog-post { max-width: 800px; margin: 2rem auto; }
            .blog-post h1 { color: #ff00ff; background: #ffdb00;}
            .blog-list { padding: 0; }
            .blog-list li {list-style-type: decimal-leading-zero;}
            .post-date { color: #666; font-size: 0.9rem; margin-bottom: 1rem; }
            .post-title { margin-bottom: 0.5rem; color: darkgrey; background: none;}
            .post-title a {color: #ff00ff; background: #ffdb00;}
              
            /* Search bar styles */
            .search-container {
                max-width: 800px;
                margin: 2rem auto 1rem;
            }
            .search-container input {
                width: 100%;
                padding: 0.5rem;
                font-size: 1rem;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-family: sans-serif;
            }
            .search-container input:focus {
                outline: none;
                border-color: darkgreen;
            }
              
            # code, kbd, pre {
            #   background: #373737;
            #   color: #ffffff;
            # }
                      
        """),    
    )
)

# Directory where markdown files are stored
POSTS_DIR = Path("posts")
POSTS_DIR.mkdir(exist_ok=True)

def get_posts():
    """Get all posts sorted by date"""
    posts = []
    for file in POSTS_DIR.glob("*.md"):
        # Get post content and metadata using frontmatter
        with open(file) as f:
            post = frontmatter.load(f)
            post.metadata['url'] = f"/post/{file.stem}"
            post.metadata['date'] = post.metadata.get('date', datetime.fromtimestamp(file.stat().st_mtime))
            posts.append(post)
    return sorted(posts, key=lambda x: x.metadata['date'], reverse=True)


@rt("/")
def get():
    # Get all posts
    posts = get_posts()

    # Render posts
    content = Div(        
        H1("rafa sacaan"),
        P("""
          hola, mi nombre es rafa, soy data scientist y voy a empezar a juntar mis notas por acá. 
          espero que estos pedazos de conocimiento sean de ayuda para alguien más también!
        """),
        # Add search bar
        Div(
            Input(
                type="text", 
                id="search", 
                placeholder="Busca tu post...",
                oninput="filterPosts()"
            ),
            cls="search-container"
        ),
        Ul(
            *[Li(
                H3(A(post.metadata['title'], href=post.metadata['url']), cls="post-title"),
                Div(post.metadata['date'].strftime("%B %d, %Y"), cls="post-date"),
                P(post.metadata.get('description', ''))
            ) for post in posts],
            cls="blog-list"
        ),
        cls="blog-title"
    )
    return Title("rafasacaan"), content


@rt("/post/{slug}")
def get(slug: str):
    try:
        file = POSTS_DIR / f"{slug}.md"
        with open(file) as f:
            post = frontmatter.load(f)
            
            # content = Div(
            #     H1(post.metadata['title']),
            #     Div(post.metadata['date'].strftime("%B %d, %Y"), cls="post-date"),
            #     Div(NotStr(markdown2.markdown(
            #         post.content,
            #         extras=['fenced-code-blocks', 'code-friendly', 'tables']
            #     )), cls="markdown-content"),
            #     A("← Back to Home", href="/"),
            #     cls="blog-post"
            # )
            
            md = markdown.Markdown(extensions=[
                'fenced_code',
                'codehilite',
                'tables',
                'extra'
            ], extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'use_pygments': True,
                    'noclasses': True,  # This is important - it inlines the CSS
                    'pygments_style': 'friendly'
                }
            })
            
            content = Div(
                H1(post.metadata['title']),
                Div(post.metadata['date'].strftime("%B %d, %Y"), cls="post-date"),
                Div(NotStr(md.convert(post.content)), cls="markdown-content"),
                A("← Back to Home", href="/"),
                cls="blog-post"
            )

            return Title("rafasacaan"), content
        
    except FileNotFoundError:
        return H1("Post not found")

if __name__ == "__main__":
    serve()