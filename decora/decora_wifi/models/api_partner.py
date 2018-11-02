# Leviton Cloud Services API model ApiPartner.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class ApiPartner(BaseModel):
    def __init__(self, session, model_id=None):
        super(ApiPartner, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/count"
        return session.call_api(api, attribs, 'get')

    def count_oauth_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners"
        return session.call_api(api, attribs, 'post')

    def create_oauth_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_oauth_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_oauth_tokens(self, oauth_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens/{1}".format(self._id, oauth_token_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = ApiPartner(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_oauth_tokens(self, oauth_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens/{1}".format(self._id, oauth_token_id)
        data = self._session.call_api(api, attribs, 'get')

        from .oauth_token import OauthToken
        model = OauthToken(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/ApiPartners/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_oauth_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .oauth_token import OauthToken
        result = []
        if items is not None:
            for data in items:
                model = OauthToken(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_oauth_tokens(self, oauth_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/{0}/oauthTokens/{1}".format(self._id, oauth_token_id)
        data = self._session.call_api(api, attribs, 'put')

        from .oauth_token import OauthToken
        model = OauthToken(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners"
        data = session.call_api(api, attribs, 'put')

        model = ApiPartner(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ApiPartners/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

