from core.exporters import sanitize_text, format_html_preview, format_docx, format_pdf
SAMPLE="""NON-DISCLOSURE AGREEMENT\n\n1. CONFIDENTIALITY\nThe receiving party shall protect confidential information.\n\n2. TERM\nThe obligations continue for two years.\n"""
def test_sanitize(): assert sanitize_text("  hi\x00 ")=="hi"
def test_html(): assert "<h3>" in format_html_preview(SAMPLE)
def test_docx(): assert format_docx(SAMPLE,"NDA")[:2]==b"PK"
def test_pdf(): assert format_pdf(SAMPLE,"NDA").startswith(b"%PDF")
