from django.test import TestCase
from resources.models import ManagerControl


class ManagerControlModelTest(TestCase):
    fixtures = ['manager_fixture']

    def test_manager_control_relations(self):
        man_ctrl = ManagerControl.objects.all().first()
        self.assertEqual(man_ctrl.user.id, 1)
        self.assertEqual(man_ctrl.user.username, 'joaop')
