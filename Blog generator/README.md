# 📝 Blog Generator

Welcome to the **Blog Generator**! 🚀  
This project helps you automatically generate engaging 200-word blog posts on any topic using AWS Bedrock's Llama 2 model, and saves them directly to your S3 bucket. Perfect for marketers, bloggers, and content creators!

---

## ✨ Features

- ⚡ **Instant Blog Generation** – Create quality blog posts on any topic in seconds!
- 🧠 **Powered by Llama 2** – Uses AWS Bedrock's Llama 2 for smart content creation.
- ☁️ **S3 Storage** – Automatically saves your posts in an S3 bucket for easy access and management.
- 🛠️ **Serverless** – Designed to run seamlessly as an AWS Lambda function.

---

## 📁 Folder Contents

| File              | Description                                      |
|-------------------|--------------------------------------------------|
| `app.py`          | Lambda function code for blog generation & upload |
| `requirements.txt`| Python dependencies for the Lambda function       |

---

## 🚦 How It Works

1. **Trigger Lambda:** Send an event with `blog_event` specifying your topic.
2. **Generate Blog:** AWS Bedrock (Llama 2) creates a 200-word blog post.
3. **Save to S3:** Blog is stored in your specified S3 bucket under `blog-output/`.
4. **Response:** Lambda returns a completion message with status.

---

## 🏁 Quick Start

**Setup:**
1. Ensure your AWS Lambda has permissions for Bedrock and S3 access.
2. Deploy `app.py` as your Lambda handler.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Trigger the Lambda with an event like:
    ```json
    {
      "body": "{\"blog_event\": \"The future of AI in healthcare\"}"
    }
    ```

**Check your blog post** in the S3 bucket (`blog_generate_aws_bedrock`) inside `blog-output/`.

---

## 📝 Example Event

```json
{
  "body": "{\"blog_event\": \"The impact of renewable energy\"}"
}
```

---

## 🛡️ Requirements

- AWS account with access to Bedrock and S3
- Python 3.8+ for Lambda runtime
- Lambda execution role with Bedrock and S3 permissions

---

## 📌 Notes

- 🟢 Make sure to update the S3 bucket name and AWS region as needed in `app.py`.
- 🔒 Secure your AWS credentials and never hard-code them.

---

## 🤝 Contributions

Pull requests and issues are welcome! Feel free to contribute new features or improvements.

---

## ⭐ Happy Blogging!

Let the AI do the writing while you focus on sharing your ideas! ✍️✨
