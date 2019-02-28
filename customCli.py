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
    news_request = requests.get(
        "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=45d024f423f94974a94342bc7b1d6fd6")
    news_dictionary = news_request.json()
    articles =news_dictionary['articles']
    
    for article in articles[:4] :
        click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
        click.echo(click.style('BY: ' + article['author'], fg='green'))
        click.echo('\n')
        click.echo(click.wrap_text(article['description'], 100))
        click.echo('\n')
        click.echo('-' * 100)
anchor()
