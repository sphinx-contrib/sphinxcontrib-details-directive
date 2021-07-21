"""
    sphinxcontrib.details.directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017-2019 by Takeshi KOMIYA
    :license: Apache License 2.0, see LICENSE for details.
"""


from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.nodes import NodeMatcher

from sphinxcontrib.details.directive.version import __version__


class details(nodes.Element, nodes.General):
    pass


class summary(nodes.TextElement, nodes.General):
    pass


def visit_details(self, node):
    if node.get('opened'):
        self.body.append(self.starttag(node, 'details', open="open"))
    else:
        self.body.append(self.starttag(node, 'details'))


def depart_details(self, node):
    self.body.append('</details>')


def visit_summary(self, node):
    self.body.append(self.starttag(node, 'summary'))


def depart_summary(self, node):
    self.body.append('</summary>')


def visit_details_latex(self, node):
    if "newenvironment{sphinxdetails}" not in self.elements["preamble"]:
        self.elements["preamble"] += \
            "\n\\newenvironment{sphinxdetails}{}{}\n"

    self.body.append("\n\\begin{sphinxdetails}\n")


def depart_details_latex(self, node):
    self.body.append("\\end{sphinxdetails}\n")


def visit_summary_latex(self, node):
    if "sphinxdetailssummary" not in self.elements["preamble"]:
        self.elements["preamble"] += \
            "\n\\newcommand{\\sphinxdetailssummary}[1]{#1}\n"
    self.body.append("\\sphinxdetailssummary{")


def depart_summary_latex(self, node):
    self.body.append("}\n")



class DetailsDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'class': directives.class_option,
        'name': directives.unchanged,
        'open': directives.flag,
    }

    def run(self):
        admonition = nodes.container('',
                                     classes=self.options.get('classes', []),
                                     opened='open' in self.options,
                                     type='details')
        textnodes, messages = self.state.inline_text(self.arguments[0],
                                                     self.lineno)
        admonition += nodes.paragraph(self.arguments[0], '', *textnodes)
        admonition += messages
        self.state.nested_parse(self.content, self.content_offset, admonition)
        self.add_name(admonition)
        return [admonition]


class DetailsTransform(SphinxPostTransform):
    default_priority = 200
    builders = ('html', 'latex')

    def run(self):
        matcher = NodeMatcher(nodes.container, type='details')
        for node in self.document.traverse(matcher):
            newnode = details(**node.attributes)
            newnode += summary('', '', *node[0])
            newnode.extend(node[1:])
            node.replace_self(newnode)


def setup(app):
    app.add_node(details, html=(visit_details, depart_details),
                 latex=(visit_details_latex, depart_details_latex))
    app.add_node(summary, html=(visit_summary, depart_summary),
                 latex=(visit_summary_latex, depart_summary_latex))
    app.add_directive('details', DetailsDirective)
    app.add_post_transform(DetailsTransform)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
