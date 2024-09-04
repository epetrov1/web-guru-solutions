from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


#https://xhtml2pdf.readthedocs.io/en/latest/usage.html
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    font_config = {
        'font_path': 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap',
        'css': 'body { font-family: "Roboto", sans-serif; }',  # Use Google Font 'Roboto'
    }

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding="UTF-8", **font_config)
    if pdf.err:
        raise Exception("PDF error: %s" % pdf.err)
    return result.getvalue()