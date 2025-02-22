import requests # allow us to send HTPP requests/to fetch news from an API
from deep_translator import GoogleTranslator #  let us translate the text this case the news headlines and descriptions
import webbrowser #  built_in Python library that let us open URls in a web brower
from datetime import datetime #  to get the today's date

NEWS_API_KEY = '9971a6a48b9540289d13004d9c0120a3'  # Mine API key that I need to acess the news data from the provider of the API. 
#  Is a password that let me get data.

# Function to fetch last BBC news from the current day
def get_last_news():
    today_date = datetime.today().strftime('%Y-%m-%d')  # Get today's date in the format 'YYYY-MM-DD'
    
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={NEWS_API_KEY}&from={today_date}&pageSize=1'
    response = requests.get(url)  #  requesting to the API to get the news
    
    if response.status_code == 200: #  if everything goes well/if the status code is 200 means success then the code will run the next line of code
        data = response.json()
        return data['articles']
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return [] #  It return the articles

# Function to translate text
def translate_text(text, target_language):
    try: # try something that might cause error/lets try
        translation = GoogleTranslator(source='auto', target=target_language).translate(text) # Will automatically detect the language
        return translation
    except Exception as a: # If an error happens store the error message in a variable call a , and print...
        print(f"Error while translating: {a}")
        return text  # return original text even if happen an error/translation failed

# Function to display translated BBC news and ask if the user wants to open the article
def display_translated_bbc_news(articles, target_language):
    for article in articles:   # loop, will go through each article
        title = article['title']
        description = article['description']
        content = article['content']
        article_url = article.get('url', None)  # Use .get() to avoid errors if 'url' is missing, if any url will store None

        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Content: {content}\n")
        
        # Translate the article title, description, and content
        translated_title = translate_text(title, target_language)
        translated_description = translate_text(description, target_language)
        translated_content = translate_text(content, target_language)

         # Print the translated news
        print(f"--- Translated News ---")
        print(f"Translated Title: {translated_title}")
        print(f"Translated Description: {translated_description}")
        print(f"Translated Content: {translated_content}\n")
        print("============================================\n")  # Separator line
        
        # Ask the user if they want to open the article URL in the browser
        if article_url:  # Check if article_url exists
            open_url = input(f"Do you want to open this article in the browser? (y/n): ").strip().lower()
            
            if open_url == 'y':
                print(f"Opening the article in browser...")
                webbrowser.open(article_url)  # Open the URL in the default web browser
            else:
                print("Okay, not opening the URL.")
        else:
            print("No URL available for this article.")

# Main function to drive the translation project
def main():
    print("Fetching today's BBC news...") # title
    articles = get_last_news()  # Call the get_last_news() function to get articles and stores in a variable call articles
    
    if articles: # check if artciles has any news
        print("\n--- Today's BBC News ---\n")
        target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ") # user to enter which language code he/she wants to translate to
        display_translated_bbc_news(articles, target_language) #  will display the news, translating it and asking user if he want to open the article
    else: # if no articles
        print("No news available at the moment.")

# Run the main function. Is called only if the script is being run directly (not imported as a module in another script
if __name__ == '__main__':
    main()
