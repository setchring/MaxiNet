"""This class is an wrapper for Containernet."""
import sys
try:
    from mininet.node import Docker
    from mininet.topo import Topo
    from MaxiNet.Frontend import maxinet
except ImportError as a:
    print "Containernet is NOT installed or cannot be found. Please install Containernet before using this python file!\n"
    raise
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


class ContainerExperiment(maxinet.Experiment):
    """ A Mininettopo with Docker related methods.
        Inherits Experiment.
        This class is not more than API beautification."""
    def __init__(self, cluster, topology, **params):
        # Call original Experiment init
        maxinet.Experiment.__init__(self, cluster, topology, **params)

    def addDocker(self, name, cls=Docker, wid=None, pos=None, **params):
        """A wrapper for the addHost class to add docker hosts at runtime.

        Args:
            name: Name of the host.
            cls: The docker instanciation
            wid: Optional worker id to place node.
            pos:Optional existing node name whose worker should be used
                as host of node.
            **params: parameters to use at mininet host class
                instanciation.
        """
        return self.addHost(name, cls, wid, pos, **params)


class ContainernetTopo ( Topo ):
    """
        A Mininettopo with Docker related methods.
        Inherits Topo.
        This class is not more than API beautification.
        """

    def __init__(self, *args, **params):
        # call original Mininet.__init__
        Topo.__init__(self, *args, **params)

    def addDocker(self, name, cls=Docker, **opts):
        # TODO: Comment check
        """
        Wrapper for addHost method that adds a
        Docker container as a host.
        """
        if not opts and self.hopts:
            opts = self.hopts

        return self.addHost(name, cls=cls, **opts)
