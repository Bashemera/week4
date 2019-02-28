import click
import requests


@click.command()
def ancho():
   
    Welcome()    

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
cli()
