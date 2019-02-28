import click
import requests


@click.command()
def anchor():
   
    Welcome()
    getApiData()

def Welcome():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='yellow'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 32 + 'Welcome to your Favourite news anchor ' + ' ' * 32 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='blue'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' * 100, fg='yellow'))
    click.echo('\n')
    
def getApiData():
    print("Hello!! You are Welcome to your favourite news anchor. Sit back and enjoy News from your favourite news sources.")
    name = input('> What\'s your name?: ')
    print('\nIt\'s nice to meet you {}. Please select a number that represents your news source: \n'.format(name))
    print('-' * 100)
    print("Below is a list of sources you may chose from")
    print("1.ABC News")
    print("2.Al Jazeera English")
    print("3.BBC News")
    print("4.CNBC")
    print('-' * 100)
    news_source =input(str("Enter News Source Number \t"))
    print ('\n')

    if(news_source=='1'):
        print("\t\t\t ABC NEWS HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=45d024f423f94974a94342bc7b1d6fd6")
        news_dictionary = abcnews_request.json()
        articles =news_dictionary['articles']
        
        for article in articles[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
            click.echo(click.style('BY: ' + article['author'], fg='green'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 100)
    elif(news_source=='2'):
        print("\t\t\t Al Jazeera English HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey=45d024f423f94974a94342bc7b1d6fd6")
        news_dictionary = abcnews_request.json()
        articles =news_dictionary['articles']
        
        for article in articles[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
            click.echo(click.style('BY: ' + article['author'], fg='green'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 100)
    elif(news_source=='3'):
        print("\t\t\t BBC News HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=45d024f423f94974a94342bc7b1d6fd6")
        news_dictionary = abcnews_request.json()
        articles =news_dictionary['articles']
        
        for article in articles[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
            click.echo(click.style('BY: ' + article['author'], fg='green'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 100)
    elif(news_source=='4'):
        print("\t\t\t CNBC HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=cnbc&apiKey=45d024f423f94974a94342bc7b1d6fd6")
        news_dictionary = abcnews_request.json()
        articles =news_dictionary['articles']
        
        for article in articles[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
            click.echo(click.style('BY: ' + article['author'], fg='green'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 100)
    else:
        print("Please Select value within the range")
anchor()
