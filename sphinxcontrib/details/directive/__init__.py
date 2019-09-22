# extension testbed


from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.nodes import NodeMatcher


class details(nodes.Element, nodes.General):
    pass


class summary(nodes.TextElement, nodes.General):
    pass


def visit_details(self, node):
    self.body.append('<details>')


def depart_details(self, node):
    self.body.append('</details>')


def visit_summary(self, node):
    self.body.append('<summary>')


def depart_summary(self, node):
    self.body.append('</summary>')


class DetailsDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        admonition = nodes.container('', type='details')
        textnodes, messages = self.state.inline_text(self.arguments[0],
                                                     self.lineno)
        admonition += nodes.paragraph(self.arguments[0], '', *textnodes)
        admonition += messages
        self.state.nested_parse(self.content, self.content_offset, admonition)
        return [admonition]


class DetailsTransform(SphinxPostTransform):
    default_priority = 200
    builders = ('html',)

    def run(self):
        matcher = NodeMatcher(nodes.container, type='details')
        for node in self.document.traverse(matcher):
            newnode = details()
            newnode += summary('', '', *node[0])
            newnode.extend(node[1:])
            node.replace_self(newnode)


def setup(app):
    app.add_node(details, html=(visit_details, depart_details))
    app.add_node(summary, html=(visit_summary, depart_summary))
    app.add_directive('details', DetailsDirective)
    app.add_post_transform(DetailsTransform)

    return {
        'parallel_read_safe': True,
    }