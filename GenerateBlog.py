# Write a program that generates a blog

def generate_blog(title, content):
    blog = f"# {title}\n\n{content}\n"
    return blog

title = input("Enter the blog title: ")
content = input("Enter the blog content: ")
blog_post = generate_blog(title, content)
print("\nGenerated Blog Post:\n")
print(blog_post)
