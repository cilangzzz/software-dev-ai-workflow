"""Confluence space management tools.

Tools:
    - confluence_get_spaces: Get all spaces
    - confluence_get_space: Get a single space by key
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from typing import Any, Dict, List, Optional

from _common import (
    AtlassianCredentials,
    get_confluence_client,
    format_json_response,
    format_error_response,
    ConfigurationError,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    APIError,
    NetworkError,
)


def _simplify_space(space_data: Dict[str, Any]) -> Dict[str, Any]:
    """Simplify space data to essential fields."""
    desc = space_data.get('description', {})
    plain_desc = desc.get('plain', {}).get('value', '') if desc else ''

    return {
        'key': space_data.get('key', ''),
        'name': space_data.get('name', ''),
        'type': space_data.get('type', ''),
        'description': plain_desc,
        'id': space_data.get('id', ''),
        'url': space_data.get('_links', {}).get('webui', '')
    }


def confluence_get_spaces(
    limit: int = 50,
    start_at: int = 0,
    space_type: Optional[str] = None,
    expand: Optional[str] = None,
    credentials: Optional[AtlassianCredentials] = None
) -> str:
    """Get all Confluence spaces.

    Args:
        limit: Maximum number of results (default: 50)
        start_at: Index of first result for pagination (default: 0)
        space_type: Filter by type: 'global', 'personal', or None for all
        expand: Fields to expand (e.g., 'description', 'icon', 'homepage')

    Returns:
        JSON string with spaces list or error information
    """
    try:
        client = get_confluence_client(credentials)

        if limit < 0:
            raise ValidationError('limit must be non-negative')
        if start_at < 0:
            raise ValidationError('start_at must be non-negative')

        params: Dict[str, Any] = {
            'limit': limit,
            'start': start_at
        }

        if space_type:
            params['type'] = space_type

        if expand:
            params['expand'] = expand
        else:
            params['expand'] = 'description'

        response = client.get('/rest/api/space', params=params)

        results = response.get('results', [])
        simplified_spaces = [_simplify_space(s) for s in results]

        result = {
            'spaces': simplified_spaces,
            'total': response.get('size', len(results)),
            'start_at': start_at,
            'limit': limit,
            'is_last': start_at + len(results) >= response.get('size', 0)
        }

        return format_json_response(result)

    except ConfigurationError as e:
        return format_error_response('ConfigurationError', str(e))
    except AuthenticationError as e:
        return format_error_response('AuthenticationError', str(e))
    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except (APIError, NetworkError) as e:
        return format_error_response(type(e).__name__, str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Unexpected error: {str(e)}')


def confluence_get_space(
    space_key: str,
    expand: Optional[str] = None,
    credentials: Optional[AtlassianCredentials] = None
) -> str:
    """Get a single Confluence space by key.

    Args:
        space_key: Space key (e.g., 'DEV', 'TEAM')
        expand: Fields to expand (e.g., 'description,icon,homepage')

    Returns:
        JSON string with space data or error information
    """
    try:
        client = get_confluence_client(credentials)

        if not space_key:
            raise ValidationError('space_key is required')

        params: Dict[str, Any] = {}
        if expand:
            params['expand'] = expand
        else:
            params['expand'] = 'description'

        response = client.get(f'/rest/api/space/{space_key}', params=params)

        simplified = _simplify_space(response)

        # Add homepage info if expanded
        if expand and 'homepage' in expand:
            homepage = response.get('homepage', {})
            if homepage:
                simplified['homepage'] = {
                    'id': homepage.get('id', ''),
                    'title': homepage.get('title', '')
                }

        # Add icon info if expanded
        if expand and 'icon' in expand:
            icon = response.get('icon', {})
            if icon:
                simplified['icon'] = icon.get('path', '')

        return format_json_response(simplified)

    except ConfigurationError as e:
        return format_error_response('ConfigurationError', str(e))
    except AuthenticationError as e:
        return format_error_response('AuthenticationError', str(e))
    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except NotFoundError as e:
        return format_error_response('NotFoundError', str(e))
    except (APIError, NetworkError) as e:
        return format_error_response(type(e).__name__, str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Unexpected error: {str(e)}')


def confluence_get_space_content(
    space_key: str,
    content_type: Optional[str] = None,
    limit: int = 25,
    start_at: int = 0,
    depth: Optional[str] = None,
    credentials: Optional[AtlassianCredentials] = None
) -> str:
    """Get content (pages, blog posts) from a space.

    Args:
        space_key: Space key
        content_type: Type of content: 'page', 'blogpost', or None for all
        limit: Maximum number of results (default: 25)
        start_at: Index of first result for pagination (default: 0)
        depth: Content depth: 'root' for top-level only, 'all' for all

    Returns:
        JSON string with content list or error information
    """
    try:
        client = get_confluence_client(credentials)

        if not space_key:
            raise ValidationError('space_key is required')
        if limit < 0:
            raise ValidationError('limit must be non-negative')
        if start_at < 0:
            raise ValidationError('start_at must be non-negative')

        params: Dict[str, Any] = {
            'limit': limit,
            'start': start_at
        }

        if depth:
            params['depth'] = depth

        response = client.get(f'/rest/api/space/{space_key}/content', params=params)

        # Confluence Data Center returns content grouped by type:
        # { "page": { "results": [...] }, "blogpost": { "results": [...] } }
        # Confluence Cloud returns: { "results": [...] }
        all_content: List[Dict[str, Any]] = []

        if content_type:
            # Get specific type
            type_data = response.get(content_type, {})
            results = type_data.get('results', [])
            for c in results:
                all_content.append({
                    'id': c.get('id', ''),
                    'title': c.get('title', ''),
                    'type': c.get('type', content_type),
                    'status': c.get('status', ''),
                    'url': c.get('_links', {}).get('webui', '')
                })
            total = type_data.get('size', len(results))
        else:
            # Get all types - Data Center format
            for ctype in ['page', 'blogpost']:
                type_data = response.get(ctype, {})
                results = type_data.get('results', [])
                for c in results:
                    all_content.append({
                        'id': c.get('id', ''),
                        'title': c.get('title', ''),
                        'type': c.get('type', ctype),
                        'status': c.get('status', ''),
                        'url': c.get('_links', {}).get('webui', '')
                    })

            # Also check for Cloud format (direct results)
            direct_results = response.get('results', [])
            for c in direct_results:
                all_content.append({
                    'id': c.get('id', ''),
                    'title': c.get('title', ''),
                    'type': c.get('type', ''),
                    'status': c.get('status', ''),
                    'url': c.get('_links', {}).get('webui', '')
                })

            total = sum(
                response.get(t, {}).get('size', 0)
                for t in ['page', 'blogpost']
            ) + len(direct_results)

        result = {
            'space_key': space_key,
            'content': all_content,
            'total': total,
            'start_at': start_at,
            'limit': limit,
            'is_last': start_at + len(all_content) >= total
        }

        return format_json_response(result)

    except ConfigurationError as e:
        return format_error_response('ConfigurationError', str(e))
    except AuthenticationError as e:
        return format_error_response('AuthenticationError', str(e))
    except ValidationError as e:
        return format_error_response('ValidationError', str(e))
    except NotFoundError as e:
        return format_error_response('NotFoundError', str(e))
    except (APIError, NetworkError) as e:
        return format_error_response(type(e).__name__, str(e))
    except Exception as e:
        return format_error_response('UnexpectedError', f'Unexpected error: {str(e)}')