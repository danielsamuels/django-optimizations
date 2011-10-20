"""
Optimizations for the django web framework.

Developed by Dave Hall.

<http://www.etianen.com/>
"""

from optimizations.propertycache import cached_property
from optimizations.thumbnailcache import default_thumbnail_cache


get_thumbnail = default_thumbnail_cache.get_thumbnail