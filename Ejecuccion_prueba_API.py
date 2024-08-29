import unittest
from app import app

class LocationAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_locations(self):
        response = self.app.get('/locations')
        self.assertEqual(response.status_code, 200)

    def test_add_location(self):
        response = self.app.post('/locations', json={"id": 1, "name": "Test Location"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Location", response.get_data(as_text=True))

    def test_get_location(self):
        self.app.post('/locations', json={"id": 2, "name": "Another Location"})
        response = self.app.get('/locations/2')
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        self.app.post('/locations', json={"id": 3, "name": "Update Location"})
        response = self.app.put('/locations/3', json={"name": "Updated Location"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Location", response.get_data(as_text=True))

    def test_delete_location(self):
        self.app.post('/locations', json={"id": 4, "name": "Delete Location"})
        response = self.app.delete('/locations/4')
        self.assertEqual(response.status_code, 204)

if _name_ == '_main_':
    unittest.main()