import os
import shutil
from unittest import skip

from dplhooks import settings
from dplhooks.deploys.essentials.deployer import ContainerDeployer
from dplhooks.testcases import APITestCase


class DeployTestCase(APITestCase):
    @skip
    def test_deploy(self):
        deployer = ContainerDeployer(
            workdir=os.path.join(settings.BASE_DIR, '.testdir'),
            confdir=os.path.join(settings.BASE_DIR, "examples/.conf-examples")
        )
        deployer.deploy('dplhooks', 'token')
