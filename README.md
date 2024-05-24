
# Daily Digest Email

This repository contains a Python script for sending daily news digests via email. The script automates the process of collecting news articles and sending them to subscribers' email addresses on a daily basis, providing a convenient way to stay updated on the latest news without the need for a graphical user interface (UI).

## Features:

- **Automated News Collection**: Collects news articles from various sources or APIs.
- **Customizable Digest**: Allows customization of the news sources, categories, and frequency of email digests.

## Usage:

1. **Configure Email Settings**: Set up the email server and credentials in the script to enable sending emails.
2. **Customize News Sources**: Specify the sources or APIs for fetching news articles according to your preferences.
3. **Run the Script**: Execute the Python script using a scheduler (e.g., cronjob) to send daily email digests.
   ```
   python main.py
   ```

## Dependencies:

This script relies on the following Python libraries:

- `requests`: For making HTTP requests to fetch news articles.
- `smtplib`: For sending emails via SMTP.
- `schedule`: For scheduling tasks to send daily email digests.
- `datetime`: For handling dates and times.

Ensure these dependencies are installed before running the script.

## Contribution:

Contributions are welcome! If you have any ideas for improvement or would like to contribute to the project, feel free to submit a pull request or open an issue on GitHub.
