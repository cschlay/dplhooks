import os
import shutil
from unittest import skip

from dplhooks import settings
from dplhooks.deploys.essentials.deployer import ContainerDeployer
from dplhooks.testcases import APITestCase


class DeployTestCase(APITestCase):
    """
    def tearDown(self) -> None:
        try:
            shutil.rmtree('.testdir')
        except FileNotFoundError:
            pass
    """

    def test_deploy(self):
        deployer = ContainerDeployer(
            workdir=os.path.join(settings.BASE_DIR, '.testdir'),
            confdir=os.path.join(settings.BASE_DIR, "examples/.conf-examples")
        )
        deployer.deploy('dplhooks')

    @skip
    def test_deploy_api(self):
        response = self.client.post('/public/deploy', {
            'token': 'token',
            'project': 'dplhooks'
        })
