import sys
from decora_wifi import DecoraWiFiSession
from decora_wifi.models.person import Person
from decora_wifi.models.residential_account import ResidentialAccount
from decora_wifi.models.residence import Residence


class Decora(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.residences = []
        self.switches = {}
        self.session = None
        self._authenticate()
        self._get_residences()
        self._get_switches()

    def _authenticate(self):
        session = DecoraWiFiSession()
        session.login(self.email, self.password)
        self.session = session

    def _get_residences(self):
        perms = self.session.user.get_residential_permissions()
        self.residences = []
        for permission in perms:
            if permission.residentialAccountId is not None:
                acct = ResidentialAccount(
                    self.session, permission.residentialAccountId)
                for res in acct.get_residences():
                    self.residences.append(res)
            elif permission.residenceId is not None:
                res = Residence(self.session, permission.residenceId)
                self.residences.append(res)

    def _get_switches(self):
        self.switches = {}
        for residence in self.residences:
            for switch in residence.get_iot_switches():
                name = switch.name.split(" ")
                name = name[2]
                self.switches[name] = switch

    def set_param(self, name, key, value):
        if not self.switches[name]:
            return "{} does not exist".format(name)

        self.switches[name].update_attributes({key: value})
        return None

    def get_switches(self):
        return self.switches.keys()
