from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

resume = env.get_template("resume.html")

print(resume.render())