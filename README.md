# Description

Create H3C Comware7 switches configuration by Ansible+Jinja2+YAML.

## Custom filters

### bracket2list

> Referenced module: [bracket_expansion](https://pypi.org/project/bracket-expansion/).

USE:

If you have a jinja2 template like `{{ G0/0/[0-4] | bracket2list }}`  
It will be a iterable list: `[G0/0/0,G0/0/1,G0/0/2,G1/0/3,G1/0/4]`  
Then you can use `for` statement to configure these interfaces.

### tolist

USE:

This filter can separate a string by comma.

## Todo

- [ ] 123
- [ ] 456
