# Leviton Cloud Services API model Person.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Person(BaseModel):
    def __init__(self, session, model_id=None):
        super(Person, self).__init__(session, model_id)

    @classmethod
    def apply_password(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/applyPassword"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def confirm(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/confirm"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/count"
        return session.call_api(api, attribs, 'get')

    def count_access_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_management_tiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_notification_subscriptions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_notification_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_role_mappings(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person"
        return session.call_api(api, attribs, 'post')

    def create_access_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_management_tiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person"
        return session.call_api(api, attribs, 'post')

    def create_notification_subscriptions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_notification_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_role_mappings(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_access_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_management_tiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_notification_subscriptions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_notification_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_role_mappings(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_access_tokens(self, access_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens/{1}".format(self._id, access_token_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations/{1}".format(self._id, invitation_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/{1}".format(self._id, management_tier_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_notification_subscriptions(self, notification_subscription_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions/{1}".format(self._id, notification_subscription_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_notification_triggers(self, notification_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers/{1}".format(self._id, notification_trigger_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions/{1}".format(self._id, permission_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_preferences(self, preference_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_permissions(self, residential_permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions/{1}".format(self._id, residential_permission_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_role_mappings(self, role_mapping_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings/{1}".format(self._id, role_mapping_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_user_feedbacks(self, user_feedback_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def exists_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/rel/{1}".format(self._id, management_tier_id)
        return self._session.call_api(api, attribs, 'head')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = Person(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_access_tokens(self, access_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens/{1}".format(self._id, access_token_id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations/{1}".format(self._id, invitation_id)
        data = self._session.call_api(api, attribs, 'get')

        from .invitation import Invitation
        model = Invitation(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/{1}".format(self._id, management_tier_id)
        data = self._session.call_api(api, attribs, 'get')

        from .management_tier import ManagementTier
        model = ManagementTier(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_notification_subscriptions(self, notification_subscription_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions/{1}".format(self._id, notification_subscription_id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_notification_triggers(self, notification_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers/{1}".format(self._id, notification_trigger_id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions/{1}".format(self._id, permission_id)
        data = self._session.call_api(api, attribs, 'get')

        from .permission import Permission
        model = Permission(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_preferences(self, preference_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference_id)
        data = self._session.call_api(api, attribs, 'get')

        from .preference import Preference
        model = Preference(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_permissions(self, residential_permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions/{1}".format(self._id, residential_permission_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_permission import ResidentialPermission
        model = ResidentialPermission(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_role_mappings(self, role_mapping_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings/{1}".format(self._id, role_mapping_id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_user_feedbacks(self, user_feedback_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback_id)
        data = self._session.call_api(api, attribs, 'get')

        from .user_feedback import UserFeedback
        model = UserFeedback(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Person/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_access_tokens(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_current(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def get_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .invitation import Invitation
        result = []
        if items is not None:
            for data in items:
                model = Invitation(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_management_tiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .management_tier import ManagementTier
        result = []
        if items is not None:
            for data in items:
                model = ManagementTier(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_notification_subscriptions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_notification_triggers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .permission import Permission
        result = []
        if items is not None:
            for data in items:
                model = Permission(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_preferences(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .preference import Preference
        result = []
        if items is not None:
            for data in items:
                model = Preference(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_permission import ResidentialPermission
        result = []
        if items is not None:
            for data in items:
                model = ResidentialPermission(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_role_mappings(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_user_feedbacks(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .user_feedback import UserFeedback
        result = []
        if items is not None:
            for data in items:
                model = UserFeedback(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def link_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/rel/{1}".format(self._id, management_tier_id)
        data = self._session.call_api(api, attribs, 'put')

        from .management_tier import ManagementTier
        model = ManagementTier(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def login(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/login"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def logout(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/logout"
        return session.call_api(api, attribs, 'post')

    def notify(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notify".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def reset_password(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/reset"
        return session.call_api(api, attribs, 'post')

    def unlink_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/rel/{1}".format(self._id, management_tier_id)
        return self._session.call_api(api, attribs, 'delete')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_access_tokens(self, access_token_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/accessTokens/{1}".format(self._id, access_token_id)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/invitations/{1}".format(self._id, invitation_id)
        data = self._session.call_api(api, attribs, 'put')

        from .invitation import Invitation
        model = Invitation(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_management_tiers(self, management_tier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/managementTiers/{1}".format(self._id, management_tier_id)
        data = self._session.call_api(api, attribs, 'put')

        from .management_tier import ManagementTier
        model = ManagementTier(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_notification_subscriptions(self, notification_subscription_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationSubscriptions/{1}".format(self._id, notification_subscription_id)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_notification_triggers(self, notification_trigger_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/notificationTriggers/{1}".format(self._id, notification_trigger_id)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_permissions(self, permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/permissions/{1}".format(self._id, permission_id)
        data = self._session.call_api(api, attribs, 'put')

        from .permission import Permission
        model = Permission(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_preferences(self, preference_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/preferences/{1}".format(self._id, preference_id)
        data = self._session.call_api(api, attribs, 'put')

        from .preference import Preference
        model = Preference(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_permissions(self, residential_permission_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/residentialPermissions/{1}".format(self._id, residential_permission_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_permission import ResidentialPermission
        model = ResidentialPermission(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_role_mappings(self, role_mapping_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/roleMappings/{1}".format(self._id, role_mapping_id)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_user_feedbacks(self, user_feedback_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/userFeedbacks/{1}".format(self._id, user_feedback_id)
        data = self._session.call_api(api, attribs, 'put')

        from .user_feedback import UserFeedback
        model = UserFeedback(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person"
        data = session.call_api(api, attribs, 'put')

        model = Person(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

    def verify_email(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Person/{0}/verifyEmail".format(self._id)
        return self._session.call_api(api, attribs, 'post')

