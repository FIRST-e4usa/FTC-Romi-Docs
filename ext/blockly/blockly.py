from docutils import nodes
from docutils.parsers.rst import Directive, directives


class Blockly(Directive):

    has_content = True
    required_arguments = 2
    optional_arguments = 0
    final_argument_whitespace = False

    option_spec = {'height': directives.unchanged}

    def run(self):
        blocks = '../../_static/snippets/' + self.arguments[0] + '.blk'
        html = '<iframe src="../../_static/blockly/index.html" style="border: 0px;" width="100%" height="' + self.options["height"] + '" blocks="' + blocks + '"></iframe>'

        html_node = nodes.raw('', html, format='html')
        return [html_node]


def setup(app):
    app.add_directive("blockly", Blockly)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
