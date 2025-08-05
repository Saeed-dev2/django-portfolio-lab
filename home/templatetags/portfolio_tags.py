from django import template

register = template.Library()

@register.filter
def get_status_color(status):
    """Return Bootstrap color class for project status"""
    status_colors = {
        'completed': 'success',
        'in_progress': 'warning',
        'planned': 'info',
    }
    return status_colors.get(status, 'secondary')

@register.filter
def truncate_chars(value, length):
    """Truncate string to specified length"""
    if len(value) <= length:
        return value
    return value[:length] + '...'