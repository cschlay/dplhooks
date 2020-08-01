from dplhooks.testcases import APITestCase


class CICDTest(APITestCase):
    def test_get_webhooks(self):
        response = self.client.get('/integrations/gitlab/webhooks')
        self.assertEqual(response.status_code, 200)
