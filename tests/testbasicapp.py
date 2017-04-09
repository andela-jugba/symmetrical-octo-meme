from unittest import TestCase
from app import create_app, db
from flask import current_app

class TestBasicApp(TestCase):
  def setUp(self):
    self.app = create_app('test')
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def testAppExits(self):
    self.assertIsNotNone(current_app)

  def testAppConfig(self):
    self.assertTrue(self.app.config['TESTING'])
