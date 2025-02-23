# Last-news-BBC

This Python script fetches the latest news from BBC and allows users to translate the news articles into a specified language. It then gives users the option to open the article in their web browser. The script utilizes the NewsAPI to get the news, the Google Translator API for translations, and the built-in webbrowser library to open article URLs.

**Key Features**
* Fetch Latest BBC News: Retrieves top news headlines from BBC for the current day.
* Translation: Translates article titles, descriptions, and content into the user-specified language (e.g., Spanish, French).
* Open in Browser: Allows the user to open the news articles in their default web browser.

**Technologies & Libraries Used**
* requests: To send HTTP requests and fetch news data from the NewsAPI.
* deep_translator: To translate news articles using the Google Translator.
* webbrowser: A built-in Python library to open URLs in the browser.
* datetime: To fetch the current date for filtering today's news.

**How It Works**
* Fetch News: The script uses the NewsAPI to fetch the latest BBC news articles based on today's date.
* Translate News: The script uses GoogleTranslator from the deep_translator library to translate the news article title, description, and content into the user's target language.
* User Interaction: After displaying the translated news, the user is prompted to decide if they want to open the full article in their web browser.

**Usage**
* Set Up: Install the required libraries:
pip install requests deep_translator

* API Key: Replace the placeholder API key (NEWS_API_KEY) in the script with your own NewsAPI key.
  
* Run the Script: Execute the script, which will fetch today’s news, translate it, and ask if you'd like to open the article in a browser.

**Future Improvements**
* Translate Article URL: Currently, the script translates the article's title, description, and content. In the future, I plan to extend this feature to also translate the URL of the article itself, based on the user’s desired language. This will provide a fully localized experience for users accessing articles through the browser.
