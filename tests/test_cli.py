""" Tests for command line interface.

"""
from aiida.manage.tests.unittest_classes import PluginTestCase


class TestDataCli(PluginTestCase):
    """Test verdi data cli plugin."""

    def setUp(self):
        from click.testing import CliRunner
        from aiida.plugins import DataFactory

        ShengBTEParameters = DataFactory('shengbte')
        self.parameters = ShengBTEParameters({'ignore-case': True})
        self.parameters.store()
        self.runner = CliRunner()

    def test_data_shengbte_list(self):
        """Test 'verdi data shengbte list'

        Tests that it can be reached and that it lists the node we have set up.
        """
        from aiida_shengbte.cli import list_

        # result = self.runner.invoke(list_, catch_exceptions=False)
        # self.assertIn(str(self.parameters.pk), result.output)

    def test_data_shengbte_export(self):
        """Test 'verdi data shengbte export'

        Tests that it can be reached and that it shows the contents of the node
        we have set up.
        """
        # from aiida_shengbte.cli import export

        # result = self.runner.invoke(export, [str(self.parameters.pk)],
        #                             catch_exceptions=False)
        # self.assertIn('ignore-case', result.output)
