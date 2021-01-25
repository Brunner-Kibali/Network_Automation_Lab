# Import Jinja2 library
from jinja2 import Environment, FileSystemLoader

# bracket_expansion is also a third party library.
# Install through pip before running this.

from bracket_expansion import bracket_expansion

# Declare template environment
ENV = Environment(loader=FileSystemLoader('.'))

# Filters are added to the ENV object after declaration. "bracket_expansion"
# is a function that we're passing in--the template engine will actually
# execute this function when rendering the template.

ENV.filters['bracket_expansion'] = bracket_expansion
template = ENV.get_template("template.j2")

# The bracket_expansion function we've passed in as a filter requires a
# text pattern to work against. We'll pass this in as "iface_pattern"

print(template.render(iface_pattern='GigabitEthernet0/0/[0-3]'))
