from os import path

from sphinx.addnodes import document, nodes


def setup(app):
    app.add_html_theme("takao", path.abspath(path.dirname(__file__)))
    app.connect("html-page-context", setup_context)


def setup_context(app, pagename, templatename, context, doctree: document):
    context["page_nav_items"] = get_page_nav_items(doctree)


def get_page_nav_items(doctree: document):
    if not doctree:
        return []

    root_sections = get_children(doctree, "section")

    nav_root = root_sections[0] if len(root_sections) == 1 else doctree

    return get_sections(nav_root, recurse=True)


def get_sections(node: nodes.Element, recurse=False):
    sections = get_children(node, "section")

    return [
        {
            "href": f'#{section["ids"][0]}',
            "title": get_title(section),
            **({"children": get_sections(section)} if recurse else {}),
        }
        for section in sections
    ]


def get_title(node: nodes.Element):
    titles = get_children(node, "title")

    if not titles:
        return node["ids"][0]

    return titles[0].astext()


def get_children(node: nodes.Element, tagname: str):
    return [child for child in node.children if child.tagname == tagname]
