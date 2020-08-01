from django.test import TestCase

from dplhooks.deploys.essentials.conf_parser import ConfigurationParser


class ConfigurationParserTest(TestCase):

    def test_init(self):
        parser = ConfigurationParser('examples/.conf-examples')
        self.assertEqual(parser.projects['version'], '1')
        self.assertEqual(parser.projects['workdir'], '~/projects')
        self.assertEqual(parser.projects['projects']['dplhooks']['repository'], 'https://github.com/cschlay/dplhooks.git')
