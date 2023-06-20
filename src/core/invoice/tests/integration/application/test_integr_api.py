from  unittest import TestCase
import responses


class TestAPIIntegr(TestCase):

    def test_generate_the_invoices_by_the_api(self):
        data = responses.Response(
            method= 'POST',
            url = 'http://localhost:8000/generate_invoices',
            json = {
                'month': 1,
                'year': 2022,
                'type': "cash"
            },
            status=200,
            content_type= 'application/json'
        )
        response = responses.add(data)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.body, '{"month": 1, "year": 2022, "type": "cash"}')
