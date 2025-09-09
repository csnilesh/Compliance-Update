import requests
import random

def fetch_data():
    # Simulate fetching data from an API or a database
    topics = ["Technology", "Health", "Travel", "Food", "Lifestyle"]
    return random.choice(topics)

def generate_blog_content(topic):
    # Generate a simple blog post based on the topic
    content = f"## {topic} Blog Post\n\n"
    content += f"This is a blog post about {topic}. Here we discuss various aspects of {topic}.\n\n"
    content += "### Key Points:\n"
    content += "- Point 1\n"
    content += "- Point 2\n"
    content += "- Point 3\n"
    return content

def save_blog_post(content):
    # Save the generated blog post to a file
    with open("generated_blog.md", "w") as file:
        file.write(content)

def main():
    topic = fetch_data()
    blog_content = generate_blog_content(topic)
    save_blog_post(blog_content)
    print("Blog post generated successfully.")

if __name__ == "__main__":
    main()