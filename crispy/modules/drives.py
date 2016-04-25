import logging
import os

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate the HDD's on a remote machine. """
    
    def init_argparse(self):
	self.parser = CrispyArgumentParser(prog="drives", description=self.__doc__)
	#self.parser.add_argument()

    def run(self, args):
	logger.debug("in module.py run()")
	info = "[*] Disk Partitions:\n"

        partitions = os.listdir('/Volumes')
        for disk in partitions:
            info += "\t%s" %disk

	logger.debug(info)
        return info + "\n"
