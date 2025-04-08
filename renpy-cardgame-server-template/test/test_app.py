import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Player

class TestGameServer(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_join_game(self):
        res = self.client.post('/join', json={'name': 'Alice'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('Player Alice joined the game!', res.get_json()['message'])

    def test_update_player(self):
        self.client.post('/join', json={'name': 'Bob'})
        res = self.client.post('/update_player', json={'name': 'Bob', 'wins': 3, 'losses': 1})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Player Bob's stats updated!", res.get_json()['message'])



if __name__ == "__main__":
    unittest.main()
