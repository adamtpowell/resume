from jinja2 import Environment, FileSystemLoader
import content

env = Environment(loader=FileSystemLoader('templates'))

resume = env.get_template("base.html")

print(resume.render(projects=content.projects))