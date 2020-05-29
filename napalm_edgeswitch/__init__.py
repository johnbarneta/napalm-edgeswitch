"""napalm_mikrotik package."""

# Import stdlib
import pkg_resources

# Import local modules
from napalm_edgeswitch.edgeswitch import EdgeSwitchDriver

try:
    __version__ = pkg_resources.get_distribution('napalm-edgeswitch').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

__all__ = ('EdgeSwitchDriver', )
