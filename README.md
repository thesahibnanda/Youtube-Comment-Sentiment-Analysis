# <b> YouTube Comment Scraping And Its Sentiment Analysis  With Severity And Score </b>

Introducing YouTube Sentiment Analysis Tool, a sophisticated program that can scrape certain sampled comments from given YouTube video and perform sentiment analysis using advanced natural language processing (NLP) techniques. With this tool, you can quickly analyze both individual comments and the overall sentiment of the video.

<br>

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Working of Each Aspect of the Tool](#working-of-each-aspect-of-the-tool)
- [Closing Remarks](#closing-remarks)

<br>

## Installation

Provide instructions on how to install this project, including any dependencies that need to be installed first. For example:

    1. Clone the repository: `git clone https://github.com/thesahibnanda/Youtube-Comment-Sentiment-Analysis.git`
    2. Install dependencies: `pip install -r requirements.txt`

<br>

## Usage

Step 1: 

To use this tool just, execute the 'FinalScript.py' using following Terminal Commands:

Windows: 
```powershell
# First Go To The Directory Where Tool Is Saved
PS C:\Users\UserName> py FinalScript.py
```

Mac:
```bash
# First Go To The Directory Where Tool Is Saved
python FinalScript.py
```

Linux: 
```bash
# First Go To The Directory Where Tool Is Saved
$ pyhton FinalScript.py
```

Step 2:

Enter YouTube video link as a command line input.

<br>


## Working of Each Aspect of the Tool 

1. <u>YouTubeCommentScraper.py</u>
    
    - This Python3 script scrapes comments from the provided YouTube URL.
    - One can change the amount of comments scraped by changing the ending value of 'for' loop mentioned in the script.
    ```python
    for i in range(0,10): #Ending Value Can Be Changed
        response = youtube.video_comments()
        data = response['body']
        all_data.extend(data)
    ```

2. <u> PreprocessingData.py </u>

    - This Python script preprocesses data (or cleans data) so that Sentiment Analysis can give better results.

3. <u> SentimentAndSeverityAnalysis.py </u>

    - This Python script find Sentiment, Score and Severity of a particular given text.

<br>

## Closing Remarks

- Connect with me on <b> LinkedIn</b>: https://www.linkedin.com/in/sahib-nanda-44b2bb264

- Check out my <b> Geeks For Geeks </b> Profile: https://auth.geeksforgeeks.org/user/sahibnanda/

- Check out of my <b> LeetCode </b> Profile: https://leetcode.com/imsahibnanda/













