from docutils import nodes
from docutils.parsers.rst import Directive, directives

static_path = '../../_static'

class Blockly(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False

    option_spec = {'height': directives.unchanged}

    def run(self):
        index_url = f'{static_path}/blockly/index.html'

        block_file_name = self.arguments[0]
        if not block_file_name.lower().endswith('.blk'):
            block_file_name += '.blk'
        blocks_url = f'{static_path}/blk_files/{block_file_name}'

        height = self.options['height']

        html = f'<iframe src="{index_url}" style="border: 0px;" width="100%" height="{height}" blocks-url="{blocks_url}"></iframe>'

        html_node = nodes.raw('', html, format='html')
        return [html_node]


def setup(app):
    app.add_directive("blockly", Blockly)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
