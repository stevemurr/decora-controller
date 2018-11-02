# Leviton Cloud Services API model TouchscreenDefinition.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class TouchscreenDefinition(BaseModel):
    def __init__(self, session, model_id=None):
        super(TouchscreenDefinition, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions"
        return session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = TouchscreenDefinition(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/TouchscreenDefinitions/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_whitelist(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}/whitelist".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .whitelist import Whitelist
        model = Whitelist(self._session, data['id'])
        model.data = data
        return model

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions"
        data = session.call_api(api, attribs, 'put')

        model = TouchscreenDefinition(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/TouchscreenDefinitions/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

