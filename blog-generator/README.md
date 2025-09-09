# Blog Generator

This project is designed to automate the generation of blog content using a Python script. It leverages GitHub Actions to schedule and run the blog generation process daily.

## Project Structure

```
blog-generator
├── src
│   └── ai_blog_writer.py      # Main logic for generating blog content
├── .github
│   └── workflows
│       └── generate-blog.yml   # GitHub Actions workflow for blog generation
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd blog-generator
   ```

2. **Install dependencies:**
   Make sure you have Python 3.9 installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- The blog generation process is automated using GitHub Actions. It runs daily at 6 AM IST.
- You can also manually trigger the workflow from the GitHub Actions tab in your repository.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.