"""Markdown to Confluence Storage Format converter.

This module provides functionality to convert Markdown content to Confluence
Storage Format (XML-based format used by Confluence).

Tools:
    - markdown_to_confluence: Convert Markdown text to Confluence storage format
    - markdown_file_to_confluence: Convert a Markdown file to Confluence storage format
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import re
from typing import Any, Dict, List, Optional, Tuple

from _common import (
    format_json_response,
    format_error_response,
    ValidationError,
)


class MarkdownToConfluenceConverter:
    """Convert Markdown content to Confluence Storage Format.

    Confluence Storage Format is an XML-based format that Confluence uses to store
    page content. This converter transforms standard Markdown syntax to the
    equivalent Confluence storage format elements.

    Supported Markdown elements:
        - Headers (h1-h6)
        - Paragraphs
        - Bold and italic text
        - Inline code and code blocks with language specification
        - Bullet and numbered lists (including nested lists)
        - Links (external and internal)
        - Images with optional parameters
        - Tables with headers
        - Blockquotes
        - Horizontal rules
        - Task lists (- [ ] and - [x])
    """

    # Language mapping for code blocks
    LANGUAGE_MAP = {
        'python': 'python',
        'py': 'python',
        'javascript': 'javascript',
        'js': 'javascript',
        'typescript': 'typescript',
        'ts': 'typescript',
        'java': 'java',
        'cpp': 'cpp',
        'c': 'c',
        'csharp': 'csharp',
        'cs': 'csharp',
        'go': 'go',
        'golang': 'go',
        'rust': 'rust',
        'ruby': 'ruby',
        'php': 'php',
        'sql': 'sql',
        'bash': 'bash',
        'shell': 'bash',
        'sh': 'bash',
        'json': 'json',
        'yaml': 'yaml',
        'yml': 'yaml',
        'xml': 'xml',
        'html': 'html',
        'css': 'css',
        'markdown': 'markdown',
        'md': 'markdown',
        'text': 'none',
        '': 'none',
    }

    def __init__(self):
        """Initialize the converter."""
        self.list_stack: List[Tuple[str, int]] = []  # [(type, level), ...]
        self.in_table: bool = False  # Track if we're inside a table
        self.table_has_header: bool = False  # Track if table has header row

    def convert(self, markdown: str) -> str:
        """Convert Markdown content to Confluence Storage Format.

        Args:
            markdown: Markdown text to convert

        Returns:
            Confluence Storage Format string
        """
        if not markdown:
            return ''

        # Normalize line endings
        markdown = markdown.replace('\r\n', '\n').replace('\r', '\n')

        # Process the markdown line by line
        lines = markdown.split('\n')
        result_lines = []

        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            # Check for code blocks first (they need special handling)
            if stripped.startswith('```'):
                code_block, consumed = self._process_code_block(lines, i)
                result_lines.append(code_block)
                i += consumed
                continue

            # Check for table start (process entire table at once)
            if stripped.startswith('|'):
                table_content, consumed = self._process_table(lines, i)
                result_lines.append(table_content)
                i += consumed
                continue

            # Process other elements
            processed = self._process_line(line)
            result_lines.append(processed)
            i += 1

        # Close any remaining open lists
        while self.list_stack:
            list_type, _ = self.list_stack.pop()
            result_lines.append(f'</{list_type}>')

        # Join and clean up
        result = '\n'.join(result_lines)

        # Post-process: wrap orphan text in paragraphs
        result = self._wrap_text_in_paragraphs(result)

        return result

    def _process_line(self, line: str) -> str:
        """Process a single line of Markdown.

        Args:
            line: Current line to process

        Returns:
            Converted line in Confluence format
        """
        stripped = line.strip()

        # Empty line - close all lists
        if not stripped:
            return self._close_all_lists()

        # Headers
        header_match = re.match(r'^#{1,6}\s+(.+)$', stripped)
        if header_match:
            self._close_all_lists()
            level = len(stripped) - len(stripped.lstrip('#'))
            content = self._process_inline(header_match.group(1))
            return f'<h{level}>{content}</h{level}>'

        # Horizontal rule
        if re.match(r'^[-*_]{3,}$', stripped):
            self._close_all_lists()
            return '<hr />'

        # Task list items
        task_match = re.match(r'^[-*+]\s+\[([ xX])\]\s+(.+)$', stripped)
        if task_match:
            checked = task_match.group(1).lower() == 'x'
            content = self._process_inline(task_match.group(2))
            return self._process_task_list_item(content, checked)

        # Bullet list items
        bullet_match = re.match(r'^[-*+]\s+(.+)$', stripped)
        if bullet_match:
            content = self._process_inline(bullet_match.group(1))
            return self._process_list_item('ul', content, stripped)

        # Numbered list items
        numbered_match = re.match(r'^(\d+)[.)]\s+(.+)$', stripped)
        if numbered_match:
            content = self._process_inline(numbered_match.group(2))
            return self._process_list_item('ol', content, stripped)

        # Blockquote
        if stripped.startswith('>'):
            self._close_all_lists()
            quote_content = stripped[1:].strip()
            processed_content = self._process_inline(quote_content)
            return f'<blockquote><p>{processed_content}</p></blockquote>'

        # Regular paragraph content
        self._close_all_lists()
        return self._process_inline(stripped)

    def _process_code_block(self, lines: List[str], start_index: int) -> Tuple[str, int]:
        """Process a code block.

        Args:
            lines: All lines in the document
            start_index: Starting index of the code block

        Returns:
            Tuple of (converted code block, number of lines consumed)
        """
        start_line = lines[start_index].strip()

        # Extract language from the opening line
        language = ''
        if len(start_line) > 3:
            lang_spec = start_line[3:].strip().lower()
            language = self.LANGUAGE_MAP.get(lang_spec, lang_spec)

        # Find the closing ```
        code_lines = []
        i = start_index + 1

        while i < len(lines):
            if lines[i].strip() == '```':
                break
            code_lines.append(lines[i])
            i += 1

        # Calculate lines consumed (opening, content, closing)
        consumed = i - start_index + 1

        # Escape the code content
        code_content = '\n'.join(code_lines)
        code_content = self._escape_xml(code_content)

        # Build Confluence code macro
        if language and language != 'none':
            result = f'''<ac:structured-macro ac:name="code">
<ac:parameter ac:name="language">{language}</ac:parameter>
<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body>
</ac:structured-macro>'''
        else:
            result = f'''<ac:structured-macro ac:name="code">
<ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body>
</ac:structured-macro>'''

        return result, consumed

    def _process_inline(self, text: str) -> str:
        """Process inline Markdown elements.

        Args:
            text: Text with inline Markdown elements

        Returns:
            Text with inline elements converted to Confluence format
        """
        if not text:
            return ''

        # Process inline code first (to prevent other processing inside code)
        text = self._process_inline_code(text)

        # Process images
        text = self._process_images(text)

        # Process links
        text = self._process_links(text)

        # Process bold and italic
        text = self._process_bold_italic(text)

        # Process strikethrough
        text = self._process_strikethrough(text)

        # Escape remaining XML characters that aren't part of generated tags
        text = self._escape_remaining_xml(text)

        return text

    def _process_inline_code(self, text: str) -> str:
        """Process inline code (backtick enclosed).

        Args:
            text: Text potentially containing inline code

        Returns:
            Text with inline code converted to Confluence format
        """
        pattern = r'`([^`]+)`'

        def replace_code(match):
            content = self._escape_xml(match.group(1))
            return f'<code>{content}</code>'

        return re.sub(pattern, replace_code, text)

    def _process_images(self, text: str) -> str:
        """Process image syntax.

        Args:
            text: Text potentially containing image syntax

        Returns:
            Text with images converted to Confluence format
        """
        # Match ![alt](url) or ![alt|width,height](url)
        pattern = r'!\[([^\]|]*)(?:\|([^\]]*))?\]\(([^)]+)\)'

        def replace_image(match):
            alt = match.group(1) or ''
            params = match.group(2) or ''
            url = match.group(3)

            # Parse width/height parameters
            width = ''
            height = ''
            if params:
                param_parts = params.split(',')
                if param_parts:
                    width = param_parts[0].strip()
                    if len(param_parts) > 1:
                        height = param_parts[1].strip()

            # Build Confluence image tag
            attrs = f' ac:alt="{self._escape_xml(alt)}"'
            if width:
                attrs += f' ac:width="{width}"'
            if height:
                attrs += f' ac:height="{height}"'

            return f'<ac:image{attrs}><ri:url ri:value="{self._escape_xml(url)}" /></ac:image>'

        return re.sub(pattern, replace_image, text)

    def _process_links(self, text: str) -> str:
        """Process link syntax.

        Args:
            text: Text potentially containing links

        Returns:
            Text with links converted to Confluence format
        """
        # Match [text](url)
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'

        def replace_link(match):
            link_text = match.group(1)
            url = match.group(2)

            # Check if it's a Confluence internal link pattern
            # Patterns like "spaceKey:Page Title" or "#anchor"
            if ':' in url and not url.startswith('http'):
                parts = url.split(':', 1)
                space_key = parts[0]
                page_title = parts[1] if len(parts) > 1 else ''

                return f'''<ac:link>
<ri:page ri:space-key="{space_key}" ri:content-title="{self._escape_xml(page_title)}" />
<ac:plain-text-link-body><![CDATA[{self._escape_xml(link_text)}]]></ac:plain-text-link-body>
</ac:link>'''

            # External link - process nested formatting in link text
            # Note: _escape_remaining_xml will be called by _process_inline at the end
            processed_text = self._process_inline(link_text)
            return f'<a href="{self._escape_xml(url)}">{processed_text}</a>'

        return re.sub(pattern, replace_link, text)

    def _process_bold_italic(self, text: str) -> str:
        """Process bold and italic text.

        Args:
            text: Text potentially containing bold/italic markers

        Returns:
            Text with bold/italic converted to Confluence format
        """
        # Bold with ** or __
        def replace_bold(match):
            content = self._escape_xml(match.group(1))
            return f'<strong>{content}</strong>'
        text = re.sub(r'\*\*([^*]+)\*\*', replace_bold, text)
        text = re.sub(r'__([^_]+)__', replace_bold, text)

        # Italic with * or _
        def replace_italic(match):
            content = self._escape_xml(match.group(1))
            return f'<em>{content}</em>'
        text = re.sub(r'\*([^*]+)\*', replace_italic, text)
        text = re.sub(r'_([^_]+)_', replace_italic, text)

        return text

    def _process_strikethrough(self, text: str) -> str:
        """Process strikethrough text.

        Args:
            text: Text potentially containing strikethrough markers

        Returns:
            Text with strikethrough converted to Confluence format
        """
        # Strikethrough with ~~
        def replace_strikethrough(match):
            content = self._escape_xml(match.group(1))
            return f'<s>{content}</s>'
        text = re.sub(r'~~([^~]+)~~', replace_strikethrough, text)
        return text

    def _process_list_item(self, list_type: str, content: str, line: str) -> str:
        """Process a list item and manage list nesting.

        Args:
            list_type: 'ul' or 'ol'
            content: Processed content of the list item
            line: Original line text

        Returns:
            List item with proper list opening/closing tags
        """
        # Determine indentation level
        indent = len(line) - len(line.lstrip())
        level = indent // 2  # Assuming 2-space indentation

        result = []

        # Handle list nesting changes
        while self.list_stack and self.list_stack[-1][1] > level:
            closed_type, _ = self.list_stack.pop()
            result.append(f'</{closed_type}>')

        if not self.list_stack or self.list_stack[-1][1] < level:
            self.list_stack.append((list_type, level))
            result.append(f'<{list_type}>')
        elif self.list_stack[-1][0] != list_type:
            # Close previous list type and open new one
            closed_type, _ = self.list_stack.pop()
            result.append(f'</{closed_type}>')
            self.list_stack.append((list_type, level))
            result.append(f'<{list_type}>')

        result.append(f'<li>{content}</li>')
        return '\n'.join(result)

    def _process_task_list_item(self, content: str, checked: bool) -> str:
        """Process a task list item.

        Args:
            content: Processed content of the task item
            checked: Whether the task is checked

        Returns:
            Task list item in Confluence format
        """
        # Handle task list as a special list type
        if not self.list_stack or self.list_stack[-1][0] != 'ul':
            if self.list_stack:
                closed_type, _ = self.list_stack.pop()
                self._pending_close = f'</{closed_type}>'
            self.list_stack.append(('ul', 0))

        checked_attr = 'true' if checked else 'false'
        return f'<li><ac:task><ac:task-status>{checked_attr}</ac:task-status><ac:task-body>{content}</ac:task-body></ac:task></li>'

    def _close_all_lists(self) -> str:
        """Close all open lists.

        Returns:
            String with closing tags for all open lists
        """
        result = []
        while self.list_stack:
            list_type, _ = self.list_stack.pop()
            result.append(f'</{list_type}>')
        return '\n'.join(result) if result else ''

    def _process_table_row(self, row: str, is_header: bool = False) -> str:
        """Process a table row.

        Args:
            row: Table row line starting with |
            is_header: Whether this is a header row

        Returns:
            Table row in Confluence format
        """

        # Split cells
        cells = [c.strip() for c in row.strip('|').split('|')]

        row_content = []
        for cell in cells:
            processed_cell = self._process_inline(cell)
            tag = 'th' if is_header else 'td'
            row_content.append(f'<{tag}>{processed_cell}</{tag}>')

        return f'<tr>{"".join(row_content)}</tr>'

    def _process_table(self, lines: List[str], start_index: int) -> Tuple[str, int]:
        """Process a complete table.

        Args:
            lines: All lines in the document
            start_index: Starting index of the table

        Returns:
            Tuple of (complete table in Confluence format, number of lines consumed)
        """
        result = ['<table>']

        # Collect all table rows
        table_rows = []
        i = start_index
        while i < len(lines):
            current_line = lines[i].strip()
            if not current_line.startswith('|'):
                break
            table_rows.append(current_line)
            i += 1

        # Calculate lines consumed
        consumed = len(table_rows)

        # Process rows
        for row_idx, row in enumerate(table_rows):
            # Check if this is a separator row
            if re.match(r'^\|[\s\-:]+\|[\s\-:]+\|', row):
                # Mark the last added row to be converted to header
                if result and result[-1].startswith('<tr>'):
                    result[-1] = result[-1].replace('<td>', '<th>').replace('</td>', '</th>')
                continue

            # Check if next row is a separator (then this is header)
            is_header = (row_idx + 1 < len(table_rows) and
                        re.match(r'^\|[\s\-:]+\|[\s\-:]+\|', table_rows[row_idx + 1]))

            row_content = self._process_table_row(row, is_header=is_header)
            if row_content:
                result.append(row_content)

        result.append('</table>')
        return '\n'.join(result), consumed

    def _wrap_text_in_paragraphs(self, text: str) -> str:
        """Wrap orphan text lines in paragraph tags.

        Args:
            text: Converted text

        Returns:
            Text with orphan lines wrapped in <p> tags
        """
        lines = text.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()

            # Skip empty lines
            if not stripped:
                result.append('')
                continue

            # Skip lines that are already wrapped in tags or are closing tags
            if re.match(r'^<[a-z0-9:]+[^>]*>', stripped) or stripped.startswith('</'):
                result.append(line)
                continue

            # Wrap in paragraph
            result.append(f'<p>{stripped}</p>')

        return '\n'.join(result)

    def _escape_xml(self, text: str) -> str:
        """Escape XML special characters, avoiding double-escaping.

        Args:
            text: Text to escape

        Returns:
            Escaped text
        """
        if not text:
            return ''

        # First, protect existing entities by replacing them temporarily
        # This avoids double-escaping (e.g., &amp; -> &amp;amp;)
        entity_pattern = r'&(amp|lt|gt|quot|apos|#\d+|#x[0a-fA-F]+);'

        def protect_entity(match):
            return f'\x00ENT{match.group(1)}\x00'

        text = re.sub(entity_pattern, protect_entity, text)

        # Now escape all remaining special characters
        replacements = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;',
        }

        for char, entity in replacements.items():
            text = text.replace(char, entity)

        # Restore protected entities
        def restore_entity(match):
            return f'&{match.group(1)};'

        text = re.sub(r'\x00ENT([^\x00]+)\x00', restore_entity, text)

        return text

    def _escape_remaining_xml(self, text: str) -> str:
        """Escape XML characters that aren't part of generated tags.

        This method escapes <, >, and & that appear in plain text but are NOT
        part of the XML tags we've already generated during conversion.

        Args:
            text: Text with some XML tags already present

        Returns:
            Text with remaining special characters escaped
        """
        if not text:
            return ''

        # Tags we generate - don't escape inside these
        # Pattern matches: opening tags, closing tags, self-closing tags, CDATA
        tag_pattern = r'<(/?(?:code|strong|em|s|a|ac:[a-z-]+|ri:[a-z-]+)[^>]*>|!\[CDATA\[.*?\]\]>|hr />)'

        result = []
        last_end = 0

        # Find all tag positions
        for match in re.finditer(tag_pattern, text):
            # Escape the text before this tag
            if match.start() > last_end:
                plain_text = text[last_end:match.start()]
                plain_text = self._escape_xml(plain_text)
                result.append(plain_text)

            # Keep the tag unchanged
            result.append(match.group(0))
            last_end = match.end()

        # Escape any remaining text after the last tag
        if last_end < len(text):
            plain_text = text[last_end:]
            plain_text = self._escape_xml(plain_text)
            result.append(plain_text)

        return ''.join(result)


def markdown_to_confluence(
    markdown: str,
    wrap_in_paragraphs: bool = True
) -> str:
    """Convert Markdown text to Confluence Storage Format.

    This function converts standard Markdown syntax to Confluence's Storage Format,
    which is an XML-based format used by Confluence to store page content.

    Args:
        markdown: Markdown text to convert
        wrap_in_paragraphs: Whether to wrap orphan text in <p> tags (default: True)

    Returns:
        JSON string with converted content or error information

    Example:
        >>> result = markdown_to_confluence("# Hello\\nThis is **bold** text.")
        >>> print(result)
        {"success": true, "content": "<h1>Hello</h1><p>This is <strong>bold</strong> text.</p>"}

    Supported Markdown elements:
        - Headers: # through ######
        - Bold: **text** or __text__
        - Italic: *text* or _text_
        - Strikethrough: ~~text~~
        - Inline code: `code`
        - Code blocks: ```language ... ```
        - Bullet lists: - item, * item, + item
        - Numbered lists: 1. item, 2) item
        - Task lists: - [ ] task, - [x] completed
        - Links: [text](url)
        - Internal links: [text](spaceKey:Page Title)
        - Images: ![alt](url) or ![alt|width,height](url)
        - Tables: | col1 | col2 |
        - Blockquotes: > quote text
        - Horizontal rules: ---, ***, ___
    """
    try:
        if not markdown:
            raise ValidationError('markdown content is required')

        converter = MarkdownToConfluenceConverter()
        content = converter.convert(markdown)

        return format_json_response({
            'success': True,
            'content': content,
            'original_length': len(markdown),
            'converted_length': len(content)
        })

    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Conversion error: {str(e)}')


def markdown_file_to_confluence(
    file_path: str,
    wrap_in_paragraphs: bool = True
) -> str:
    """Convert a Markdown file to Confluence Storage Format.

    This function reads a Markdown file from the specified path and converts
    its content to Confluence's Storage Format.

    Args:
        file_path: Path to the Markdown file (absolute or relative)
        wrap_in_paragraphs: Whether to wrap orphan text in <p> tags (default: True)

    Returns:
        JSON string with converted content or error information

    Example:
        >>> result = markdown_file_to_confluence("/path/to/document.md")
        >>> print(result)
        {
            "success": true,
            "content": "<h1>Title</h1><p>Content...</p>",
            "file_path": "/path/to/document.md",
            "file_size": 1024
        }
    """
    try:
        if not file_path:
            raise ValidationError('file_path is required')

        # Resolve file path
        path = Path(file_path)

        if not path.exists():
            raise ValidationError(f'File not found: {file_path}')

        if not path.is_file():
            raise ValidationError(f'Path is not a file: {file_path}')

        # Read file content
        markdown = path.read_text(encoding='utf-8')

        # Convert
        converter = MarkdownToConfluenceConverter()
        content = converter.convert(markdown)

        return format_json_response({
            'success': True,
            'content': content,
            'file_path': str(path.absolute()),
            'file_size': path.stat().st_size,
            'original_length': len(markdown),
            'converted_length': len(content)
        })

    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except FileNotFoundError as e:
        return format_error_response('NotFoundError', str(e))
    except PermissionError as e:
        return format_error_response('PermissionError', f'Permission denied: {str(e)}')
    except UnicodeDecodeError as e:
        return format_error_response('UnicodeError', f'Failed to decode file (encoding issue): {str(e)}')
    except Exception as e:
        return format_error_response('UnexpectedError', f'Conversion error: {str(e)}')


def create_confluence_page_from_markdown(
    space_key: str,
    title: str,
    markdown: str,
    parent_id: Optional[str] = None
) -> str:
    """Convert Markdown and create a Confluence page with the converted content.

    This is a convenience function that combines markdown_to_confluence and
    confluence_create_page into a single operation.

    Args:
        space_key: Space key where the page will be created
        title: Page title
        markdown: Markdown content to convert and use as page content
        parent_id: Parent page ID (optional)

    Returns:
        JSON string with created page data or error information

    Example:
        >>> result = create_confluence_page_from_markdown(
        ...     space_key="DEV",
        ...     title="API Documentation",
        ...     markdown="# Overview\\nThis is the API documentation.",
        ...     parent_id="12345"
        ... )
    """
    try:
        # Import here to avoid circular dependency
        from confluence_pages import confluence_create_page

        if not space_key:
            raise ValidationError('space_key is required')
        if not title:
            raise ValidationError('title is required')
        if not markdown:
            raise ValidationError('markdown content is required')

        # Convert markdown to Confluence format
        converter = MarkdownToConfluenceConverter()
        content = converter.convert(markdown)

        # Create the page
        return confluence_create_page(
            space_key=space_key,
            title=title,
            content=content,
            parent_id=parent_id
        )

    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Failed to create page: {str(e)}')


def update_confluence_page_from_markdown(
    page_id: str,
    title: str,
    markdown: str
) -> str:
    """Convert Markdown and update a Confluence page with the converted content.

    This is a convenience function that combines markdown_to_confluence and
    confluence_update_page into a single operation.

    Args:
        page_id: Page ID to update
        title: New page title
        markdown: Markdown content to convert and use as page content

    Returns:
        JSON string with updated page data or error information

    Example:
        >>> result = update_confluence_page_from_markdown(
        ...     page_id="67890",
        ...     title="Updated API Documentation",
        ...     markdown="# Updated Overview\\nNew content here."
        ... )
    """
    try:
        # Import here to avoid circular dependency
        from confluence_pages import confluence_update_page

        if not page_id:
            raise ValidationError('page_id is required')
        if not title:
            raise ValidationError('title is required')
        if not markdown:
            raise ValidationError('markdown content is required')

        # Convert markdown to Confluence format
        converter = MarkdownToConfluenceConverter()
        content = converter.convert(markdown)

        # Update the page
        return confluence_update_page(
            page_id=page_id,
            title=title,
            content=content
        )

    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Failed to update page: {str(e)}')